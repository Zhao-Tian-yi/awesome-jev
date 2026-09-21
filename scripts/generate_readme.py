#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Render a compact, trilingual research map without changing the audited facts."""
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
 'tagline': '**Compare how Jev-like models make decisions, how they are trained, and which code and weights you can use.**',
 'description': 'A research-oriented map of Jev and System One Models. Architectures, decision readouts, RLCD and Calibration — with links to the implementation behind each label.',
 'counts': '{n} community implementations · 1 official reference · {p} related papers · English / 中文 / 日本語',
 'bookmark': 'Star this map to find the comparisons and source links again when choosing or training a decision model.',
 'nav': ['Models', 'Find by goal', 'Recent updates', 'Training audit', 'Contribute'],
 'what': 'What is Jev?',
 'intro': '`State + runtime-defined question + options → typed probabilistic decision`. Noul estimates a binary condition; Choice compares declared options; Score returns an ordered-level distribution and expectation. This list separates the official API from independent implementations. **Non-AR does not imply diffusion; direct probabilities do not guarantee Calibration.**',
 'models': 'Model Landscape',
 'scope': 'Official Jev stays first. Other rows follow verified first-public dates, then the existing curation order when dates are unknown. Stars do not determine the order.',
 'table_help': 'Definitions, date coverage, and full technical comparison',
 'help': '**{u}/{n} first-public dates remain unverified.** Unknown is not replaced by repository creation dates or later releases. **AR Decoding** in the full table concerns answer generation, not backbone pretraining. **Artifacts** distinguishes project weights, adapters/heads and reused upstream models. RL labels are version-specific; see the actual methods rather than treating every RLCD claim as the proprietary recipe.',
 'details': '[Full technical table](docs/comparison.md) · [Evidence and version notes](docs/evidence.md) · [Audit limitations](docs/audit.md)',
 'audit': 'Technical audit: {at}.',
 'stars': 'Stars sampled at {at}; this is a popularity snapshot, not a quality score. [API sources](data/github-stars.json). Refreshing stars does not refresh the technical audit.',
 'properties': 'Expand the Jev-like capability matrix',
 'properties_help': '✅ documented · ⚠️ partial, variant-specific or ordinary batching · ❌ absent · ? unverified. Shared State means reused computation. Parallel Q distinguishes native slots from batched rows. Calibration records procedures/evidence, not a universal guarantee.',
 'start': 'Find by goal', 'start_note': 'Reading routes, not a ranking. Check the linked version notes before using a project.',
 'goals': ['Try decisions without training', 'Train a decision mechanism', 'Explore encoder-based decisions', 'Study diffusion answer slots', 'Inspect calibration-aware RL'],
 'inspect': ['Candidate logits and shared prefixes', 'Decision heads, data formats and training paths', 'Bidirectional encoding and dynamic candidates', 'Masked slots, denoising steps and question isolation', 'Sampling, rewards, gradients and checkpoint scope'],
 'goal_headers': ['Goal', 'Starting points', 'What to inspect'],
 'updates': 'Recent updates', 'updates_note': 'These dates describe changes to this list, not upstream release dates. Star-only refreshes are excluded. [Full log](docs/updates.md).',
 'update_headers': ['Date', 'Type', 'Change', 'Evidence'],
 'guide': 'Research guide', 'guide_headers': ['Question', 'Read'],
 'questions': ['How is a probability produced?', 'What does RLCD mean in each implementation?', 'How does Jev relate to LLMs, rerankers and diffusion?', 'How should quality, Calibration and efficiency be compared?'],
 'guide_note': 'Methods remain separate from measured outcomes. We do not infer vendor internals from API behavior or compare unmatched benchmark numbers as a leaderboard.',
 'timeline': 'Expand verified version / artifact milestones',
 'timeline_note': 'Version milestones are not first-public dates. Official Jev is kept first; the remaining dated milestones are chronological.',
 'papers': 'Related research', 'papers_note': 'Primary research ordered by arXiv v1 date; these are related methods, not automatically Jev implementations.',
 'official': 'Official resources and tools',
 'official_note': '[TypeSafe](https://typesafe.ai/) · [Launch article](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [Documentation](https://docs.typesafe.ai/) · [Official GitHub](https://github.com/typesafe-ai). SDK source is not Jev model source. Current verification boundaries are retained in the [audit](docs/audit.md).',
 'tools': ['Python client and API schemas', 'JavaScript/TypeScript client', 'Ordinary LLM APIs behind a System One comparison interface', 'Question-design guidance and worked patterns; not a network specification'],
 'application': 'Application example: [Jevenator 2](https://github.com/mmastrac/jevenator2) uses a separate decision endpoint for region-scan localization. It is not a new backbone or evidence of official Jev architecture.',
 'contribute': 'Contributing',
 'contribute_note': 'Found a project or a mistake? Send a link, a short explanation and supporting evidence. **No YAML editing or three-language translation is required to open an issue.** Maintainers validate facts and synchronize translations before inclusion.',
 'submit': 'Suggest a project', 'correct': 'Correct an entry',
 'maintain': 'For a pull request, edit the YAML facts and regenerate the pages. [Contribution guide](CONTRIBUTING.md) · [Content license](LICENSE) · [Code license](LICENSE-CODE). Independent resource; not affiliated with TypeSafe AI.',
 'awesome': 'An awesome list of awesome Jev lists. Known first-public dates first; Unknown does not mean unpublished.',
},
'zh': {
 'tagline': '**看清 Jev-like 模型怎么实现、怎么训练，以及哪些代码和权重可以使用。**',
 'description': '面向研究的 Jev 与 System One Model 技术图谱。对照架构、决策读出、RLCD 与 Calibration，并追溯每个技术标签背后的实现。',
 'counts': '{n} 个社区实现 · 1 个官方参照 · {p} 篇相关研究 · English / 中文 / 日本語',
 'bookmark': '收藏这份对照表，后续选模型、查训练方法和源码证据时方便回来查看。',
 'nav': ['模型比较', '按需求查找', '近期更新', '训练核查', '参与贡献'],
 'what': '什么是 Jev？',
 'intro': '`State + 运行时定义的问题 + 选项 → 有类型的概率决策`。Noul 估计二元条件，Choice 比较给定候选，Score 返回有序等级分布及其期望。本仓库区分官方 API 与独立实现。**Non-AR 不等于 diffusion；直接输出概率不保证 Calibration。**',
 'models': '模型全景',
 'scope': '官方 Jev 始终置顶。其余按已核实的首次公开日期升序排列；未知日期保留原策展顺序，不按 Stars 排名。',
 'table_help': '展开字段定义、日期完整性与详细对照',
 'help': '**{u}/{n} 个首次公开日期仍未核实。** 保留 Unknown，不以仓库创建时间或后续版本日期代替。详细表的 **AR Decoding** 判断答案是否逐 token 生成，而非底座预训练方式。**Artifacts** 区分项目权重、adapter/head 与复用上游模型。RL 状态以具体版本为准，不能把社区 RLCD 名称直接当成官方配方。',
 'details': '[完整技术对照表](docs/comparison.md) · [证据与版本说明](docs/evidence.md) · [核查限制](docs/audit.md)',
 'audit': '技术核查日期：{at}。',
 'stars': 'Stars 采集时间：{at}；仅作关注度快照，不代表技术质量。[API 来源](data/github-stars.json)。刷新 Stars 不等于重新核查技术信息。',
 'properties': '展开 Jev-like 能力矩阵',
 'properties_help': '✅ 文档支持 · ⚠️ 部分、特定版本或普通 batch · ❌ 不支持 · ? 未核实。Shared State 指计算复用，Parallel Q 区分原生槽位与批处理行；Calibration 记录方法或证据，不代表普遍保证。',
 'start': '按需求查找', 'start_note': '这是阅读入口，不是性能排名。使用前请查看所链接的版本与证据说明。',
 'goals': ['不训练，先做本地决策', '自己训练决策机制', '研究 encoder 决策路线', '研究 diffusion 回答槽位', '研究校准相关强化学习'],
 'inspect': ['候选 logits 与共享前缀', 'Decision Head、数据格式与训练路径', '双向编码与动态候选', 'Masked slots、去噪步数与问题隔离', '采样、reward、梯度与 checkpoint 范围'],
 'goal_headers': ['目标', '阅读入口', '重点检查'],
 'updates': '近期更新', 'updates_note': '这里记录本仓库的变化，不是上游项目的发布日期；仅刷新 Stars 不计入实质更新。[完整记录](docs/updates.md)。',
 'update_headers': ['日期', '类型', '变化', '依据'],
 'guide': '研究导航', 'guide_headers': ['问题', '资料'],
 'questions': ['模型如何得到概率？', '不同实现中的 RLCD 到底是什么？', 'Jev 与 LLM、reranker、diffusion 有什么关系？', '如何公平比较能力、Calibration 与效率？'],
 'guide_note': '训练机制与实测效果分开记录；不从 API 行为推断厂商内部架构，也不将不同条件下的 benchmark 数字拼成排行榜。',
 'timeline': '展开已核实的版本／产物里程碑',
 'timeline_note': '版本里程碑不等于首次公开日期。官方 Jev 置顶，其后已知日期升序排列。',
 'papers': '相关研究', 'papers_note': '按 arXiv v1 日期排列的一手研究；相关方法不直接算作 Jev 实现。',
 'official': '官方资源与工具',
 'official_note': '[TypeSafe](https://typesafe.ai/) · [发布文章](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [官方文档](https://docs.typesafe.ai/) · [官方 GitHub](https://github.com/typesafe-ai)。SDK 源码不等于 Jev 模型源码；具体核实范围见[核查记录](docs/audit.md)。',
 'tools': ['Python 客户端与 API schema', 'JavaScript/TypeScript 客户端', '把普通 LLM API 包装成 System One 比较接口', '问题设计指南与实例，不是网络结构说明'],
 'application': '应用示例：[Jevenator 2](https://github.com/mmastrac/jevenator2) 调用独立决策端点完成区域扫描定位；它不是新底座，也不能证明官方 Jev 的架构。',
 'contribute': '参与贡献',
 'contribute_note': '发现新项目或错误？提交链接、简短说明和证据即可。**提 Issue 不要求修改 YAML，也不要求翻译三种语言。** 维护者核查后再同步事实与翻译。',
 'submit': '推荐项目', 'correct': '纠正条目',
 'maintain': '提交 PR 时修改 YAML 事实源并重新生成页面。[贡献指南](CONTRIBUTING.md) · [内容许可](LICENSE) · [代码许可](LICENSE-CODE)。本仓库为独立整理，与 TypeSafe AI 无隶属关系。',
 'awesome': '收集 awesome Jev lists 的 awesome list。已知首次公开日期优先；Unknown 不代表尚未公开。',
},
'ja': {
 'tagline': '**Jev-like モデルの仕組み、学習方法、利用できるコードと重みを比較する。**',
 'description': 'Jev と System One Models の研究マップ。アーキテクチャ、判断の読み出し、RLCD、Calibration を整理し、各技術ラベルの実装にリンクします。',
 'counts': '{n} 件のコミュニティ実装 · 1 件の公式参照 · {p} 件の関連研究 · English / 中文 / 日本語',
 'bookmark': 'モデル選定や学習方法の調査に戻れるよう、この比較表を Star で保存してください。',
 'nav': ['モデル比較', '目的から探す', '最近の更新', '学習の検証', '貢献方法'],
 'what': 'Jev とは？',
 'intro': '`State + 実行時に定義する質問 + 選択肢 → 型付きの確率的判断`。Noul は二値条件、Choice は候補集合、Score は順序付きレベルの分布と期待値を扱います。公式 API と独立実装を区別します。**Non-AR は diffusion と同義ではなく、確率の直接出力も Calibration を保証しません。**',
 'models': 'モデル一覧',
 'scope': '公式 Jev を先頭に固定し、確認済みの初回公開日を昇順、未確認項目を既存の収録順に並べます。Stars 順ではありません。',
 'table_help': '列の定義、日付の確認状況、詳細比較を開く',
 'help': '**初回公開日は {n} 件中 {u} 件が未確認です。** 作成日や後続リリース日で代用しません。詳細表の **AR Decoding** は回答の逐次生成を指し、事前学習方式ではありません。**Artifacts** はプロジェクト固有の重み、adapter/head、上流モデルの利用を区別します。RL の記述は対象の版に限定し、コミュニティの RLCD を公式手法と同一視しません。',
 'details': '[詳細比較表](docs/comparison.md) · [根拠と版の注記](docs/evidence.md) · [検証の制約](docs/audit.md)',
 'audit': '技術情報の検証時点：{at}。',
 'stars': 'Stars の取得時点：{at}。注目度の参考値であり、品質評価ではありません。[API 出典](data/github-stars.json)。Stars の更新は技術情報の再検証を意味しません。',
 'properties': 'Jev-like 機能比較を開く',
 'properties_help': '✅ 文書上の対応 · ⚠️ 部分的、特定の版または通常の batch · ❌ 非対応 · ? 未確認。Shared State は計算の再利用を指し、Parallel Q は native slots と batch を区別します。Calibration は手順や根拠の記録であり、一般的保証ではありません。',
 'start': '目的から探す', 'start_note': '性能ランキングではなく、読む順序の案内です。利用前に版と根拠を確認してください。',
 'goals': ['追加学習なしで判断を試す', '判断機構を学習する', 'Encoder 系の判断を調べる', 'Diffusion の回答スロットを調べる', '確率校正を考慮した RL を調べる'],
 'inspect': ['候補 logits と共有 prefix', 'Decision Head、データ形式、学習経路', '双方向 encoding と動的候補', 'Masked slots、denoising 回数、質問の独立性', 'Sampling、reward、gradient、checkpoint の範囲'],
 'goal_headers': ['目的', '出発点', '確認する点'],
 'updates': '最近の更新', 'updates_note': 'このリストの変更日であり、上流の公開日ではありません。Stars の更新だけは含めません。[全履歴](docs/updates.md)。',
 'update_headers': ['日付', '種類', '変更', '根拠'],
 'guide': '研究ガイド', 'guide_headers': ['問い', '資料'],
 'questions': ['確率はどのように得られるか？', '各実装で RLCD は何を意味するか？', 'LLM、reranker、diffusion とどう違うか？', '能力、Calibration、効率をどう公平に比較するか？'],
 'guide_note': '学習機構と測定結果を分けます。API の振る舞いから内部構造を推定したり、異なる条件の数値をランキングにまとめたりしません。',
 'timeline': '確認済みの版／成果物の節目を開く',
 'timeline_note': '版の節目は初回公開日ではありません。公式 Jev を先頭にし、日付がある節目を昇順に並べます。',
 'papers': '関連研究', 'papers_note': 'arXiv v1 の日付順の一次研究です。関連手法をそのまま Jev 実装として扱いません。',
 'official': '公式リソースとツール',
 'official_note': '[TypeSafe](https://typesafe.ai/) · [発表記事](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [公式文書](https://docs.typesafe.ai/) · [公式 GitHub](https://github.com/typesafe-ai)。SDK のコードは Jev のモデルコードではありません。確認範囲は[検証記録](docs/audit.md)に残します。',
 'tools': ['Python クライアントと API schema', 'JavaScript/TypeScript クライアント', '通常の LLM API を System One の比較インターフェースに変換', '質問設計のガイドと例。ネットワーク仕様ではない'],
 'application': '応用例：[Jevenator 2](https://github.com/mmastrac/jevenator2) は別の判断 endpoint で領域走査を行います。新しい backbone や公式 Jev の構造を示す証拠ではありません。',
 'contribute': '貢献方法',
 'contribute_note': '新しい実装や誤りを見つけたら、リンク、短い説明、根拠を送ってください。**Issue の投稿には YAML 編集や三言語への翻訳は不要です。** 収録前にメンテナーが事実と翻訳を確認します。',
 'submit': '実装を推薦', 'correct': '項目を訂正',
 'maintain': 'PR では YAML の事実を編集し、ページを再生成します。[貢献ガイド](CONTRIBUTING.md) · [コンテンツのライセンス](LICENSE) · [コードのライセンス](LICENSE-CODE)。TypeSafe AI とは無関係の独立リソースです。',
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


def disclosure(summary, *body):
    return '<details>\n<summary>' + summary + '</summary>\n\n' + '\n\n'.join(body) + '\n\n</details>'


def update_table(updates, lang, prefix=''):
    return table(TEXT[lang]['update_headers'], [[e['date'], e['kind'], e['summary'][lang],
        f"[Source]({e['url'] if '://' in e['url'] else prefix + e['url']})"] for e in updates])


def render_readme(lang, data, papers, lists, snapshot, updates):
    t = TEXT[lang]
    projects = data['projects']
    by_id = {p['id']: p for p in projects}
    nav_targets = ['#models', '#start-here', '#updates', 'docs/training.md', '#contributing']
    parts = ['# Awesome Jev', '> ' + NOTICE[lang],
        '[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)',
        t['tagline'], t['description'],
        t['counts'].format(n=sum(not p['official'] for p in projects), p=len(papers)),
        ' · '.join(f'[{label}]({target})' for label, target in zip(t['nav'], nav_targets)),
        t['bookmark'], '<!-- Generated from data/*.yaml. See scripts/generate_readme.py. -->',
        '## ' + t['what'], t['intro'], '<a id="models"></a>', '## ' + t['models'], t['scope'],
        '<!-- landscape:start -->\n' + landscape(projects, snapshot) + '\n<!-- landscape:end -->',
        t['details'],
        disclosure(t['table_help'], t['help'].format(u=sum(p['release_date'] is None for p in projects), n=len(projects)),
                   t['audit'].format(at=data['checked_at']), t['stars'].format(at=snapshot['checked_at'])),
        disclosure(t['properties'], t['properties_help'],
                   '<!-- properties:start -->\n' + property_table(projects) + '\n<!-- properties:end -->'),
        '<a id="start-here"></a>', '## ' + t['start'], t['start_note'],
        table(t['goal_headers'], [[t['goals'][i], ' · '.join(evidence_link(by_id[j]) for j in ids),
                                 f"[{t['inspect'][i]}]({guide})"] for i, (ids, guide) in enumerate(ROUTES)]),
        '<a id="updates"></a>', '## ' + t['updates'], t['updates_note'], update_table(updates[:3], lang),
        '## ' + t['guide'],
        table(t['guide_headers'], [[q, f'[{path.rsplit("/", 1)[-1]}]({path})'] for q, path in zip(t['questions'],
              ['docs/architecture.md', 'docs/training.md', 'docs/jev-vs-models.md', 'docs/evaluation.md'])]), t['guide_note']]
    events = [(p['release_date'] or 'Unknown', p['name'], 'Official reference') for p in projects if p['official']]
    milestones = []
    for p in projects:
        for e in p['release_evidence']:
            if e.get('date') and not e.get('first_public'):
                milestones.append((e['date'], p['name'], f"[Version/artifact]({e['url']})"))
    parts += [disclosure(t['timeline'], t['timeline_note'], table(['Date', 'Project', 'Milestone'],
              events + sorted(milestones, key=lambda row: row[0]))),
        '## ' + t['papers'], t['papers_note'], table(['Date', 'Paper', 'Topic'],
        [[p['date'], f"[{p['title']}]({p['paper']})", p['topic']] for p in papers]),
        '## ' + t['official'], t['official_note'], table(['Tool', 'Purpose'],
        [[f'[{name}](https://github.com/typesafe-ai/{name})', description] for name, description in zip(
          ['typesafe-sdk-python', 'typesafe-sdk-js', 'system-one-adapter-python', 'skills'], t['tools'])]),
        t['application'], '<a id="contributing"></a>', '## ' + t['contribute'], t['contribute_note'],
        f"[{t['submit']}]({REPO}/issues/new?template=suggest-project.yml) · [{t['correct']}]({REPO}/issues/new?template=metadata-correction.yml)",
        t['maintain'], '## Awesome Awesome Jev 😄', t['awesome'],
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
