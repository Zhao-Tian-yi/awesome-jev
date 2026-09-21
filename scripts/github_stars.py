#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Refresh numeric GitHub star snapshots and decorate generated README tables.

Run `python scripts/github_stars.py --refresh`, then the normal README generator.
Counts are snapshots, never a technical-quality score or a sorting key.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import time
import urllib.request
import urllib.error
from urllib.parse import urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = 'data/github-stars.json'
NOTICE = {
    'en': '**Frequent, real-time updates ahead:** This repository will be updated intensively in the near term, tracking new Jev / System One Models implementations, architectures, training methods, and evaluations.',
    'zh': '**本仓库近期会高强度实时更新**，持续跟进 Jev / System One Models 的开源实现、模型架构、训练方法与评测进展。',
    'ja': '**当面は高頻度でリアルタイム更新：** Jev / System One Models の公開実装、アーキテクチャ、学習手法、評価の最新動向を集中的に追い、このリポジトリを随時更新します。',
}
CAPTION = {
    'en': '**GitHub Stars** snapshot: {at}. Popularity only, not a quality ranking; the existing ordering is unchanged. — = no model repository. [Snapshot / API sources](data/github-stars.json).',
    'zh': '**GitHub Stars** 采集时间：{at}。仅作关注度参考，不代表技术质量，原有排序不变；— 表示没有对应模型仓库。[快照与 API 来源](data/github-stars.json)。',
    'ja': '**GitHub Stars** 取得時点：{at}。注目度の参考値であり、品質ランキングではありません。既存の並び順は維持します。— は対応するモデルリポジトリなし。[スナップショットと API 出典](data/github-stars.json)。',
}


def repo_name(url):
    """Accept actual GitHub repositories, not organizations or non-GitHub URLs."""
    if not isinstance(url, str):
        return None
    parsed = urlsplit(url)
    if parsed.scheme != 'https' or parsed.netloc.lower() != 'github.com':
        return None
    parts = parsed.path.strip('/').removesuffix('.git').split('/')
    if len(parts) != 2 or any(not re.fullmatch(r'[A-Za-z0-9_.-]+', part) for part in parts):
        return None
    return '/'.join(parts)


def load_snapshot(root=ROOT):
    snapshot = json.loads((root / SNAPSHOT).read_text(encoding='utf-8'))
    at = dt.datetime.fromisoformat(snapshot['checked_at'].replace('Z', '+00:00'))
    if at.tzinfo is None or not isinstance(snapshot['repositories'], dict):
        raise ValueError('Star snapshot needs a timezone and a repository map')
    for name, record in snapshot['repositories'].items():
        if repo_name('https://github.com/' + name) != name:
            raise ValueError('Invalid repository in star snapshot: ' + name)
        count = record['stars']
        if type(count) is not int or count < 0:
            raise ValueError('Invalid star count for ' + name)
        if record['source'] != 'https://api.github.com/repos/' + name:
            raise ValueError('Invalid star source for ' + name)
    return snapshot


def star_cell(url, snapshot):
    name = repo_name(url)
    if name is None:
        return '—'
    record = snapshot['repositories'].get(name.lower())
    if record is None:
        return 'Unknown'
    return f"[{record['stars']:,}](https://github.com/{name}/stargazers)"


def add_star_column(block, snapshot):
    """Add a column immediately after Project/Repository without reordering rows."""
    result = []
    row_index = 0
    for line in block.splitlines():
        if not line.startswith('|'):
            result.append(line)
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]
        if row_index == 0:
            value = 'GitHub Stars'
        elif row_index == 1:
            value = '---:'
        else:
            match = re.search(r'\]\((https://github\.com/[^)]+)\)', cells[0])
            value = star_cell(match.group(1) if match else None, snapshot)
        cells.insert(1, value)
        result.append('| ' + ' | '.join(cells) + ' |')
        row_index += 1
    if row_index < 2:
        raise ValueError('Expected a Markdown repository table')
    return '\n'.join(result)


