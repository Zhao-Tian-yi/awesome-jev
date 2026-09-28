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
| [SemIf](https://github.com/TheoLeeCJ/SemIf) | [4,461](https://github.com/TheoLeeCJ/SemIf/stargazers) | Unknown | Qwen3.5 / MiniCPM5 / Qwen3<br>0.6B / 2B / 4B | AR LLM<br>Next-token logits | None<br>RL: No | [Upstream model / setup](https://github.com/TheoLeeCJ/SemIf) | [Sources](docs/evidence.md#semif) |
| [OpenJev / DiffusionGemma](https://github.com/razorback16/openjev) | [466](https://github.com/razorback16/openjev/stargazers) | Unknown | DiffusionGemma 26B-A4B<br>26B total / approximately 4B active<br>Input: Text + image | Diffusion / Masked<br>Masked decision slots | None<br>RL: No | [Upstream weights](https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4) | [Sources](docs/evidence.md#openjev-diffusiongemma) |
| [Kev](https://github.com/jaredpalmer/kev) | [7,457](https://github.com/jaredpalmer/kev/stargazers) | Unknown | Qwen3.5; earlier Qwen3<br>0.8B / 4B / 9B | AR LLM + Pointer Head<br>Pointer head | LoRA + Decision Head<br>RL: No | [Adapter/head](https://huggingface.co/jaredpalmer/kev-4b) | [Sources](docs/evidence.md#kev) |
| [NanoJev](https://github.com/TianyuCodings/NanoJev) | [2,361](https://github.com/TianyuCodings/NanoJev/stargazers) | Unknown | Qwen3-0.6B<br>0.6B + heads | AR LLM + Decision Head<br>Option-wise scoring | SFT; RL prototype<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/C-Tianyu/NanoJev) | [Sources](docs/evidence.md#nanojev) |
| [jevlike](https://github.com/vinnylarouge/jevlike) | [1,321](https://github.com/vinnylarouge/jevlike/stargazers) | Unknown | Custom / frozen HF encoder<br>Configuration-dependent | Option Scorer<br>Option-wise scoring | Head-only / from scratch<br>RL: No | Adapter/head; see evidence | [Sources](docs/evidence.md#jevlike) |
| [Laya](https://github.com/NandhaKishorM/laya) | [26,876](https://github.com/NandhaKishorM/laya/stargazers) | Unknown | ModernBERT / mmBERT<br>421M / 322M (author-reported) | Encoder-based<br>Option-marker head | Full FT + RL<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/convaiinnovations/laya) | [Sources](docs/evidence.md#laya) |
| [Von](https://github.com/wfzyx/von) | [730](https://github.com/wfzyx/von/stargazers) | Unknown | ModernBERT variants<br>395M (OptionMarker; author-reported) | Encoder-based / Cross-Encoder<br>Option-marker / NLI | Calibration Training<br>RL: No | [Adapter/head](https://huggingface.co/wfzyx/von-1.0) | [Sources](docs/evidence.md#von) |
| [decider](https://github.com/Mapika/decider) | [864](https://github.com/Mapika/decider/stargazers) | Unknown | Qwen3.5 family<br>0.8B / 2B / 4B / 34.7B total, 3B active (MoE)<br>Input: Text; optional native-image variant | Hybrid + Decision Head<br>Label-token projection | Multi-stage<br>RL: RLCR-like | [Project weights](https://huggingface.co/Mapika/decider-2b) | [Sources](docs/evidence.md#decider) |
| [mini-Jev](https://github.com/r-ms/mini-jev) | [57](https://github.com/r-ms/mini-jev/stargazers) | Unknown | Qwen3-4B-Instruct-2507<br>4B | AR LLM<br>Next-token logits / Verbalizer | None<br>RL: No | [Upstream model / setup](https://github.com/r-ms/mini-jev) | [Sources](docs/evidence.md#mini-jev) |
| [LitJev](https://github.com/zhengxuyu/litjev) | [45](https://github.com/zhengxuyu/litjev/stargazers) | Unknown | Qwen family<br>27B default; configurable<br>Input: Text + image (checkpoint-dependent) | AR LLM<br>Next-token logits | None<br>RL: No | [Upstream model / setup](https://github.com/zhengxuyu/litjev) | [Sources](docs/evidence.md#litjev) |
| [Open JEV (zhihz)](https://github.com/zhihz/openjev) | [35](https://github.com/zhihz/openjev/stargazers) | Unknown | Qwen3-4B-Instruct-2507<br>4B | AR LLM<br>Next-token logits / Verbalizer | None<br>RL: No | [Upstream model / setup](https://github.com/zhihz/openjev) | [Sources](docs/evidence.md#zhihz-openjev) |
| [open-jev (daseinlabs)](https://github.com/daseinlabs/open-jev) | [116](https://github.com/daseinlabs/open-jev/stargazers) | Unknown | Gemma 3 4B<br>4B + optional head | AR LLM / Option Scorer<br>Option likelihood / head | None / Head-only<br>RL: No | No project-weight release | [Sources](docs/evidence.md#dasein-openjev) |
| [reflex](https://github.com/kshetrajna12/reflex) | [153](https://github.com/kshetrajna12/reflex/stargazers) | Unknown | Qwen3.5-4B (stable)<br>4B default<br>Input: Text + image | AR LLM<br>Next-token logits | None<br>RL: No | [Upstream model / setup](https://github.com/kshetrajna12/reflex) | [Sources](docs/evidence.md#reflex) |
| [Verdict / OpenJev](https://github.com/Heman10x-NGU/Verdict-open-jev) | [107](https://github.com/Heman10x-NGU/Verdict-open-jev/stargazers) | Unknown | ModernBERT-base + GLiClass<br>151M (author-reported) | Encoder-based<br>Joint label / context scoring head | Calibration Training<br>RL: No | [Project weights](https://huggingface.co/heman10x/rlcd-modernbert-151m) | [Sources](docs/evidence.md#verdict) |
| [eve-rlcd](https://github.com/anthony-maio/eve-rlcd) | [6](https://github.com/anthony-maio/eve-rlcd/stargazers) | Unknown | Qwen3-0.6B-Base<br>0.6B | AR LLM<br>Next-token logits / Verbalizer | SFT + RL<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/anthonym21/qwen3-0.6b-rlcd-decision) | [Sources](docs/evidence.md#eve-rlcd) |
| [minojev](https://github.com/zeredy879/minojev) | [25](https://github.com/zeredy879/minojev/stargazers) | Unknown | Qwen3-1.7B<br>1.7B + approximately 0.8M head | AR LLM + Decision Head<br>Option-wise scoring | Head-only<br>RL: No | [Adapter/head](https://huggingface.co/zeredy879/minojev) | [Sources](docs/evidence.md#minojev) |
| [Luce](https://github.com/scienthoon/luce) | [7](https://github.com/scienthoon/luce/stargazers) | Unknown | Qwen3 / Qwen2.5<br>4B default | AR LLM + Decision Head<br>Decision Head / Verbalizer | Distillation + LoRA + Head<br>RL: No | Availability unverified | [Sources](docs/evidence.md#luce) |
| [poorjev](https://github.com/rupeshpoojary9/poorjev) | [10](https://github.com/rupeshpoojary9/poorjev/stargazers) | Unknown | Zero-shot NLI encoders<br>Configuration-dependent | Cross-Encoder<br>NLI option-wise scoring | Calibration Training<br>RL: No | No project-weight release | [Sources](docs/evidence.md#poorjev) |
| [jevbetter](https://github.com/olanotolu/jevbetter) | [15](https://github.com/olanotolu/jevbetter/stargazers) | Unknown | Custom / frozen HF encoder<br>Configuration-dependent | Option Scorer<br>Option-wise scoring | SFT / Head-only<br>RL: No | Availability unverified | [Sources](docs/evidence.md#jevbetter) |
| [JevForge](https://github.com/zwliJay/jev-forge) | [71](https://github.com/zwliJay/jev-forge/stargazers) | Unknown | Qwen3.5-0.8B / Qwen3-0.6B<br>0.8B + scorer | AR LLM + Decision Head<br>Option-wise scoring | SFT; RL prototype<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/AndeyTait/JevForge-0.8B) | [Sources](docs/evidence.md#jevforge) |
| [System One Open](https://github.com/mithalouni/system-one-open) | [37](https://github.com/mithalouni/system-one-open/stargazers) | Unknown | Gemma 4 E2B / Gemma 3 270M<br>E2B (vendor label) / 270M | AR LLM + Decision Head<br>Label-token slots | LoRA / SFT<br>RL: No | No project-weight release | [Sources](docs/evidence.md#system-one-open) |
| [Visual Jev (Yu & Yao)](https://github.com/guanxuyu-sv/Visual-Jev) | [24](https://github.com/guanxuyu-sv/Visual-Jev/stargazers) | Unknown | Qwen3-VL<br>4B / 8B<br>Input: Text + image | AR VLM<br>Existing LM-head candidate-token logits | LoRA / answer SFT<br>RL: No | [Adapter/head](https://huggingface.co/guanxuyu/visual-jev-4b-answer-sft) | [Sources](docs/evidence.md#visual-jev-yu) |
| [Valen](https://github.com/Liuziyu77/Valen) | [347](https://github.com/Liuziyu77/Valen/stargazers) | Unknown | Qwen3.5<br>0.8B / 2B + decision head<br>Input: Text + image + video | Hybrid VLM + Decision Head<br>Shared candidate head; separate ordinal-level branches | SFT + experimental RL<br>RL: RLCD (claimed) | [Adapter/head](https://huggingface.co/Valen-Team/Valen-Preview-0923) | [Sources](docs/evidence.md#valen) |
| [OmniJev (Qwen)](https://github.com/tinnel123666888/OmniJev) | [102](https://github.com/tinnel123666888/OmniJev/stargazers) | Unknown | Qwen3.5<br>0.8B / 2B / 4B<br>Input: Image + frame mosaic + spectrogram | Hybrid VLM + Decision/ordinal heads<br>Typed decision heads; prefix branches | LoRA + Calibration Training<br>RL: No | [Adapter/head](https://huggingface.co/tinnel123/OmniJev) | [Sources](docs/evidence.md#omnijev) |
| [Jev-Spatial](https://github.com/Fr0zenCrane/jev-spatial) | [2](https://github.com/Fr0zenCrane/jev-spatial/stargazers) | Unknown | Molmo2-ER<br>Not separately verified<br>Input: Image(s) + spatial question | AR VLM + Decision Head<br>Unified choice head; hierarchical scalar/point decisions | LoRA + Decision Head<br>RL: No | [Project weights](https://huggingface.co/Fr0zencr4nE/jev-spatial) | [Sources](docs/evidence.md#jev-spatial) |
| [LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) | [349](https://github.com/Yinsongxu/LLM2Jev/stargazers) | Unknown | Configurable LLM / VLM (Qwen examples)<br>Configuration-dependent<br>Input: Text + image | AR/Hybrid VLM / Option Scorer<br>Candidate binary scoring from prefill logits | None<br>RL: No | [Upstream model / setup](https://github.com/Yinsongxu/LLM2Jev) | [Sources](docs/evidence.md#llm2jev) |
| [Jev Visual (MLX)](https://github.com/hr98w/jev-visual) | [291](https://github.com/hr98w/jev-visual/stargazers) | Unknown | Qwen3.5-0.8B<br>0.8B; documented 4-bit path<br>Input: Text + image / camera frame | Hybrid VLM / Option Scorer<br>Candidate-label / sequence logits | None<br>RL: No | [Upstream model / setup](https://github.com/hr98w/jev-visual) | [Sources](docs/evidence.md#jev-visual-mlx) |
| [Visual Jev (Anderson)](https://github.com/andrueandersoncs/visual-jev) | [3](https://github.com/andrueandersoncs/visual-jev/stargazers) | Unknown | Qwen3-VL<br>Size depends on registry checkpoint<br>Input: Image(s) + text | AR VLM + Pointer Head<br>Learned option pointer head | LoRA + Decision Head + Calibration Training<br>RL: No | Availability unverified | [Sources](docs/evidence.md#visual-jev-anderson) |
| [OpenJev Multimodal](https://github.com/jev-skills/openjev-multimodal) | [3](https://github.com/jev-skills/openjev-multimodal/stargazers) | Unknown | Qwen VLM family via llama.cpp<br>0.8B / 4B default profiles; larger optional<br>Input: Text + image / sampled frames | AR/Hybrid VLM<br>One generated label token + candidate probabilities | None<br>RL: No | [Upstream model / setup](https://github.com/jev-skills/openjev-multimodal) | [Sources](docs/evidence.md#openjev-multimodal) |
| [Jev-Omni (Gemma)](https://huggingface.co/akhilaaa3/Jev-Omni) | — | Unknown | Gemma 4 12B IT<br>12B + 256-slot head<br>Input: Text + image + audio + frames | Multimodal Backbone + Classification Head<br>Last-hidden-state 256-slot classifier | Fine-tuning (author reported)<br>RL: Unknown | [Project weights](https://huggingface.co/akhilaaa3/Jev-Omni) | [Sources](docs/evidence.md#jev-omni) |
| [GroundingJev (task-specific)](https://github.com/xyzzzh/GroundingJev) | [7](https://github.com/xyzzzh/GroundingJev/stargazers) | Unknown | Qwen3.5-0.8B<br>0.8B + regression head<br>Input: Image + referring expression | Hybrid VLM + Regression Head<br>Continuous normalized bounding-box regression | Head-only then joint SFT<br>RL: No | [Project weights](https://huggingface.co/xyzzzh/GroundingJev) | [Sources](docs/evidence.md#groundingjev) |
<!-- landscape:end -->

メタデータ更新：**2026-09-28**（今回はマルチモーダル中心。旧項目の全面再検証ではありません） · Stars 取得：**2026-09-28T04:19:51Z**（[API 出典](data/github-stars.json)）。Unknown は初回公開日の未確認を示します。Stars は技術品質の指標ではありません。

[技術比較の全項目](docs/comparison.md) · [根拠とバージョン情報](docs/evidence.md) · [検証上の制約](docs/audit.md) · [マルチモーダル：画像・動画・音声・位置推定](docs/multimodal.md)

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
| 画像から直接判断する | [Jev Visual (MLX)](docs/evidence.md#jev-visual-mlx) · [LLM2Jev](docs/evidence.md#llm2jev) · [OpenJev Multimodal](docs/evidence.md#openjev-multimodal) | [画素入力とテキスト化・キャッシュ再利用](docs/multimodal.md) |
| 視覚判断の学習と RL を調べる | [Visual Jev (Yu & Yao)](docs/evidence.md#visual-jev-yu) · [Valen](docs/evidence.md#valen) · [OmniJev (Qwen)](docs/evidence.md#omnijev) | [既存 LM head と学習済み head・RL と校正損失](docs/multimodal.md) |
| 空間判断と位置推定を調べる | [Jev-Spatial](docs/evidence.md#jev-spatial) · [GroundingJev (task-specific)](docs/evidence.md#groundingjev) | [階層的グリッド選択と直接 bbox 回帰](docs/multimodal.md) |
| 動画と音声の入力経路を比較する | [Jev-Omni (Gemma)](docs/evidence.md#jev-omni) · [OmniJev (Qwen)](docs/evidence.md#omnijev) · [Valen](docs/evidence.md#valen) | [フレーム抽出・モザイク・スペクトログラム・音声入力](docs/multimodal.md) |

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
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | [466](https://github.com/OmniJev/awesome-jev-gallery/stargazers) | 2026-09 | English | Research / Ecosystem | 論文、オープンモデル、評価、エコシステム資料。改名後の正規 URL。 |
| [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev) | [1](https://github.com/Zhao-Tian-yi/awesome-jev/stargazers) | 2026-09-21 | English / 简体中文 / 日本語 | Research | はい、このリポジトリも awesome Jev リストの awesome list に入りました。 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | [1,852](https://github.com/yibie/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | 応用領域別の一覧。掲載と品質の保証を明確に区別する。 |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | [513](https://github.com/AnotiaWang/awesome-jev/stargazers) | Unknown | English / 简体中文 | Ecosystem | アプリケーション、ライブラリ、ツール、研究の二言語一覧。 |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | [201](https://github.com/hellogumbo/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | 検索可能な付属サイトを持つアプリケーションと統合の一覧。 |
