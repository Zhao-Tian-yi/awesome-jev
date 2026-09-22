#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Render four-section, trilingual READMEs and retain detailed research documents."""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path
from urllib.parse import urlencode

import yaml
from github_stars import NOTICE, load_snapshot, star_cell

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/Zhao-Tian-yi/awesome-jev'
LANGUAGES = {'en': 'README.md', 'zh': 'README.zh-CN.md', 'ja': 'README.ja.md'}
SYMBOL = {'yes': '✅', 'no': '❌', 'partial': '⚠️', 'unknown': '?'}
OUTPUT = {'Noul': 'N', 'Choice': 'C', 'Score': 'S', 'Binary': 'B',
          'Probability Distribution': 'P', 'Ranking': 'R', 'Multi-class': 'M',
          'Regression': 'Reg', 'Confidence': 'Conf'}
TEXT = {
'en': {
 'description': 'A research-oriented map of Jev and System One Models: implementations, architectures, training, and available code and weights.',
 'models': 'Model Landscape',
 'scope': 'Official Jev stays first. Other rows follow verified first-public dates, then existing curation order for unknown dates. Stars do not determine the order.',
 'details': '[Full technical table](docs/comparison.md) · [Evidence and version notes](docs/evidence.md) · [Audit limitations](docs/audit.md)',
 'metadata': 'Technical audit: **{audit}** · Stars snapshot: **{stars}** ([API sources](data/github-stars.json)). Unknown means the first-public date is unverified; stars are not a quality score.',
 'start': 'Find by goal',
 'start_note': 'Reading routes, not a ranking. Check the linked version notes before using a project.',
 'goals': ['Try decisions without training', 'Train a decision mechanism', 'Explore encoder-based decisions', 'Study diffusion answer slots', 'Inspect calibration-aware RL'],
 'inspect': ['Candidate logits and shared prefixes', 'Decision heads, data formats and training paths', 'Bidirectional encoding and dynamic candidates', 'Masked slots, denoising steps and question isolation', 'Sampling, rewards, gradients and checkpoint scope'],
 'goal_headers': ['Goal', 'Starting points', 'What to inspect'],
 'update_headers': ['Date', 'Type', 'Change', 'Evidence'],
 'official': 'Official resources and tools',
 'official_note': '[TypeSafe](https://typesafe.ai/) · [Launch article](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [Documentation](https://docs.typesafe.ai/) · [Official GitHub](https://github.com/typesafe-ai). SDK source is not Jev model source; see the [audit](docs/audit.md) for verification boundaries.',
 'tools': ['Python client and API schemas', 'JavaScript/TypeScript client', 'Ordinary LLM APIs behind a System One comparison interface', 'Question-design guidance and worked patterns; not a network specification'],
 'awesome': 'An awesome list of awesome Jev lists. Known first-public dates first; Unknown does not mean unpublished.',
},
'zh': {
 'description': '面向研究的 Jev 与 System One Model 技术图谱，整理开源实现、模型架构、训练方法及可用代码与权重。',
 'models': '模型全景',
 'scope': '官方 Jev 始终置顶。其余按已核实的首次公开日期升序排列；未知日期保留原策展顺序，不按 Stars 排名。',
 'details': '[完整技术对照表](docs/comparison.md) · [证据与版本说明](docs/evidence.md) · [核查限制](docs/audit.md)',
 'metadata': '技术核查：**{audit}** · Stars 快照：**{stars}**（[API 来源](data/github-stars.json)）。Unknown 表示首次公开日期未核实；Stars 不代表技术质量。',
 'start': '按需求查找',
 'start_note': '这是阅读入口，不是性能排名。使用前请查看所链接的版本与证据说明。',
 'goals': ['不训练，先做本地决策', '自己训练决策机制', '研究 encoder 决策路线', '研究 diffusion 回答槽位', '研究校准相关强化学习'],
 'inspect': ['候选 logits 与共享前缀', 'Decision Head、数据格式与训练路径', '双向编码与动态候选', 'Masked slots、去噪步数与问题隔离', '采样、reward、梯度与 checkpoint 范围'],
 'goal_headers': ['目标', '阅读入口', '重点检查'],
 'update_headers': ['日期', '类型', '变化', '依据'],
 'official': '官方资源与工具',
 'official_note': '[TypeSafe](https://typesafe.ai/) · [发布文章](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [官方文档](https://docs.typesafe.ai/) · [官方 GitHub](https://github.com/typesafe-ai)。SDK 源码不等于 Jev 模型源码；具体核实范围见[核查记录](docs/audit.md)。',
 'tools': ['Python 客户端与 API schema', 'JavaScript/TypeScript 客户端', '把普通 LLM API 包装成 System One 比较接口', '问题设计指南与实例，不是网络结构说明'],
 'awesome': '收集 awesome Jev lists 的 awesome list。已知首次公开日期优先；Unknown 不代表尚未公开。',
},
'ja': {
 'description': 'Jev と System One Models の研究マップ。公開実装、アーキテクチャ、学習方法、利用できるコードと重みを整理します。',
 'models': 'モデル一覧',
 'scope': '公式 Jev を先頭に固定し、確認済みの初回公開日を昇順、未確認項目を既存の収録順に並べます。Stars 順ではありません。',
 'details': '[技術比較の全項目](docs/comparison.md) · [根拠とバージョン情報](docs/evidence.md) · [検証上の制約](docs/audit.md)',
 'metadata': '技術検証：**{audit}** · Stars 取得：**{stars}**（[API 出典](data/github-stars.json)）。Unknown は初回公開日の未確認を示します。Stars は技術品質の指標ではありません。',
 'start': '目的から探す',
 'start_note': 'ランキングではなく、読み始めるための案内です。利用前にリンク先の版と根拠を確認してください。',
 'goals': ['学習せずに判断を試す', '判断機構を学習する', 'encoder による判断を調べる', 'diffusion の回答スロットを調べる', '校正を考慮した RL を調べる'],
 'inspect': ['候補 logits と共有 prefix', 'Decision Head、データ形式、学習経路', '双方向 encoding と動的な候補', 'Masked slots、denoising の回数、質問の独立性', 'sampling、reward、gradient、checkpoint の範囲'],
 'goal_headers': ['目的', '入口', '確認する点'],
 'update_headers': ['日付', '種類', '変更', '根拠'],
 'official': '公式リソースとツール',
 'official_note': '[TypeSafe](https://typesafe.ai/) · [発表記事](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [公式文書](https://docs.typesafe.ai/) · [公式 GitHub](https://github.com/typesafe-ai)。SDK のコードは Jev のモデルコードではありません。確認範囲は[検証記録](docs/audit.md)に残します。',
 'tools': ['Python クライアントと API schema', 'JavaScript/TypeScript クライアント', '通常の LLM API を System One の比較インターフェースに変換', '質問設計のガイドと例。ネットワーク仕様ではない'],
 'awesome': 'Awesome Jev リストを集める awesome list。確認済みの初回公開日を優先し、Unknown は未公開を意味しません。',
}}
ROUTES = [(['semif', 'mini-jev'], 'docs/comparison.md'),
          (['kev', 'nanojev', 'luce'], 'docs/training.md'),
          (['laya', 'von'], 'docs/architecture.md'),
          (['openjev-diffusiongemma'], 'docs/architecture.md'),
          (['eve-rlcd', 'laya', 'nanojev'], 'docs/training.md')]


