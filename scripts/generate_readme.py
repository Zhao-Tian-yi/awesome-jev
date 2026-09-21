#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Deterministically render three READMEs and an evidence index from YAML facts."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {'en': 'README.md', 'zh': 'README.zh-CN.md', 'ja': 'README.ja.md'}
SYMBOL = {'yes': '✅', 'no': '❌', 'partial': '⚠️', 'unknown': '?'}
OUTPUT = {'Noul': 'N', 'Choice': 'C', 'Score': 'S', 'Binary': 'B',
          'Probability Distribution': 'P', 'Ranking': 'R', 'Multi-class': 'M',
          'Regression': 'Reg', 'Confidence': 'Conf'}
TEXT = {
'en': {
 'description': 'A curated, research-oriented map of Jev and System One Models — open-source implementations, architectures, training, calibrated decisions, and evaluation.',
 'headings': ['What is Jev?', 'Model Landscape', 'Jev-like Properties', 'Timeline', 'Official Resources', 'Open-Source Models', 'Architecture', 'Training & Calibration', 'Decision Mechanisms', 'Benchmarks & Evaluation', 'Related Research', 'SDKs & Tools', 'Applications', 'Contributing'],
 'intro': '`State + runtime-defined question + options → typed probabilistic decision`. Noul estimates a binary condition, Choice distributes probability over a supplied menu, and Score returns an ordered-level distribution and expectation. The interface is not a disclosed architecture. Native numerical output is not a Calibration guarantee.',
 'snapshot': 'Audit snapshot', 'scope': 'official reference + {community} independent implementations. Not a ranking or an exhaustive inventory.',
 'dates': '**First-public dates: {unknown}/{total} core rows unverified.** Unknown is intentional; repository creation and later releases are not substituted. Official Jev stays first; verified dates sort ascending, followed by unknowns in stable curation order. See [audit limitations](docs/audit.md).',
 'legend': '**AR** means token-by-token decision generation, not backbone pretraining. **Weights** means project-specific artifacts: Partial = adapter/head; ❌ can still use open upstream weights. N/C/S = Noul/Choice/Score; B/P/R = Binary/Probability Distribution/Ranking. Version details and sources: [evidence index](docs/evidence.md).',
 'properties': '✅ documented support · ⚠️ partial, variant-specific or ordinary batching · ❌ absent · ? unverified. Calibration marks documented procedures/evidence, not a universal guarantee. Shared means reused computation, not merely shared input. Parallel Q distinguishes native slots from batched rows; official behavior alone does not disclose the internals.',
 'timeline': 'Official first, then dated **version/artifact milestones**. These are not first-public dates and do not determine model-table order.',
 'unverified': 'First publication unverified', 'version': 'version/artifact milestone only',
 'official': '[TypeSafe](https://typesafe.ai/) · [Launch article](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [Documentation](https://docs.typesafe.ai/) · [Official GitHub](https://github.com/typesafe-ai). The skill was readable; launch/model-limit pages could not be freshly verified in this audit. Model weights and the proprietary training recipe are not provided by the SDKs.',
 'models': 'Core rows contain an inspectable local decision mechanism or dedicated model, not merely an API call. [Detailed notes and evidence](docs/evidence.md) identify the reviewed path; optional or historical variants are not silently merged.',
 'architecture': 'Separate backbone family, decision readout and execution schedule. Causal logit readout, trained pointer/scoring heads, encoder models and masked-diffusion slots all occur here. **Non-AR ≠ diffusion; one request ≠ one forward.** [Architecture](docs/architecture.md) · [Jev vs adjacent models](docs/jev-vs-models.md).',
 'training': 'Official RLCD is a vendor term with unverified proprietary details. Community `RLCD (claimed)` entries name their own method and evidence; CE/Brier or temperature fitting alone is **not RL**. Prototype and released-checkpoint status are separate. **RLCR is not established to equal RLCD.** [Training audit](docs/training.md).',
 'mechanism': 'The readout column distinguishes candidate-token logits, a trained pointer/scalar head and masked answer slots. Returned probabilities are conditional on the declared alternatives; a valid schema does not make a decision true. [Mechanism comparisons](docs/jev-vs-models.md).',
 'evaluation': 'Report task quality, Calibration, risk-coverage, unseen questions/options and matched latency/memory. No upstream benchmark was rerun for this list. [Evaluation protocol](docs/evaluation.md) · [SemIf fixtures](https://github.com/TheoLeeCJ/SemIf/tree/master/benchmarks) · [mini-Jev controls](https://github.com/r-ms/mini-jev).',
 'papers': 'Related primary research, ordered by arXiv v1 date; these are not Jev implementations.',
 'tools': ['Python client and API schemas; not model source.', 'JavaScript/TypeScript client; not model source.', 'Wraps ordinary LLM APIs as a System One comparison interface.', 'Question-design guidance and examples; not a network specification.'],
 'application': '[Jevenator 2](https://github.com/mmastrac/jevenator2) performs region-scan localization through a separate decision endpoint. It is an application, not a new backbone or evidence of official Jev architecture.',
 'contributing': 'Edit the YAML facts and localized notes, then run `python scripts/generate_readme.py` and `python scripts/validate.py`. The READMEs and evidence index are generated. [Contribution rules](CONTRIBUTING.md) · [Content license](LICENSE) · [Code license](LICENSE-CODE). Independent resource; not affiliated with TypeSafe.',
 'awesome': 'An awesome list of awesome Jev lists. Known dates first; Unknown does not mean unpublished. Month-only dates do not imply an exact day.',
 'date': 'Date', 'project': 'Project', 'event': 'Event', 'paper': 'Paper', 'topic': 'Topic', 'repository': 'Repository', 'release': 'Release Date', 'languages': 'Languages', 'focus': 'Focus', 'notes': 'Notes', 'tool': 'Tool', 'purpose': 'Purpose',
},
'zh': {
 'description': '面向研究的 Jev 与 System One Model 技术图谱，系统整理开源实现、模型架构、训练方法、校准决策学习与评测。',
 'headings': ['什么是 Jev？', '模型全景', 'Jev-like 能力矩阵', '时间线', '官方资源', '开源模型', '架构', '训练与 Calibration', '决策机制', '基准与评测', '相关研究', 'SDK 与工具', '应用', '参与贡献'],
 'intro': '`State + 运行时定义的问题 + 选项 → 有类型的概率决策`。Noul 估计二元条件，Choice 给出候选集合上的概率分布，Score 返回有序等级分布及其期望。接口定义不等于内部架构披露，原生数值输出也不保证 Calibration。',
 'snapshot': '核查快照', 'scope': '个官方参照 + {community} 个独立实现；不作排名，也不宣称穷尽全部仓库。',
 'dates': '**首次公开日期：{unknown}/{total} 个核心条目仍未证实。** 保留 Unknown，不以仓库创建时间或后续版本日期代替。官方 Jev 始终第一；已证实日期升序，其后为保持原策展顺序的未知日期项目。参见[核查限制](docs/audit.md)。',
 'legend': '**AR** 判断决策是否逐 token 生成，不判断底座的预训练方式。**Weights** 指项目自身发布的权重；Partial 为 adapter/head，❌ 仍可能依赖开放的上游权重。N/C/S = Noul/Choice/Score；B/P/R = Binary/Probability Distribution/Ranking。[证据索引](docs/evidence.md)记录版本细节与来源。',
 'properties': '✅ 文档支持 · ⚠️ 部分、特定版本或普通 batch · ❌ 不支持 · ? 未核实。Calibration 记录方法或评测证据，不代表普遍保证。Shared 指计算复用，不只是输入相同。Parallel Q 区分原生槽位与批处理行；官方接口行为也不等于内部结构披露。',
 'timeline': '官方置顶，其后列出已确认日期的**版本／产物里程碑**。这些不是首次公开日期，也不用于替代模型表的排序依据。',
 'unverified': '首次公开日期未证实', 'version': '仅为版本／产物里程碑',
 'official': '[TypeSafe](https://typesafe.ai/) · [发布文章](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [官方文档](https://docs.typesafe.ai/) · [官方 GitHub](https://github.com/typesafe-ai)。本次可读取官方 skill，但未能重新获取发布文章及模型长度限制页面；SDK 不包含模型权重与专有训练配方。',
 'models': '核心表收录可检查的本地决策机制或专门模型，不收录只有 API 调用的应用。[详细说明与证据](docs/evidence.md)标明核查路径，不混合可选功能和历史版本。',
 'architecture': '分别描述底座、决策读出和执行方式。当前包含 causal logits、训练后的 pointer/scoring head、encoder 和 masked diffusion 槽位。**Non-AR ≠ diffusion；一次请求 ≠ 一次前向。** [架构说明](docs/architecture.md) · [与相邻模型的关系](docs/jev-vs-models.md)。',
 'training': '官方 RLCD 为专有细节未核实的厂商术语。社区 `RLCD (claimed)` 须附具体方法和证据；只有 CE/Brier 或 temperature fitting **不属于 RL**。实验原型与已发布 checkpoint 分开标注。**没有证据证明 RLCR 等于 RLCD。** [训练核查](docs/training.md)。',
 'mechanism': '决策读出分别标记候选 token logits、训练得到的 pointer/scalar head 与 masked answer slots。概率以给定候选集合为条件；格式合法不等于语义正确。[机制比较](docs/jev-vs-models.md)。',
 'evaluation': '同时报告任务能力、Calibration、risk-coverage、未见问题／选项，以及匹配条件下的延迟和显存。本次未重跑上游 benchmark。[评测协议](docs/evaluation.md) · [SemIf 数据与脚本](https://github.com/TheoLeeCJ/SemIf/tree/master/benchmarks) · [mini-Jev 对照](https://github.com/r-ms/mini-jev)。',
 'papers': '按 arXiv v1 日期排列的一手相关研究；这些论文不直接算作 Jev 实现。',
 'tools': ['Python 客户端与 API schema，不是模型源码。', 'JavaScript/TypeScript 客户端，不是模型源码。', '将普通 LLM API 包装成 System One 比较接口。', '问题设计指南与示例，不是网络结构说明。'],
 'application': '[Jevenator 2](https://github.com/mmastrac/jevenator2) 调用独立决策端点完成区域扫描定位。它属于应用，不是新底座，也不能证明官方 Jev 架构。',
 'contributing': '修改 YAML 事实与多语言说明，再运行 `python scripts/generate_readme.py` 和 `python scripts/validate.py`。README 与证据索引均自动生成。[贡献规则](CONTRIBUTING.md) · [内容许可](LICENSE) · [代码许可](LICENSE-CODE)。本仓库为独立资料整理，与 TypeSafe 无隶属关系。',
 'awesome': '收集 awesome Jev lists 的 awesome list。已知日期优先；Unknown 不代表未公开，月份精度也不代表具体某一天。',
 'date': '日期', 'project': '项目', 'event': '事件', 'paper': '论文', 'topic': '方向', 'repository': '仓库', 'release': '首次公开日期', 'languages': '语言', 'focus': '侧重', 'notes': '说明', 'tool': '工具', 'purpose': '用途',
},
'ja': {
 'description': 'Jev と System One Models の研究マップ。公開実装、アーキテクチャ、学習手法、確率校正、評価を整理します。',
 'headings': ['Jev とは？', 'モデル一覧', 'Jev-like 機能比較', 'タイムライン', '公式リソース', 'オープンソースモデル', 'アーキテクチャ', '学習と Calibration', '意思決定の仕組み', 'ベンチマークと評価', '関連研究', 'SDK とツール', 'アプリケーション', '貢献方法'],
 'intro': '`State + 実行時に定義する質問 + 選択肢 → 型付きの確率的判断`。Noul は二値条件、Choice は候補集合の確率分布、Score は順序付きレベルの分布と期待値を返します。API の定義は内部構造の公開ではなく、数値を直接返すだけでは Calibration は保証されません。',
 'snapshot': '監査時点', 'scope': '件の公式参照 + {community} 件の独立実装。ランキングでも網羅的な全件一覧でもありません。',
 'dates': '**主要行の初回公開日は {total} 件中 {unknown} 件が未確認です。** リポジトリ作成日や後続リリース日で置き換えず、Unknown を残します。公式 Jev を先頭に固定し、確認済みの日付を昇順、未確認項目を既存の収録順に並べます。[監査上の制約](docs/audit.md)。',
 'legend': '**AR** は判断の token-by-token 生成を指し、事前学習方式ではありません。**Weights** はプロジェクト固有の成果物です。Partial は adapter/head、❌ でも上流の公開重みは利用できます。N/C/S = Noul/Choice/Score、B/P/R = Binary/Probability Distribution/Ranking。[根拠一覧](docs/evidence.md)に版と出典を記録しています。',
 'properties': '✅ 文書上の対応 · ⚠️ 部分対応、版依存、通常の batch · ❌ 非対応 · ? 未確認。Calibration は手法や評価の記録であり普遍的な保証ではありません。Shared は計算の再利用です。Parallel Q は固有スロットとバッチ行を区別し、公式 API の挙動だけから内部実装は推定しません。',
 'timeline': '公式を先頭に置き、その後に日付を確認した**版／成果物の節目**を示します。初回公開日ではなく、モデル一覧の並び順を置き換えるものでもありません。',
 'unverified': '初回公開日未確認', 'version': '版／成果物の節目のみ',
 'official': '[TypeSafe](https://typesafe.ai/) · [公開記事](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [文書](https://docs.typesafe.ai/) · [公式 GitHub](https://github.com/typesafe-ai)。公式 skill は取得できましたが、公開記事とコンテキスト制限のページは今回再確認できませんでした。SDK にモデル重みや独自学習レシピは含まれません。',
 'models': '主要行には検査可能なローカル判断機構または専用モデルを収録し、単なる API 呼び出しは含めません。[詳細と根拠](docs/evidence.md)で対象経路を示し、任意機能と旧版を混同しません。',
 'architecture': '基盤モデル、判断の readout、実行方式を別々に記録します。Causal logits、学習済み pointer/scoring head、encoder、masked diffusion スロットがあります。**Non-AR ≠ diffusion、一度のリクエスト ≠ 一度の forward。** [構造](docs/architecture.md) · [関連モデルとの比較](docs/jev-vs-models.md)。',
 'training': '公式 RLCD は独自の詳細が未確認のベンダー用語です。コミュニティの `RLCD (claimed)` には具体的手法と根拠を付けます。CE/Brier や temperature fitting のみは **RL ではありません**。実験段階と公開 checkpoint を分け、**RLCR と RLCD が同一とは扱いません**。[学習監査](docs/training.md)。',
 'mechanism': '候補 token logits、学習済み pointer/scalar head、masked answer slots を区別します。確率は提示された候補集合に条件付けられ、形式が正しくても意味が正しいとは限りません。[仕組みの比較](docs/jev-vs-models.md)。',
 'evaluation': 'タスク性能、Calibration、risk-coverage、未見の質問／選択肢、同条件の遅延とメモリを報告します。この監査で上流 benchmark は再実行していません。[評価方法](docs/evaluation.md) · [SemIf 実験資料](https://github.com/TheoLeeCJ/SemIf/tree/master/benchmarks) · [mini-Jev 対照](https://github.com/r-ms/mini-jev)。',
 'papers': 'arXiv v1 の日付順に並べた一次研究です。Jev の実装としては数えません。',
 'tools': ['Python クライアントと API schema。モデル本体ではない。', 'JavaScript/TypeScript クライアント。モデル本体ではない。', '通常の LLM API を System One 比較インターフェースに変換する。', '質問設計と実例のガイド。ネットワーク仕様ではない。'],
 'application': '[Jevenator 2](https://github.com/mmastrac/jevenator2) は別の判断エンドポイントを呼び出して領域スキャンによる位置推定を行います。新しい基盤モデルではなく、公式 Jev の構造を証明するものでもありません。',
 'contributing': 'YAML の事実と各言語の説明を編集し、`python scripts/generate_readme.py` と `python scripts/validate.py` を実行してください。README と根拠一覧は自動生成です。[貢献規則](CONTRIBUTING.md) · [内容ライセンス](LICENSE) · [コードライセンス](LICENSE-CODE)。TypeSafe とは無関係の独立した資料です。',
 'awesome': 'Awesome Jev lists の awesome list です。既知の日付を先に並べ、Unknown を未公開とは解釈しません。月単位の日付から特定の日を推定することもありません。',
 'date': '日付', 'project': 'プロジェクト', 'event': '出来事', 'paper': '論文', 'topic': '分野', 'repository': 'リポジトリ', 'release': '初回公開日', 'languages': '言語', 'focus': '対象', 'notes': '備考', 'tool': 'ツール', 'purpose': '用途',
}}


