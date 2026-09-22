# Awesome Jev

> **当面は高頻度でリアルタイム更新：** Jev / System One Models の公開実装、アーキテクチャ、学習手法、評価の最新動向を集中的に追い、このリポジトリを随時更新します。

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Jev と System One Models の研究マップ。公開実装、アーキテクチャ、学習方法、利用できるコードと重みを整理します。

[モデル一覧](#models) · [目的から探す](#start-here) · [公式リソースとツール](#official) · [Awesome Awesome Jev 😄](#awesome-awesome-jev)

<!-- Generated from data/*.yaml. See scripts/generate_readme.py. -->

<a id="models"></a>

## モデル一覧

公式 Jev を先頭に固定し、確認済みの初回公開日を昇順、未確認項目を既存の収録順に並べます。Stars 順ではありません。

<!-- landscape:start -->
| Project | GitHub Stars | First Public | Backbone / Size | Decision Architecture | Training / RL | Artifacts | Evidence |
|---|---:|---|---|---|---|---|---|
| [Official Jev](https://github.com/typesafe-ai) | — | Unknown | Not disclosed<br>Not disclosed | Custom / Not Disclosed<br>Not disclosed | Not disclosed<br>RL: RLCD | [API only](https://typesafe.ai/) | [Sources](docs/evidence.md#official-jev) |
| [SemIf](https://github.com/TheoLeeCJ/SemIf) | [3,341](https://github.com/TheoLeeCJ/SemIf/stargazers) | Unknown | Qwen3.5 / MiniCPM5 / Qwen3<br>0.6B / 2B / 4B | AR LLM<br>Next-token logits | None<br>RL: No | [Upstream model / setup](https://github.com/TheoLeeCJ/SemIf) | [Sources](docs/evidence.md#semif) |
| [OpenJev / DiffusionGemma](https://github.com/razorback16/openjev) | [285](https://github.com/razorback16/openjev/stargazers) | Unknown | DiffusionGemma 26B-A4B<br>26B total / approximately 4B active | Diffusion / Masked<br>Masked decision slots | None<br>RL: No | [Upstream weights](https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4) | [Sources](docs/evidence.md#openjev-diffusiongemma) |
| [Kev](https://github.com/jaredpalmer/kev) | [2,606](https://github.com/jaredpalmer/kev/stargazers) | Unknown | Qwen3.5; earlier Qwen3<br>0.8B / 4B / 9B | AR LLM + Pointer Head<br>Pointer head | LoRA + Decision Head<br>RL: No | [Adapter/head](https://huggingface.co/jaredpalmer/kev-4b) | [Sources](docs/evidence.md#kev) |
| [NanoJev](https://github.com/TianyuCodings/NanoJev) | [1,851](https://github.com/TianyuCodings/NanoJev/stargazers) | Unknown | Qwen3-0.6B<br>0.6B + heads | AR LLM + Decision Head<br>Option-wise scoring | SFT; RL prototype<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/C-Tianyu/NanoJev) | [Sources](docs/evidence.md#nanojev) |
| [jevlike](https://github.com/vinnylarouge/jevlike) | [1,170](https://github.com/vinnylarouge/jevlike/stargazers) | Unknown | Custom / frozen HF encoder<br>Configuration-dependent | Option Scorer<br>Option-wise scoring | Head-only / from scratch<br>RL: No | Adapter/head; see evidence | [Sources](docs/evidence.md#jevlike) |
| [Laya](https://github.com/NandhaKishorM/laya) | [11,383](https://github.com/NandhaKishorM/laya/stargazers) | Unknown | ModernBERT / mmBERT<br>421M / 322M (author-reported) | Encoder-based<br>Option-marker head | Full FT + RL<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/convaiinnovations/laya) | [Sources](docs/evidence.md#laya) |
| [Von](https://github.com/wfzyx/von) | [371](https://github.com/wfzyx/von/stargazers) | Unknown | ModernBERT variants<br>395M (OptionMarker; author-reported) | Encoder-based / Cross-Encoder<br>Option-marker / NLI | Calibration Training<br>RL: No | [Adapter/head](https://huggingface.co/wfzyx/von-1.0) | [Sources](docs/evidence.md#von) |
| [decider](https://github.com/Mapika/decider) | [277](https://github.com/Mapika/decider/stargazers) | Unknown | Qwen3.5 family<br>0.8B / 2B / 34.7B total, 3B active | Hybrid + Decision Head<br>Label-token projection | Multi-stage<br>RL: RLCR-like | [Project weights](https://huggingface.co/Mapika/decider-2b) | [Sources](docs/evidence.md#decider) |
| [mini-Jev](https://github.com/r-ms/mini-jev) | [41](https://github.com/r-ms/mini-jev/stargazers) | Unknown | Qwen3-4B-Instruct-2507<br>4B | AR LLM<br>Next-token logits / Verbalizer | None<br>RL: No | [Upstream model / setup](https://github.com/r-ms/mini-jev) | [Sources](docs/evidence.md#mini-jev) |
| [LitJev](https://github.com/zhengxuyu/litjev) | [37](https://github.com/zhengxuyu/litjev/stargazers) | Unknown | Qwen family<br>27B default; configurable | AR LLM<br>Next-token logits | None<br>RL: No | [Upstream model / setup](https://github.com/zhengxuyu/litjev) | [Sources](docs/evidence.md#litjev) |
| [Open JEV (zhihz)](https://github.com/zhihz/openjev) | [28](https://github.com/zhihz/openjev/stargazers) | Unknown | Qwen3-4B-Instruct-2507<br>4B | AR LLM<br>Next-token logits / Verbalizer | None<br>RL: No | [Upstream model / setup](https://github.com/zhihz/openjev) | [Sources](docs/evidence.md#zhihz-openjev) |
| [open-jev (daseinlabs)](https://github.com/daseinlabs/open-jev) | [91](https://github.com/daseinlabs/open-jev/stargazers) | Unknown | Gemma 3 4B<br>4B + optional head | AR LLM / Option Scorer<br>Option likelihood / head | None / Head-only<br>RL: No | No project-weight release | [Sources](docs/evidence.md#dasein-openjev) |
| [reflex](https://github.com/kshetrajna12/reflex) | [109](https://github.com/kshetrajna12/reflex/stargazers) | Unknown | Qwen3.5-4B (stable)<br>4B default | AR LLM<br>Next-token logits | None<br>RL: No | [Upstream model / setup](https://github.com/kshetrajna12/reflex) | [Sources](docs/evidence.md#reflex) |
| [Verdict / OpenJev](https://github.com/Heman10x-NGU/Verdict-open-jev) | [67](https://github.com/Heman10x-NGU/Verdict-open-jev/stargazers) | Unknown | ModernBERT-base + GLiClass<br>151M (author-reported) | Encoder-based<br>Joint label / context scoring head | Calibration Training<br>RL: No | [Project weights](https://huggingface.co/heman10x/rlcd-modernbert-151m) | [Sources](docs/evidence.md#verdict) |
| [eve-rlcd](https://github.com/anthony-maio/eve-rlcd) | [4](https://github.com/anthony-maio/eve-rlcd/stargazers) | Unknown | Qwen3-0.6B-Base<br>0.6B | AR LLM<br>Next-token logits / Verbalizer | SFT + RL<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/anthonym21/qwen3-0.6b-rlcd-decision) | [Sources](docs/evidence.md#eve-rlcd) |
| [minojev](https://github.com/zeredy879/minojev) | [25](https://github.com/zeredy879/minojev/stargazers) | Unknown | Qwen3-1.7B<br>1.7B + approximately 0.8M head | AR LLM + Decision Head<br>Option-wise scoring | Head-only<br>RL: No | [Adapter/head](https://huggingface.co/zeredy879/minojev) | [Sources](docs/evidence.md#minojev) |
| [Luce](https://github.com/scienthoon/luce) | [7](https://github.com/scienthoon/luce/stargazers) | Unknown | Qwen3 / Qwen2.5<br>4B default | AR LLM + Decision Head<br>Decision Head / Verbalizer | Distillation + LoRA + Head<br>RL: No | Availability unverified | [Sources](docs/evidence.md#luce) |
| [poorjev](https://github.com/rupeshpoojary9/poorjev) | [5](https://github.com/rupeshpoojary9/poorjev/stargazers) | Unknown | Zero-shot NLI encoders<br>Configuration-dependent | Cross-Encoder<br>NLI option-wise scoring | Calibration Training<br>RL: No | No project-weight release | [Sources](docs/evidence.md#poorjev) |
| [jevbetter](https://github.com/olanotolu/jevbetter) | [14](https://github.com/olanotolu/jevbetter/stargazers) | Unknown | Custom / frozen HF encoder<br>Configuration-dependent | Option Scorer<br>Option-wise scoring | SFT / Head-only<br>RL: No | Availability unverified | [Sources](docs/evidence.md#jevbetter) |
| [JevForge](https://github.com/zwliJay/jev-forge) | [11](https://github.com/zwliJay/jev-forge/stargazers) | Unknown | Qwen3.5-0.8B / Qwen3-0.6B<br>0.8B + scorer | AR LLM + Decision Head<br>Option-wise scoring | SFT; RL prototype<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/AndeyTait/JevForge-0.8B) | [Sources](docs/evidence.md#jevforge) |
| [System One Open](https://github.com/mithalouni/system-one-open) | [28](https://github.com/mithalouni/system-one-open/stargazers) | Unknown | Gemma 4 E2B / Gemma 3 270M<br>E2B (vendor label) / 270M | AR LLM + Decision Head<br>Label-token slots | LoRA / SFT<br>RL: No | No project-weight release | [Sources](docs/evidence.md#system-one-open) |
<!-- landscape:end -->

技術検証：**2026-09-21** · Stars 取得：**2026-09-22T03:56:16Z**（[API 出典](data/github-stars.json)）。Unknown は初回公開日の未確認を示します。Stars は技術品質の指標ではありません。

[技術比較の全項目](docs/comparison.md) · [根拠とバージョン情報](docs/evidence.md) · [検証上の制約](docs/audit.md)

<a id="start-here"></a>

## 目的から探す

ランキングではなく、読み始めるための案内です。利用前にリンク先の版と根拠を確認してください。

| 目的 | 入口 | 確認する点 |
|---|---|---|
| 学習せずに判断を試す | [SemIf](docs/evidence.md#semif) · [mini-Jev](docs/evidence.md#mini-jev) | [候補 logits と共有 prefix](docs/comparison.md) |
| 判断機構を学習する | [Kev](docs/evidence.md#kev) · [NanoJev](docs/evidence.md#nanojev) · [Luce](docs/evidence.md#luce) | [Decision Head、データ形式、学習経路](docs/training.md) |
| encoder による判断を調べる | [Laya](docs/evidence.md#laya) · [Von](docs/evidence.md#von) | [双方向 encoding と動的な候補](docs/architecture.md) |
| diffusion の回答スロットを調べる | [OpenJev / DiffusionGemma](docs/evidence.md#openjev-diffusiongemma) | [Masked slots、denoising の回数、質問の独立性](docs/architecture.md) |
| 校正を考慮した RL を調べる | [eve-rlcd](docs/evidence.md#eve-rlcd) · [Laya](docs/evidence.md#laya) · [NanoJev](docs/evidence.md#nanojev) | [sampling、reward、gradient、checkpoint の範囲](docs/training.md) |

<a id="official"></a>

## 公式リソースとツール

[TypeSafe](https://typesafe.ai/) · [発表記事](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [公式文書](https://docs.typesafe.ai/) · [公式 GitHub](https://github.com/typesafe-ai)。SDK のコードは Jev のモデルコードではありません。確認範囲は[検証記録](docs/audit.md)に残します。

| Tool | Purpose |
|---|---|
| [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) | Python クライアントと API schema |
| [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) | JavaScript/TypeScript クライアント |
| [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) | 通常の LLM API を System One の比較インターフェースに変換 |
| [skills](https://github.com/typesafe-ai/skills) | 質問設計のガイドと例。ネットワーク仕様ではない |

<a id="awesome-awesome-jev"></a>

## Awesome Awesome Jev 😄

Awesome Jev リストを集める awesome list。確認済みの初回公開日を優先し、Unknown は未公開を意味しません。

| Repository | GitHub Stars | First Public | Languages | Focus | Notes |
|---|---:|---|---|---|---|
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | [155](https://github.com/OmniJev/awesome-jev-gallery/stargazers) | 2026-09 | English | Research / Ecosystem | 論文、オープンモデル、評価、エコシステム資料。改名後の正規 URL。 |
| [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev) | [1](https://github.com/Zhao-Tian-yi/awesome-jev/stargazers) | 2026-09-21 | English / 简体中文 / 日本語 | Research | はい、このリポジトリも awesome Jev リストの awesome list に入りました。 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | [1,027](https://github.com/yibie/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | 応用領域別の一覧。掲載と品質の保証を明確に区別する。 |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | [257](https://github.com/AnotiaWang/awesome-jev/stargazers) | Unknown | English / 简体中文 | Ecosystem | アプリケーション、ライブラリ、ツール、研究の二言語一覧。 |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | [127](https://github.com/hellogumbo/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | 検索可能な付属サイトを持つアプリケーションと統合の一覧。 |