def load_data(root: Path = ROOT):
    def read(name):
        return yaml.safe_load((root / 'data' / name).read_text(encoding='utf-8'))
    return read('projects.yaml'), read('papers.yaml')['papers'], read('awesome-lists.yaml')['lists']


def load_updates(root: Path = ROOT):
    updates = yaml.safe_load((root / 'data/updates.yaml').read_text(encoding='utf-8'))['updates']
    seen = set()
    for entry in updates:
        if entry['id'] in seen or set(entry['summary']) != set(LANGUAGES):
            raise ValueError('Duplicate update or missing translation: ' + entry['id'])
        seen.add(entry['id'])
        dt.date.fromisoformat(entry['date'])
        if entry['kind'] not in ('Added', 'Updated', 'Corrected') or not entry['url']:
            raise ValueError('Invalid update: ' + entry['id'])
    return sorted(updates, key=lambda e: e['date'], reverse=True)


def ordered(items):
    return sorted(items, key=lambda p: (not p.get('official', False),
                  p.get('release_date') is None, p.get('release_date') or '9999'))


def esc(value):
    return str(value).replace('|', r'\|').replace('\n', ' ')


def table(headers, rows):
    if any(len(row) != len(headers) for row in rows):
        raise ValueError('Table row width disagrees with header')
    return '\n'.join(['| ' + ' | '.join(headers) + ' |',
        '|' + '|'.join('---:' if h == 'GitHub Stars' else '---' for h in headers) + '|'] +
        ['| ' + ' | '.join(esc(v) for v in row) + ' |' for row in rows])