def load_data(root: Path = ROOT):
    def read(name):
        with (root / 'data' / name).open(encoding='utf-8') as fh:
            return yaml.safe_load(fh)
    return read('projects.yaml'), read('papers.yaml')['papers'], read('awesome-lists.yaml')['lists']


def ordered(items):
    # Stable sorting intentionally keeps unknown/tied dates in existing curation order.
    return sorted(items, key=lambda p: (not p.get('official', False),
                   p.get('release_date') is None, p.get('release_date') or '9999'))


def esc(value):
    return str(value).replace('|', r'\|').replace('\n', ' ')


def table(headers, rows):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |',
                      '|' + '|'.join(['---'] * len(headers)) + '|'] +
                     ['| ' + ' | '.join(esc(v) for v in row) + ' |' for row in rows])


def landscape(projects):
    headers = ['Project', 'Release Date', 'Backbone', 'Params', 'Architecture',
               'Training', 'RL / RLCD', 'AR', 'Decision Mechanism', 'Outputs', 'Weights']
    rows = []
    for p in ordered(projects):
        w = {'Yes': '✅', 'No': '❌'}.get(p['weights'], p['weights'])
        rows.append([f"[{p['name']}]({p['github']})", p['release_date'] or 'Unknown',
            p['backbone'], p['params'], p['architecture'], p['training'], p['rl'],
            p['ar'], p['decision_mechanism'], '/'.join(OUTPUT[v] for v in p['outputs']), w])
    return table(headers, rows)