def annotate_readme(text, lang, snapshot):
    """Decorate model landscape and related-list tables; keep the property matrix lean."""
    title = '# Awesome Jev\n'
    if not text.startswith(title):
        raise ValueError('Unexpected README title')
    text = text.replace(title, title + '\n> ' + NOTICE[lang] + '\n', 1)
    start, end = '<!-- landscape:start -->', '<!-- landscape:end -->'
    before, tail = text.split(start, 1)
    block, after = tail.split(end, 1)
    caption = CAPTION[lang].format(at=snapshot['checked_at'])
    text = before + caption + '\n\n' + start + '\n' + add_star_column(block.strip(), snapshot) + '\n' + end + after
    heading = '## Awesome Awesome Jev 😄'
    before, final = text.rsplit(heading, 1)
    text = before + heading + add_star_column(final, snapshot) + '\n'
    return text


def refresh(root=ROOT):
    projects = yaml.safe_load((root / 'data/projects.yaml').read_text(encoding='utf-8'))['projects']
    lists = yaml.safe_load((root / 'data/awesome-lists.yaml').read_text(encoding='utf-8'))
    if isinstance(lists, dict):
        lists = lists.get('lists', lists.get('awesome_lists', []))
    names = {repo_name(p.get('github')) for p in projects}
    names.update(repo_name(p.get('url')) for p in lists)
    names.discard(None)
    records = {}
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'awesome-jev-star-snapshot'}
    token = os.getenv('GH_TOKEN') or os.getenv('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    for name in sorted(names, key=str.lower):
        canonical = name.lower()
        source = 'https://api.github.com/repos/' + canonical
        for attempt in range(3):
            try:
                request = urllib.request.Request(source, headers=headers)
                with urllib.request.urlopen(request, timeout=20) as response:
                    metadata = json.load(response)
                count = metadata['stargazers_count']
                if type(count) is not int or count < 0:
                    raise ValueError('Invalid API star count: ' + name)
                records[canonical] = {'stars': count, 'source': source}
                print(f'{name}: {count}')
                break
            except (urllib.error.URLError, TimeoutError):
                if attempt == 2:
                    raise
                time.sleep(attempt + 1)
    snapshot = {'checked_at': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'),
                'note': 'GitHub stargazers_count snapshot; not a quality ranking. Organization pages are not model repositories.',
                'repositories': records}
    destination = root / SNAPSHOT
    temporary = destination.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(destination)
    print(f'Recorded {len(records)} repositories in {SNAPSHOT}')


def self_test():
    sample = {'checked_at': '2026-09-21T00:00:00Z', 'repositories': {'owner/repo': {'stars': 1234}}}
    assert repo_name('https://github.com/typesafe-ai') is None
    assert repo_name('https://not-github.com/owner/repo') is None
    assert star_cell('https://github.com/Owner/Repo', sample) == '[1,234](https://github.com/Owner/Repo/stargazers)'
    assert star_cell('https://github.com/typesafe-ai', sample) == '—'
    text = '# Awesome Jev\n\n<!-- landscape:start -->\n| Project | AR |\n| --- | --- |\n| [R](https://github.com/Owner/Repo) | No |\n<!-- landscape:end -->\n\n## Awesome Awesome Jev 😄\n\n| Repository | Date |\n| --- | --- |\n| [R](https://github.com/Owner/Repo) | Unknown |\n'
    for lang in NOTICE:
        result = annotate_readme(text, lang, sample)
        assert result.count('GitHub Stars |') == 2
        assert result.count('[1,234]') == 2
        assert '> ' + NOTICE[lang] in result
        assert result.endswith('\n') and '2026-09-21T00:00:00Z' in result
    print('Star readout and trilingual rendering tests passed.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
    if args.refresh:
        refresh()
    if not (args.self_test or args.refresh):
        parser.error('Choose --refresh or --self-test')


if __name__ == '__main__':
    main()
