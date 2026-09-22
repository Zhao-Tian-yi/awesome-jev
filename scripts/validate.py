#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate facts, chronology, generated-page parity and optionally HTTP links."""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import ipaddress
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml
from generate_readme import ROOT, LANGUAGES, load_data, ordered, outputs

REQUIRED = {'id','name','official','release_date','release_evidence','github','website',
            'paper','huggingface','backbone','params','architecture','training','rl',
            'rl_status','ar','decision_mechanism','outputs','weights','properties',
            'evidence','notes'}
PROPS = {'typed','dynamic','variable','native','calibration','shared_state','multi_q','parallel_q','non_ar'}
MARKERS = ('landscape',)


def canonical_url(url):
    parsed=urllib.parse.urlsplit(url)
    path=parsed.path.rstrip('/')
    if parsed.netloc.lower() in ('github.com','www.github.com'):
        path=path.removesuffix('.git').lower()
    match=re.fullmatch(r'/(?:abs|pdf|html)/(\d{4}\.\d+)(?:v\d+)?(?:\.pdf)?',path)
    if parsed.netloc.lower()=='arxiv.org' and match:
        path='/abs/'+match.group(1)
    return (parsed.netloc.lower(),path)


def date_valid(value,cutoff):
    if value is None:
        return True
    if not isinstance(value,str) or not re.fullmatch(r'\d{4}-\d{2}(?:-\d{2})?',value):
        return False
    try:
        return dt.date.fromisoformat(value if len(value)==10 else value+'-01')<=cutoff
    except ValueError:
        return False


def check_data(data,papers,lists):
    errors=[]
    cutoff=dt.date.fromisoformat(str(data['checked_at']))
    projects=data['projects']
    if not projects or sum(p.get('official') is True for p in projects)!=1 or not projects[0].get('official'):
        errors.append('Exactly one official project must be first.')
    if projects!=ordered(projects):
        errors.append('Projects are not in official-first / known-date / unknown order.')
    def unique(items,key,label,urls=False):
        seen=set()
        for p in items:
            value=p.get(key)
            if value is None:
                continue
            value=canonical_url(value) if urls else str(value).casefold()
            if value in seen:
                errors.append(f'Duplicate {label}: {p.get(key)}')
            seen.add(value)
    unique(projects,'id','project ID'); unique(projects,'name','project name')
    unique(projects,'github','project GitHub URL',True); unique(projects,'paper','project paper URL',True)
    for p in projects:
        label=p.get('id','<missing ID>')
        missing=REQUIRED-set(p)
        if missing:
            errors.append(f'{label}: missing fields {sorted(missing)}')
            continue
        if not date_valid(p['release_date'],cutoff):
            errors.append(f'{label}: invalid/future first-public date')
        if p['release_date'] is not None and not any(
            e.get('date')==p['release_date'] and e.get('first_public') is True and e.get('url')
            for e in p['release_evidence']):
            errors.append(f'{label}: dated first release needs explicit first_public evidence')
        for key in ('website','paper','huggingface'):
            if p[key] is not None and not isinstance(p[key],str):
                errors.append(f'{label}: {key} must be a URL or null')
        if p['ar'] not in ('Yes','No','Hybrid','Unknown'):
            errors.append(f'{label}: invalid AR decision-path value')
        if p['weights'] not in ('Yes','No','Partial','API only','Unknown'):
            errors.append(f'{label}: invalid project-weight status')
        if p['rl']=='RLCD' and not p['official']:
            errors.append(f'{label}: unqualified RLCD is reserved for official terminology')
        if not p['evidence'] or not all(e.get('url') and e.get('supports') and e.get('level') for e in p['evidence']):
            errors.append(f'{label}: each evidence record needs URL, supports and level')
        if set(p['notes'])!=set(LANGUAGES) or not all(isinstance(v,str) and v.strip() for v in p['notes'].values()):
            errors.append(f'{label}: three localized notes required')
        if set(p['properties'])!=PROPS or any(v not in ('yes','no','partial','unknown') for v in p['properties'].values()):
            errors.append(f'{label}: invalid property matrix')
        if p['ar']=='No' and p['properties'].get('non_ar')!='yes':
            errors.append(f'{label}: AR and Non-AR property disagree')
        if p['properties'].get('parallel_q')=='yes' and p['properties'].get('multi_q')!='yes':
            errors.append(f'{label}: native parallel Q requires Multi-Q support')
        if not isinstance(p['outputs'],list) or not p['outputs']:
            errors.append(f'{label}: at least one output is required')
        for e in p['release_evidence']:
            if not e.get('url') or not date_valid(e.get('date'),cutoff):
                errors.append(f'{label}: invalid release evidence')
    unique(papers,'id','paper ID'); unique(papers,'paper','paper URL',True)
    if papers!=sorted(papers,key=lambda p:p['date']):
        errors.append('Related papers must be chronological.')
    for p in papers:
        if not date_valid(p.get('date'),cutoff) or p.get('date') is None:
            errors.append(f"{p.get('id')}: paper needs a verified valid date")
        if set(p.get('notes',{}))!=set(LANGUAGES):
            errors.append(f"{p.get('id')}: missing localized paper notes")
    unique(lists,'url','awesome-list URL',True)
    if lists!=ordered(lists):
        errors.append('Awesome lists must be in known-date / unknown order.')
    for item in lists:
        if not date_valid(item.get('release_date'),cutoff):
            errors.append(f"{item['name']}: invalid resource-list date")
        if not item.get('date_evidence') or not item.get('date_note'):
            errors.append(f"{item['name']}: date evidence/limitation required")
        if set(item.get('notes',{}))!=set(LANGUAGES):
            errors.append(f"{item['name']}: missing localized list notes")
    return errors