def property_table(projects):
    keys = ['typed','dynamic','variable','native','calibration','shared_state','multi_q','parallel_q','non_ar']
    return table(['Project','Typed','Dynamic Options','Variable K','Native P','Calibration',
                  'Shared State','Multi-Q','Parallel Q','Non-AR'],
        [[f"[{p['name']}]({p['github']})"] + [SYMBOL[p['properties'][k]] for k in keys]
         for p in ordered(projects)])


def render_readme(lang, data, papers, lists):
    t=TEXT[lang]; p=data['projects']; parts=['# Awesome Jev',
        '[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)',
        t['description'], f"{t['snapshot']}: **{data['checked_at']}** · 1 {t['scope'].format(community=sum(not x['official'] for x in p))}",
        '<!-- Generated by scripts/generate_readme.py. Edit data/*.yaml and localized text. -->']
    def section(n,*body):
        parts.extend(['## '+t['headings'][n],*body])
    section(0,t['intro'])
    section(1,t['dates'].format(unknown=sum(x['release_date'] is None for x in p),total=len(p)),t['legend'],'<!-- landscape:start -->\n'+landscape(p)+'\n<!-- landscape:end -->')
    section(2,t['properties'],'<!-- properties:start -->\n'+property_table(p)+'\n<!-- properties:end -->')
    events=[]
    for x in p:
        for e in x['release_evidence']:
            if e.get('date'):
                events.append((e['date'],x['name'],f"[{e['url'].rsplit('/',1)[-1]}]({e['url']}) — {t['version']}"))
    section(3,t['timeline'],table([t['date'],t['project'],t['event']],
        [('Unknown','Official Jev',t['unverified'])]+sorted(events,key=lambda e:e[0])))
    section(4,t['official'])
    section(5,t['models'])
    section(6,t['architecture'])
    section(7,t['training'])
    section(8,t['mechanism'])
    section(9,t['evaluation'])
    section(10,t['papers'],table([t['date'],t['paper'],t['topic']],
        [[x['date'],f"[{x['title']}]({x['paper']})",x['topic']] for x in papers]))
    repos=['typesafe-sdk-python','typesafe-sdk-js','system-one-adapter-python','skills']
    section(11,table([t['tool'],t['purpose']],
        [[f'[{repo}](https://github.com/typesafe-ai/{repo})',description]
         for repo,description in zip(repos,t['tools'])]))
    section(12,t['application'])
    section(13,t['contributing'])
    parts.extend(['## Awesome Awesome Jev 😄',t['awesome'],
        table([t['repository'],t['release'],t['languages'],t['focus'],t['notes']],
        [[f"[{x['name']}]({x['url']})",x['release_date'] or 'Unknown',
          ' / '.join(x['languages']),x['focus'],x['notes'][lang]] for x in ordered(lists)])])
    return '\n\n'.join(parts)+'\n'


