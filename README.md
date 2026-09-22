# Awesome Jev

> **Frequent, real-time updates ahead:** This repository will be updated intensively in the near term, tracking new Jev / System One Models implementations, architectures, training methods, and evaluations.

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

A research-oriented map of Jev and System One Models: implementations, architectures, training, and available code and weights.

[Model Landscape](#models) · [Find by goal](#start-here) · [Official resources and tools](#official) · [Awesome Awesome Jev 😄](#awesome-awesome-jev)

<!-- Generated from data/*.yaml. See scripts/generate_readme.py. -->

<a id="models"></a>

## Model Landscape

Official Jev stays first. Other rows follow verified first-public dates, then existing curation order for unknown dates. Stars do not determine the order.

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

Technical audit: **2026-09-21** · Stars snapshot: **2026-09-22T03:56:16Z** ([API sources](data/github-stars.json)). Unknown means the first-public date is unverified; stars are not a quality score.

[Full technical table](docs/comparison.md) · [Evidence and version notes](docs/evidence.md) · [Audit limitations](docs/audit.md)

<a id="start-here"></a>

## Find by goal

Reading routes, not a ranking. Check the linked version notes before using a project.

| Goal | Starting points | What to inspect |
|---|---|---|
| Try decisions without training | [SemIf](docs/evidence.md#semif) · [mini-Jev](docs/evidence.md#mini-jev) | [Candidate logits and shared prefixes](docs/comparison.md) |
| Train a decision mechanism | [Kev](docs/evidence.md#kev) · [NanoJev](docs/evidence.md#nanojev) · [Luce](docs/evidence.md#luce) | [Decision heads, data formats and training paths](docs/training.md) |
| Explore encoder-based decisions | [Laya](docs/evidence.md#laya) · [Von](docs/evidence.md#von) | [Bidirectional encoding and dynamic candidates](docs/architecture.md) |
| Study diffusion answer slots | [OpenJev / DiffusionGemma](docs/evidence.md#openjev-diffusiongemma) | [Masked slots, denoising steps and question isolation](docs/architecture.md) |
| Inspect calibration-aware RL | [eve-rlcd](docs/evidence.md#eve-rlcd) · [Laya](docs/evidence.md#laya) · [NanoJev](docs/evidence.md#nanojev) | [Sampling, rewards, gradients and checkpoint scope](docs/training.md) |

<a id="official"></a>

## Official resources and tools

[TypeSafe](https://typesafe.ai/) · [Launch article](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [Documentation](https://docs.typesafe.ai/) · [Official GitHub](https://github.com/typesafe-ai). SDK source is not Jev model source; see the [audit](docs/audit.md) for verification boundaries.

| Tool | Purpose |
|---|---|
| [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) | Python client and API schemas |
| [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) | JavaScript/TypeScript client |
| [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) | Ordinary LLM APIs behind a System One comparison interface |
| [skills](https://github.com/typesafe-ai/skills) | Question-design guidance and worked patterns; not a network specification |

<a id="awesome-awesome-jev"></a>

## Awesome Awesome Jev 😄

An awesome list of awesome Jev lists. Known first-public dates first; Unknown does not mean unpublished.

| Repository | GitHub Stars | First Public | Languages | Focus | Notes |
|---|---:|---|---|---|---|
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | [155](https://github.com/OmniJev/awesome-jev-gallery/stargazers) | 2026-09 | English | Research / Ecosystem | Papers, open models, evaluations and ecosystem resources; canonical renamed repository. |
| [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev) | [1](https://github.com/Zhao-Tian-yi/awesome-jev/stargazers) | 2026-09-21 | English / 简体中文 / 日本語 | Research | Yes, this repo is now part of an awesome list of awesome Jev lists. |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | [1,027](https://github.com/yibie/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | Application-domain catalogue with explicit curation and evidence caveats. |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | [257](https://github.com/AnotiaWang/awesome-jev/stargazers) | Unknown | English / 简体中文 | Ecosystem | Bilingual catalogue of applications, libraries, tools and research. |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | [127](https://github.com/hellogumbo/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | Application and integration directory with a searchable companion site. |