def check_pages(root=ROOT):
    errors=[]; expected=outputs(root); tables={}; urlsets={}
    for path,text in expected.items():
        dest=root/path
        if not dest.exists() or dest.read_text(encoding='utf-8')!=text:
            errors.append('Stale or missing generated file: '+path)
        if path.startswith('README'):
            tables[path]=[text.split(f'<!-- {m}:start -->',1)[1].split(f'<!-- {m}:end -->',1)[0] for m in MARKERS]
            urlsets[path]=set(re.findall(r'\]\(([^)]+)\)',text))
            if text.rsplit('\n## ',1)[-1].splitlines()[0]!='Awesome Awesome Jev 😄':
                errors.append('Final README section is not Awesome Awesome Jev.')
    if len({tuple(v) for v in tables.values()})!=1 or len({frozenset(v) for v in urlsets.values()})!=1:
        errors.append('Translated READMEs disagree on technical tables or link sets.')
    for path in root.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
            if '://' in target or target.startswith(('#','mailto:')):
                continue
            local=urllib.parse.unquote(target.split('#')[0])
            if local and not (path.parent/local).exists():
                errors.append(f'{path.relative_to(root)}: broken local link {target}')
    return errors


def urls_in(value):
    if isinstance(value,dict):
        for v in value.values():
            yield from urls_in(v)
    elif isinstance(value,list):
        for v in value:
            yield from urls_in(v)
    elif isinstance(value,str) and value.startswith('https://') and ' ' not in value:
        yield value


def safe_url(url):
    parsed=urllib.parse.urlsplit(url)
    if parsed.scheme!='https' or parsed.username or parsed.password or not parsed.hostname or parsed.port not in (None,443):
        raise ValueError('Only public HTTPS URLs without credentials are allowed')
    addresses=socket.getaddrinfo(parsed.hostname,443,type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global for a in addresses):
        raise ValueError('Non-public address refused')


class PublicRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        safe_url(newurl)
        return super().redirect_request(req,fp,code,msg,headers,newurl)


def check_url(url):
    try:
        safe_url(url)
        opener=urllib.request.build_opener(PublicRedirect)
        headers={'User-Agent':'awesome-jev-link-check/1.0'}
        for method in ('HEAD','GET'):
            try:
                with opener.open(urllib.request.Request(url,headers=headers,method=method),timeout=8) as response:
                    return 'ok',url,str(response.status)
            except urllib.error.HTTPError as exc:
                if method=='HEAD' and exc.code in (400,403,405,501):
                    continue
                return ('dead' if exc.code in (404,410) else 'unverified'),url,str(exc.code)
        return 'unverified',url,'HEAD/GET not accepted'
    except (OSError,ValueError,urllib.error.URLError) as exc:
        return 'unverified',url,str(exc)


def self_test(data,papers,lists):
    def rejected(mutator):
        trial=copy.deepcopy(data); mutator(trial)
        assert check_data(trial,papers,lists), 'Invalid fixture was accepted'
    rejected(lambda d:d['projects'][1].pop('params'))
    rejected(lambda d:d['projects'][1].update(name=d['projects'][0]['name']))
    rejected(lambda d:d['projects'][1].update(github=d['projects'][2]['github']))
    rejected(lambda d:d['projects'][1].update(release_date='2026-02-30'))
    rejected(lambda d:d['projects'][1].update(release_date='2099-01-01'))
    rejected(lambda d:d['projects'][1].update(release_date='2026-09-16'))
    rejected(lambda d:d['projects'][1].update(rl='RLCD'))
    rejected(lambda d:d['projects'].reverse())
    rejected(lambda d:d['projects'][1]['notes'].pop('ja'))
    assert canonical_url('https://github.com/A/B.git')==canonical_url('https://github.com/a/b/')
    assert canonical_url('https://arxiv.org/pdf/2507.16806v2.pdf')==canonical_url('https://arxiv.org/abs/2507.16806')
    assert [x['id'] for x in ordered([{'id':'u','release_date':None},{'id':'d','release_date':'2026-09-01'},{'id':'o','official':True,'release_date':None}])]==['o','d','u']
    return 12


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--links',action='store_true',help='Check primary HTTPS URLs; 404/410 fail, blocked/transient endpoints warn.')
    args=parser.parse_args()
    try:
        data,papers,lists=load_data()
        errors=check_data(data,papers,lists)+check_pages()
        if errors:
            print('\n'.join('ERROR: '+e for e in errors),file=sys.stderr)
            return 1
        tests=self_test(data,papers,lists)
        unknown=sum(p['release_date'] is None for p in data['projects'])
        print(f"PASS: {len(data['projects'])} projects, {len(papers)} papers, {len(lists)} lists; three-language parity; {tests} validator self-checks.")
        print(f'NOTICE: {unknown} first-public project dates remain unverified; see docs/audit.md.')
        if args.links:
            urls=set(urls_in([data,papers,lists]))
            for path in ROOT.rglob('*.md'):
                urls.update(u for u in re.findall(r'\]\((https://[^)]+)\)',path.read_text(encoding='utf-8')))
            with ThreadPoolExecutor(max_workers=8) as pool:
                results=list(pool.map(check_url,sorted(urls)))
            for status,url,reason in results:
                if status!='ok':
                    print(f'{status.upper()}: {url} ({reason})')
            counts={s:sum(row[0]==s for row in results) for s in ('ok','dead','unverified')}
            print('HTTP results: '+str(counts))
            return int(counts['dead']>0)
        return 0
    except (OSError,ValueError,KeyError,TypeError,AssertionError,yaml.YAMLError) as exc:
        print(f'Validation failed: {exc}',file=sys.stderr)
        return 1

if __name__=='__main__':
    raise SystemExit(main())
