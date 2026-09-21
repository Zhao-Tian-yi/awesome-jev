# Awesome Jev

> **当面は高頻度でリアルタイム更新：** Jev / System One Models の公開実装、アーキテクチャ、学習手法、評価の最新動向を集中的に追い、このリポジトリを随時更新します。

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

**Jev-like モデルの仕組み、学習方法、利用できるコードと重みを比較する。**

Jev と System One Models の研究マップ。アーキテクチャ、判断の読み出し、RLCD、Calibration を整理し、各技術ラベルの実装にリンクします。

21 件のコミュニティ実装 · 1 件の公式参照 · 6 件の関連研究 · English / 中文 / 日本語

[モデル比較](#models) · [目的から探す](#start-here) · [最近の更新](#updates) · [学習の検証](docs/training.md) · [貢献方法](#contributing)

モデル選定や学習方法の調査に戻れるよう、この比較表を Star で保存してください。

<!-- Generated from data/*.yaml. See scripts/generate_readme.py. -->

## Jev とは？

`State + 実行時に定義する質問 + 選択肢 → 型付きの確率的判断`。Noul は二値条件、Choice は候補集合、Score は順序付きレベルの分布と期待値を扱います。公式 API と独立実装を区別します。**Non-AR は diffusion と同義ではなく、確率の直接出力も Calibration を保証しません。**

<a id="models"></a>

## モデル一覧

公式 Jev を先頭に固定し、確認済みの初回公開日を昇順、未確認項目を既存の収録順に並べます。Stars 順ではありません。

<!-- landscape:start -->
| Project | GitHub Stars | First Public | Backbone / Size | Decision Architecture | Training / RL | Artifacts | Evidence |
|---|---:|---|---|---|---|---|---|
| [Official Jev](https://github.com/typesafe-ai) | — | Unknown | Not disclosed<br>Not disclosed | Custom / Not Disclosed<br>Not disclosed | Not disclosed<br>RL: RLCD | [API only](https://typesafe.ai/) | [Sources](docs/evidence.md#official-jev) |
| [SemIf](https://github.com/TheoLeeCJ/SemIf) | [2,870](https://github.com/TheoLeeCJ/SemIf/stargazers) | Unknown | Qwen3.5 / MiniCPM5 / Qwen3<br>0.6B / 2B / 4B | AR LLM<br>Next-token logits | None<br>RL: No | [Upstream model / setup](https://github.com/TheoLeeCJ/SemIf) | [Sources](docs/evidence.md#semif) |
| [OpenJev / DiffusionGemma](https://github.com/razorback16/openjev) | [260](https://github.com/razorback16/openjev/stargazers) | Unknown | DiffusionGemma 26B-A4B<br>26B total / approximately 4B active | Diffusion / Masked<br>Masked decision slots | None<br>RL: No | [Upstream weights](https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4) | [Sources](docs/evidence.md#openjev-diffusiongemma) |
| [Kev](https://github.com/jaredpalmer/kev) | [1,803](https://github.com/jaredpalmer/kev/stargazers) | Unknown | Qwen3.5; earlier Qwen3<br>0.8B / 4B / 9B | AR LLM + Pointer Head<br>Pointer head | LoRA + Decision Head<br>RL: No | [Adapter/head](https://huggingface.co/jaredpalmer/kev-4b) | [Sources](docs/evidence.md#kev) |
| [NanoJev](https://github.com/TianyuCodings/NanoJev) | [1,714](https://github.com/TianyuCodings/NanoJev/stargazers) | Unknown | Qwen3-0.6B<br>0.6B + heads | AR LLM + Decision Head<br>Option-wise scoring | SFT; RL prototype<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/C-Tianyu/NanoJev) | [Sources](docs/evidence.md#nanojev) |
| [jevlike](https://github.com/vinnylarouge/jevlike) | [1,149](https://github.com/vinnylarouge/jevlike/stargazers) | Unknown | Custom / frozen HF encoder<br>Configuration-dependent | Option Scorer<br>Option-wise scoring | Head-only / from scratch<br>RL: No | Adapter/head; see evidence | [Sources](docs/evidence.md#jevlike) |
| [Laya](https://github.com/NandhaKishorM/laya) | [7,916](https://github.com/NandhaKishorM/laya/stargazers) | Unknown | ModernBERT / mmBERT<br>421M / 322M (author-reported) | Encoder-based<br>Option-marker head | Full FT + RL<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/convaiinnovations/laya) | [Sources](docs/evidence.md#laya) |
| [Von](https://github.com/wfzyx/von) | [316](https://github.com/wfzyx/von/stargazers) | Unknown | ModernBERT variants<br>395M (OptionMarker; author-reported) | Encoder-based / Cross-Encoder<br>Option-marker / NLI | Calibration Training<br>RL: No | [Adapter/head](https://huggingface.co/wfzyx/von-1.0) | [Sources](docs/evidence.md#von) |
| [decider](https://github.com/Mapika/decider) | [260](https://github.com/Mapika/decider/stargazers) | Unknown | Qwen3.5 family<br>0.8B / 2B / 34.7B total, 3B active | Hybrid + Decision Head<br>Label-token projection | Multi-stage<br>RL: RLCR-like | [Project weights](https://huggingface.co/Mapika/decider-2b) | [Sources](docs/evidence.md#decider) |
| [mini-Jev](https://github.com/r-ms/mini-jev) | [40](https://github.com/r-ms/mini-jev/stargazers) | Unknown | Qwen3-4B-Instruct-2507<br>4B | AR LLM<br>Next-token logits / Verbalizer | None<br>RL: No | [Upstream model / setup](https://github.com/r-ms/mini-jev) | [Sources](docs/evidence.md#mini-jev) |
| [LitJev](https://github.com/zhengxuyu/litjev) | [35](https://github.com/zhengxuyu/litjev/stargazers) | Unknown | Qwen family<br>27B default; configurable | AR LLM<br>Next-token logits | None<br>RL: No | [Upstream model / setup](https://github.com/zhengxuyu/litjev) | [Sources](docs/evidence.md#litjev) |
| [Open JEV (zhihz)](https://github.com/zhihz/openjev) | [26](https://github.com/zhihz/openjev/stargazers) | Unknown | Qwen3-4B-Instruct-2507<br>4B | AR LLM<br>Next-token logits / Verbalizer | None<br>RL: No | [Upstream model / setup](https://github.com/zhihz/openjev) | [Sources](docs/evidence.md#zhihz-openjev) |
| [open-jev (daseinlabs)](https://github.com/daseinlabs/open-jev) | [84](https://github.com/daseinlabs/open-jev/stargazers) | Unknown | Gemma 3 4B<br>4B + optional head | AR LLM / Option Scorer<br>Option likelihood / head | None / Head-only<br>RL: No | No project-weight release | [Sources](docs/evidence.md#dasein-openjev) |
| [reflex](https://github.com/kshetrajna12/reflex) | [94](https://github.com/kshetrajna12/reflex/stargazers) | Unknown | Qwen3.5-4B (stable)<br>4B default | AR LLM<br>Next-token logits | None<br>RL: No | [Upstream model / setup](https://github.com/kshetrajna12/reflex) | [Sources](docs/evidence.md#reflex) |
| [Verdict / OpenJev](https://github.com/Heman10x-NGU/Verdict-open-jev) | [59](https://github.com/Heman10x-NGU/Verdict-open-jev/stargazers) | Unknown | ModernBERT-base + GLiClass<br>151M (author-reported) | Encoder-based<br>Joint label / context scoring head | Calibration Training<br>RL: No | [Project weights](https://huggingface.co/heman10x/rlcd-modernbert-151m) | [Sources](docs/evidence.md#verdict) |
| [eve-rlcd](https://github.com/anthony-maio/eve-rlcd) | [4](https://github.com/anthony-maio/eve-rlcd/stargazers) | Unknown | Qwen3-0.6B-Base<br>0.6B | AR LLM<br>Next-token logits / Verbalizer | SFT + RL<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/anthonym21/qwen3-0.6b-rlcd-decision) | [Sources](docs/evidence.md#eve-rlcd) |
| [minojev](https://github.com/zeredy879/minojev) | [25](https://github.com/zeredy879/minojev/stargazers) | Unknown | Qwen3-1.7B<br>1.7B + approximately 0.8M head | AR LLM + Decision Head<br>Option-wise scoring | Head-only<br>RL: No | [Adapter/head](https://huggingface.co/zeredy879/minojev) | [Sources](docs/evidence.md#minojev) |
| [Luce](https://github.com/scienthoon/luce) | [7](https://github.com/scienthoon/luce/stargazers) | Unknown | Qwen3 / Qwen2.5<br>4B default | AR LLM + Decision Head<br>Decision Head / Verbalizer | Distillation + LoRA + Head<br>RL: No | Availability unverified | [Sources](docs/evidence.md#luce) |
| [poorjev](https://github.com/rupeshpoojary9/poorjev) | [4](https://github.com/rupeshpoojary9/poorjev/stargazers) | Unknown | Zero-shot NLI encoders<br>Configuration-dependent | Cross-Encoder<br>NLI option-wise scoring | Calibration Training<br>RL: No | No project-weight release | [Sources](docs/evidence.md#poorjev) |
| [jevbetter](https://github.com/olanotolu/jevbetter) | [14](https://github.com/olanotolu/jevbetter/stargazers) | Unknown | Custom / frozen HF encoder<br>Configuration-dependent | Option Scorer<br>Option-wise scoring | SFT / Head-only<br>RL: No | Availability unverified | [Sources](docs/evidence.md#jevbetter) |
| [JevForge](https://github.com/zwliJay/jev-forge) | [8](https://github.com/zwliJay/jev-forge/stargazers) | Unknown | Qwen3.5-0.8B / Qwen3-0.6B<br>0.8B + scorer | AR LLM + Decision Head<br>Option-wise scoring | SFT; RL prototype<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/AndeyTait/JevForge-0.8B) | [Sources](docs/evidence.md#jevforge) |
| [System One Open](https://github.com/mithalouni/system-one-open) | [24](https://github.com/mithalouni/system-one-open/stargazers) | Unknown | Gemma 4 E2B / Gemma 3 270M<br>E2B (vendor label) / 270M | AR LLM + Decision Head<br>Label-token slots | LoRA / SFT<br>RL: No | No project-weight release | [Sources](docs/evidence.md#system-one-open) |
<!-- landscape:end -->

[詳細比較表](docs/comparison.md) · [根拠と版の注記](docs/evidence.md) · [検証の制約](docs/audit.md)

<details>
<summary>列の定義、日付の確認状況、詳細比較を開く</summary>

**初回公開日は 22 件中 22 件が未確認です。** 作成日や後続リリース日で代用しません。詳細表の **AR Decoding** は回答の逐次生成を指し、事前学習方式ではありません。**Artifacts** はプロジェクト固有の重み、adapter/head、上流モデルの利用を区別します。RL の記述は対象の版に限定し、コミュニティの RLCD を公式手法と同一視しません。

技術情報の検証時点：2026-09-21。

Stars の取得時点：2026-09-21T13:48:47Z。注目度の参考値であり、品質評価ではありません。[API 出典](data/github-stars.json)。Stars の更新は技術情報の再検証を意味しません。

</details>

<details>
<summary>Jev-like 機能比較を開く</summary>

✅ 文書上の対応 · ⚠️ 部分的、特定の版または通常の batch · ❌ 非対応 · ? 未確認。Shared State は計算の再利用を指し、Parallel Q は native slots と batch を区別します。Calibration は手順や根拠の記録であり、一般的保証ではありません。

<!-- properties:start -->
| Project | Typed | Dynamic Options | Variable K | Native P | Calibration | Shared State | Multi-Q | Parallel Q | Non-AR |
|---|---|---|---|---|---|---|---|---|---|
| [Official Jev](https://github.com/typesafe-ai) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ? | ✅ | ⚠️ | ✅ |
| [SemIf](https://github.com/TheoLeeCJ/SemIf) | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ⚠️ | ✅ |
| [OpenJev / DiffusionGemma](https://github.com/razorback16/openjev) | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ | ✅ | ✅ | ✅ |
| [Kev](https://github.com/jaredpalmer/kev) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ✅ |
| [NanoJev](https://github.com/TianyuCodings/NanoJev) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ? | ✅ | ⚠️ | ✅ |
| [jevlike](https://github.com/vinnylarouge/jevlike) | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ | ? | ? | ✅ |
| [Laya](https://github.com/NandhaKishorM/laya) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ? | ✅ | ⚠️ | ✅ |
| [Von](https://github.com/wfzyx/von) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ? | ✅ | ? | ✅ |
| [decider](https://github.com/Mapika/decider) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ✅ |
| [mini-Jev](https://github.com/r-ms/mini-jev) | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ? | ✅ |
| [LitJev](https://github.com/zhengxuyu/litjev) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ? | ✅ | ? | ✅ |
| [Open JEV (zhihz)](https://github.com/zhihz/openjev) | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| [open-jev (daseinlabs)](https://github.com/daseinlabs/open-jev) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ❌ | ✅ |
| [reflex](https://github.com/kshetrajna12/reflex) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ✅ |
| [Verdict / OpenJev](https://github.com/Heman10x-NGU/Verdict-open-jev) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ? | ✅ | ? | ✅ |
| [eve-rlcd](https://github.com/anthony-maio/eve-rlcd) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ✅ |
| [minojev](https://github.com/zeredy879/minojev) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ? | ✅ | ⚠️ | ✅ |
| [Luce](https://github.com/scienthoon/luce) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ? | ✅ | ? | ✅ |
| [poorjev](https://github.com/rupeshpoojary9/poorjev) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ? | ✅ | ⚠️ | ✅ |
| [jevbetter](https://github.com/olanotolu/jevbetter) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ? | ? | ✅ |
| [JevForge](https://github.com/zwliJay/jev-forge) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ✅ | ⚠️ | ✅ |
| [System One Open](https://github.com/mithalouni/system-one-open) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ |
<!-- properties:end -->

</details>

<a id="start-here"></a>

## 目的から探す

性能ランキングではなく、読む順序の案内です。利用前に版と根拠を確認してください。

| 目的 | 出発点 | 確認する点 |
|---|---|---|
| 追加学習なしで判断を試す | [SemIf](docs/evidence.md#semif) · [mini-Jev](docs/evidence.md#mini-jev) | [候補 logits と共有 prefix](docs/comparison.md) |
| 判断機構を学習する | [Kev](docs/evidence.md#kev) · [NanoJev](docs/evidence.md#nanojev) · [Luce](docs/evidence.md#luce) | [Decision Head、データ形式、学習経路](docs/training.md) |
| Encoder 系の判断を調べる | [Laya](docs/evidence.md#laya) · [Von](docs/evidence.md#von) | [双方向 encoding と動的候補](docs/architecture.md) |
| Diffusion の回答スロットを調べる | [OpenJev / DiffusionGemma](docs/evidence.md#openjev-diffusiongemma) | [Masked slots、denoising 回数、質問の独立性](docs/architecture.md) |
| 確率校正を考慮した RL を調べる | [eve-rlcd](docs/evidence.md#eve-rlcd) · [Laya](docs/evidence.md#laya) · [NanoJev](docs/evidence.md#nanojev) | [Sampling、reward、gradient、checkpoint の範囲](docs/training.md) |

<a id="updates"></a>

## 最近の更新

このリストの変更日であり、上流の公開日ではありません。Stars の更新だけは含めません。[全履歴](docs/updates.md)。

| 日付 | 種類 | 変更 | 根拠 |
|---|---|---|---|
| 2026-09-21 | Updated | モデル表を8列に整理し、目的別の案内、成果物リンク、簡易投稿フォームを追加。検証済みの全項目は維持。 | [Source](docs/comparison.md) |
| 2026-09-21 | Added | GitHub Stars の数値スナップショットと三言語の更新案内を追加。時系列の収録順は変更せず。 | [Source](https://github.com/Zhao-Tian-yi/awesome-jev/commit/fccf8a0ecd6c8d393acd2e734d6572f0c6d1e82c) |
| 2026-09-21 | Corrected | 共通 YAML から研究マップを再構築。判断の生成方式、backbone、コミュニティ RL の根拠を区別し、版ごとの制約を明記。 | [Source](https://github.com/Zhao-Tian-yi/awesome-jev/commit/5b64c6751e5b11597dde04ed73dafe47ba597c0f) |

## 研究ガイド

| 問い | 資料 |
|---|---|
| 確率はどのように得られるか？ | [architecture.md](docs/architecture.md) |
| 各実装で RLCD は何を意味するか？ | [training.md](docs/training.md) |
| LLM、reranker、diffusion とどう違うか？ | [jev-vs-models.md](docs/jev-vs-models.md) |
| 能力、Calibration、効率をどう公平に比較するか？ | [evaluation.md](docs/evaluation.md) |

学習機構と測定結果を分けます。API の振る舞いから内部構造を推定したり、異なる条件の数値をランキングにまとめたりしません。

<details>
<summary>確認済みの版／成果物の節目を開く</summary>

版の節目は初回公開日ではありません。公式 Jev を先頭にし、日付がある節目を昇順に並べます。

| Date | Project | Milestone |
|---|---|---|
| Unknown | Official Jev | Official reference |
| 2026-09-18 | eve-rlcd | [Version/artifact](https://github.com/anthony-maio/eve-rlcd/releases/tag/data-v1) |
| 2026-09-19 | Laya | [Version/artifact](https://github.com/NandhaKishorM/laya/releases/tag/v0.2.0) |
| 2026-09-20 | Kev | [Version/artifact](https://github.com/jaredpalmer/kev/releases/tag/kev-family) |

</details>

## 関連研究

arXiv v1 の日付順の一次研究です。関連手法をそのまま Jev 実装として扱いません。

| Date | Paper | Topic |
|---|---|---|
| 2017-06-14 | [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) | Calibration |
| 2018-10-11 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | Encoder / Masked LM |
| 2024-06-11 | [Simple and Effective Masked Diffusion Language Models](https://arxiv.org/abs/2406.07524) | Masked Diffusion |
| 2025-02-14 | [Large Language Diffusion Models](https://arxiv.org/abs/2502.09992) | Diffusion LM |
| 2025-07-22 | [Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty](https://arxiv.org/abs/2507.16806) | RLCR |
| 2025-08-11 | [GLiClass: Generalist Lightweight Model for Sequence Classification Tasks](https://arxiv.org/abs/2508.07662) | Runtime label classification |

## 公式リソースとツール

[TypeSafe](https://typesafe.ai/) · [発表記事](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [公式文書](https://docs.typesafe.ai/) · [公式 GitHub](https://github.com/typesafe-ai)。SDK のコードは Jev のモデルコードではありません。確認範囲は[検証記録](docs/audit.md)に残します。

| Tool | Purpose |
|---|---|
| [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) | Python クライアントと API schema |
| [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) | JavaScript/TypeScript クライアント |
| [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) | 通常の LLM API を System One の比較インターフェースに変換 |
| [skills](https://github.com/typesafe-ai/skills) | 質問設計のガイドと例。ネットワーク仕様ではない |

応用例：[Jevenator 2](https://github.com/mmastrac/jevenator2) は別の判断 endpoint で領域走査を行います。新しい backbone や公式 Jev の構造を示す証拠ではありません。

<a id="contributing"></a>

## 貢献方法

新しい実装や誤りを見つけたら、リンク、短い説明、根拠を送ってください。**Issue の投稿には YAML 編集や三言語への翻訳は不要です。** 収録前にメンテナーが事実と翻訳を確認します。

[実装を推薦](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=suggest-project.yml) · [項目を訂正](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml)

PR では YAML の事実を編集し、ページを再生成します。[貢献ガイド](CONTRIBUTING.md) · [コンテンツのライセンス](LICENSE) · [コードのライセンス](LICENSE-CODE)。TypeSafe AI とは無関係の独立リソースです。

## Awesome Awesome Jev 😄

Awesome Jev リストを集める awesome list。確認済みの初回公開日を優先し、Unknown は未公開を意味しません。

| Repository | GitHub Stars | First Public | Languages | Focus | Notes |
|---|---:|---|---|---|---|
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | [141](https://github.com/OmniJev/awesome-jev-gallery/stargazers) | 2026-09 | English | Research / Ecosystem | 論文、オープンモデル、評価、エコシステム資料。改名後の正規 URL。 |
| [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev) | [1](https://github.com/Zhao-Tian-yi/awesome-jev/stargazers) | 2026-09-21 | English / 简体中文 / 日本語 | Research | はい、このリポジトリも awesome Jev リストの awesome list に入りました。 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | [853](https://github.com/yibie/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | 応用領域別の一覧。掲載と品質の保証を明確に区別する。 |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | [205](https://github.com/AnotiaWang/awesome-jev/stargazers) | Unknown | English / 简体中文 | Ecosystem | アプリケーション、ライブラリ、ツール、研究の二言語一覧。 |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | [115](https://github.com/hellogumbo/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | 検索可能な付属サイトを持つアプリケーションと統合の一覧。 |