def render_evidence(data):
    parts=['# Project evidence and version notes', '[Home](../README.md) · [Audit limitations](audit.md)',
        'Generated from `data/projects.yaml`. This index distinguishes inspected source from author documentation; links are not an endorsement. Multilingual notes are retained in the data. Dates below describe first publication, not later releases.']
    for p in ordered(data['projects']):
        parts += ['## '+p['id'],f"**[{p['name']}]({p['github']})** · First public: {p['release_date'] or 'Unknown'}",p['notes']['en'],
                  f"**RL status:** {p['rl_status']}"]
        if p['huggingface']:
            parts.append(f"**Model/artifact link:** {p['huggingface']} (project weight status: {p['weights']}; upstream links are identified in notes).")
        parts.append(table(['Source','Supports','Evidence level'],
            [[f"[Source {i+1}]({e['url']})",', '.join(e['supports']),e['level']] for i,e in enumerate(p['evidence'])]))
        if p['release_evidence']:
            parts.append(table(['Date','Artifact / limitation'],
              [[e['date'] or 'Unknown',f"[{e['kind']}]({e['url']})"] for e in p['release_evidence']]))
    return '\n\n'.join(parts)+'\n'


def outputs(root: Path = ROOT):
    data,papers,lists=load_data(root)
    return {**{path:render_readme(lang,data,papers,lists) for lang,path in LANGUAGES.items()},
            'docs/evidence.md':render_evidence(data)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Fail instead of rewriting stale generated files.')
    args=parser.parse_args()
    try:
        generated=outputs()
        stale=[]
        for path,text in generated.items():
            dest=ROOT/path
            if args.check:
                if not dest.exists() or dest.read_text(encoding='utf-8') != text:
                    stale.append(path)
            else:
                dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_text(text,encoding='utf-8')
        if stale:
            print('Stale generated files: '+', '.join(stale),file=sys.stderr)
            return 1
        print('Generated pages are synchronized.' if args.check else f'Generated {len(generated)} files.')
        return 0
    except (OSError,ValueError,KeyError,TypeError,yaml.YAMLError) as exc:
        print(f'Generation failed: {exc}',file=sys.stderr)
        return 1

if __name__=='__main__':
    raise SystemExit(main())