def evidence_link(p, prefix='docs/'):
    return f"[{p['name']}]({prefix}evidence.md#{p['id']})"


def artifact(p):
    status = p['weights']
    target = p.get('huggingface')
    if status == 'API only':
        return f"[API only]({p.get('website') or p['github']})"
    if status == 'Yes':
        return f'[Project weights]({target})' if target else 'Project weights; see evidence'
    if status == 'Partial':
        return f'[Adapter/head]({target})' if target else 'Adapter/head; see evidence'
    if status == 'No' and p['training'] == 'None':
        return f'[Upstream weights]({target})' if target else f"[Upstream model / setup]({p['github']})"
    if status == 'No':
        return 'No project-weight release'
    return 'Availability unverified'


def landscape(projects, snapshot):
    rows = []
    for p in ordered(projects):
        rows.append([f"[{p['name']}]({p['github']})", star_cell(p['github'], snapshot),
            p['release_date'] or 'Unknown', f"{p['backbone']}<br>{p['params']}",
            f"{p['architecture']}<br>{p['decision_mechanism']}",
            f"{p['training']}<br>RL: {p['rl']}", artifact(p),
            f"[Sources](docs/evidence.md#{p['id']})"])
    return table(['Project', 'GitHub Stars', 'First Public', 'Backbone / Size',
                  'Decision Architecture', 'Training / RL', 'Artifacts', 'Evidence'], rows)


def full_table(projects):
    return table(['Project', 'First Public', 'Backbone', 'Params', 'Architecture', 'Training',
                  'RL / RLCD', 'AR Decoding', 'Decision Mechanism', 'Outputs', 'Project Weights'],
        [[evidence_link(p, ''), p['release_date'] or 'Unknown', p['backbone'], p['params'],
          p['architecture'], p['training'], p['rl'], p['ar'], p['decision_mechanism'],
          '/'.join(OUTPUT[v] for v in p['outputs']), p['weights']] for p in ordered(projects)])


def property_table(projects):
    keys = ['typed', 'dynamic', 'variable', 'native', 'calibration', 'shared_state', 'multi_q', 'parallel_q', 'non_ar']
    return table(['Project', 'Typed', 'Dynamic Options', 'Variable K', 'Native P', 'Calibration',
                  'Shared State', 'Multi-Q', 'Parallel Q', 'Non-AR'],
        [[f"[{p['name']}]({p['github']})"] + [SYMBOL[p['properties'][k]] for k in keys]
         for p in ordered(projects)])


def update_table(updates, lang, prefix=''):
    return table(TEXT[lang]['update_headers'], [[e['date'], e['kind'], e['summary'][lang],
        f"[Source]({e['url'] if '://' in e['url'] else prefix + e['url']})"] for e in updates])


def render_readme(lang, data, papers, lists, snapshot, updates):
    """Only these four sections belong on the homepage; supporting data stays intact."""
    t = TEXT[lang]
    projects = data['projects']
    by_id = {p['id']: p for p in projects}
    navigation = [(t['models'], '#models'), (t['start'], '#start-here'),
                  (t['official'], '#official'), ('Awesome Awesome Jev 😄', '#awesome-awesome-jev')]
    parts = ['# Awesome Jev', '> ' + NOTICE[lang],
        '[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)',
        t['description'], ' · '.join(f'[{label}]({target})' for label, target in navigation),
        '<!-- Generated from data/*.yaml. See scripts/generate_readme.py. -->',
        '<a id="models"></a>', '## ' + t['models'], t['scope'],
        '<!-- landscape:start -->\n' + landscape(projects, snapshot) + '\n<!-- landscape:end -->',
        t['metadata'].format(audit=data['checked_at'], stars=snapshot['checked_at']), t['details'],
        '<a id="start-here"></a>', '## ' + t['start'], t['start_note'],
        table(t['goal_headers'], [[t['goals'][i], ' · '.join(evidence_link(by_id[j]) for j in ids),
                                 f"[{t['inspect'][i]}]({guide})"] for i, (ids, guide) in enumerate(ROUTES)]),
        '<a id="official"></a>', '## ' + t['official'], t['official_note'],
        table(['Tool', 'Purpose'], [[f'[{name}](https://github.com/typesafe-ai/{name})', description]
            for name, description in zip(['typesafe-sdk-python', 'typesafe-sdk-js', 'system-one-adapter-python', 'skills'], t['tools'])]),
        '<a id="awesome-awesome-jev"></a>', '## Awesome Awesome Jev 😄', t['awesome'],
        table(['Repository', 'GitHub Stars', 'First Public', 'Languages', 'Focus', 'Notes'],
        [[f"[{p['name']}]({p['url']})", star_cell(p['url'], snapshot), p['release_date'] or 'Unknown',
          ' / '.join(p['languages']), p['focus'], p['notes'][lang]] for p in ordered(lists)])]
    return '\n\n'.join(parts) + '\n'


def render_evidence(data):
    parts = ['# Project evidence and version notes', '[Home](../README.md) · [Full comparison](comparison.md) · [Audit limitations](audit.md)',
        'Generated from `data/projects.yaml`. Source inspection, documentation and author claims are distinguished below. Links are not an endorsement; no new technical audit is implied by a layout update.']
    for p in ordered(data['projects']):
        correction = REPO + '/issues/new?' + urlencode({'template': 'metadata-correction.yml', 'title': 'Correction: ' + p['name'], 'project': p['name']})
        parts += ['## ' + p['id'], f"**[{p['name']}]({p['github']})** · First public: {p['release_date'] or 'Unknown'}", p['notes']['en'],
                  f"**RL status:** {p['rl_status']}", f'[Report a correction]({correction})']
        if p['huggingface']:
            parts.append(f"**Model/artifact link:** {p['huggingface']} (project-weight status: {p['weights']}; upstream links are identified in the notes).")
        parts.append(table(['Source', 'Supports', 'Evidence level'],
            [[f"[Source {i+1}]({e['url']})", ', '.join(e['supports']), e['level']] for i, e in enumerate(p['evidence'])]))
        if p['release_evidence']:
            parts.append(table(['Date', 'Artifact / limitation'],
                [[e['date'] or 'Unknown', f"[{e['kind']}]({e['url']})"] for e in p['release_evidence']]))
    return '\n\n'.join(parts) + '\n'


def outputs(root: Path = ROOT):
    data, papers, lists = load_data(root)
    snapshot = load_snapshot(root)
    updates = load_updates(root)
    comparison = '# Full technical comparison\n\n[Home](../README.md) · [Evidence](evidence.md) · [Training audit](training.md)\n\n'
    comparison += 'All fields are retained from the audited YAML. AR Decoding refers to token-by-token answer generation, not the backbone. Project Weights excludes reused upstream weights. Unknown dates remain unknown.\n\n'
    comparison += full_table(data['projects']) + '\n'
    comparison += '\n## Jev-like capability matrix\n\n'
    comparison += '✅ documented · ⚠️ partial, variant-specific or ordinary batching · ❌ absent · ? unverified. Shared State means reused computation. Parallel Q distinguishes native slots from batched rows. Calibration records procedures/evidence, not a universal guarantee.\n\n'
    comparison += '<!-- properties:start -->\n' + property_table(data['projects']) + '\n<!-- properties:end -->\n'
    log = '# Curation updates\n\n[Home](../README.md)\n\nChanges to this list, not upstream release dates. Star-only refreshes are excluded.\n\n'
    log += update_table(updates, 'en', '../') + '\n'
    return {**{path: render_readme(lang, data, papers, lists, snapshot, updates) for lang, path in LANGUAGES.items()},
            'docs/evidence.md': render_evidence(data), 'docs/comparison.md': comparison, 'docs/updates.md': log}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail rather than rewrite stale generated pages.')
    args = parser.parse_args()
    try:
        stale = []
        generated = outputs()
        for path, text in generated.items():
            dest = ROOT / path
            if args.check:
                if not dest.exists() or dest.read_text(encoding='utf-8') != text:
                    stale.append(path)
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(text, encoding='utf-8')
        if stale:
            print('Stale generated files: ' + ', '.join(stale), file=sys.stderr)
            return 1
        print('Generated pages are synchronized.' if args.check else f'Generated {len(generated)} files.')
        return 0
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        print(f'Generation failed: {exc}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
