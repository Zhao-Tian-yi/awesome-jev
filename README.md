# Awesome Jev

> **Frequent, real-time updates ahead:** This repository will be updated intensively in the near term, tracking new Jev / System One Models implementations, architectures, training methods, and evaluations.

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

**Compare how Jev-like models make decisions, how they are trained, and which code and weights you can use.**

A research-oriented map of Jev and System One Models. Architectures, decision readouts, RLCD and Calibration — with links to the implementation behind each label.

21 community implementations · 1 official reference · 6 related papers · English / 中文 / 日本語

[Models](#models) · [Find by goal](#start-here) · [Recent updates](#updates) · [Training audit](docs/training.md) · [Contribute](#contributing)

Star this map to find the comparisons and source links again when choosing or training a decision model.

<!-- Generated from data/*.yaml. See scripts/generate_readme.py. -->

## What is Jev?

`State + runtime-defined question + options → typed probabilistic decision`. Noul estimates a binary condition; Choice compares declared options; Score returns an ordered-level distribution and expectation. This list separates the official API from independent implementations. **Non-AR does not imply diffusion; direct probabilities do not guarantee Calibration.**

<a id="models"></a>

## Model Landscape

Official Jev stays first. Other rows follow verified first-public dates, then the existing curation order when dates are unknown. Stars do not determine the order.

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

[Full technical table](docs/comparison.md) · [Evidence and version notes](docs/evidence.md) · [Audit limitations](docs/audit.md)

<details>
<summary>Definitions, date coverage, and full technical comparison</summary>

**22/22 first-public dates remain unverified.** Unknown is not replaced by repository creation dates or later releases. **AR Decoding** in the full table concerns answer generation, not backbone pretraining. **Artifacts** distinguishes project weights, adapters/heads and reused upstream models. RL labels are version-specific; see the actual methods rather than treating every RLCD claim as the proprietary recipe.

Technical audit: 2026-09-21.

Stars sampled at 2026-09-21T13:48:47Z; this is a popularity snapshot, not a quality score. [API sources](data/github-stars.json). Refreshing stars does not refresh the technical audit.

</details>

<details>
<summary>Expand the Jev-like capability matrix</summary>

✅ documented · ⚠️ partial, variant-specific or ordinary batching · ❌ absent · ? unverified. Shared State means reused computation. Parallel Q distinguishes native slots from batched rows. Calibration records procedures/evidence, not a universal guarantee.

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

## Find by goal

Reading routes, not a ranking. Check the linked version notes before using a project.

| Goal | Starting points | What to inspect |
|---|---|---|
| Try decisions without training | [SemIf](docs/evidence.md#semif) · [mini-Jev](docs/evidence.md#mini-jev) | [Candidate logits and shared prefixes](docs/comparison.md) |
| Train a decision mechanism | [Kev](docs/evidence.md#kev) · [NanoJev](docs/evidence.md#nanojev) · [Luce](docs/evidence.md#luce) | [Decision heads, data formats and training paths](docs/training.md) |
| Explore encoder-based decisions | [Laya](docs/evidence.md#laya) · [Von](docs/evidence.md#von) | [Bidirectional encoding and dynamic candidates](docs/architecture.md) |
| Study diffusion answer slots | [OpenJev / DiffusionGemma](docs/evidence.md#openjev-diffusiongemma) | [Masked slots, denoising steps and question isolation](docs/architecture.md) |
| Inspect calibration-aware RL | [eve-rlcd](docs/evidence.md#eve-rlcd) · [Laya](docs/evidence.md#laya) · [NanoJev](docs/evidence.md#nanojev) | [Sampling, rewards, gradients and checkpoint scope](docs/training.md) |

<a id="updates"></a>

## Recent updates

These dates describe changes to this list, not upstream release dates. Star-only refreshes are excluded. [Full log](docs/updates.md).

| Date | Type | Change | Evidence |
|---|---|---|---|
| 2026-09-21 | Updated | Compact eight-column model map, goal-based reading routes, explicit artifact links and lightweight contribution forms; full audited fields retained. | [Source](docs/comparison.md) |
| 2026-09-21 | Added | Numeric GitHub Stars snapshots and trilingual update notices, without changing chronological curation order. | [Source](https://github.com/Zhao-Tian-yi/awesome-jev/commit/fccf8a0ecd6c8d393acd2e734d6572f0c6d1e82c) |
| 2026-09-21 | Corrected | Rebuilt the map from shared YAML; separated decision decoding, backbone families and community RL evidence, with version-specific caveats. | [Source](https://github.com/Zhao-Tian-yi/awesome-jev/commit/5b64c6751e5b11597dde04ed73dafe47ba597c0f) |

## Research guide

| Question | Read |
|---|---|
| How is a probability produced? | [architecture.md](docs/architecture.md) |
| What does RLCD mean in each implementation? | [training.md](docs/training.md) |
| How does Jev relate to LLMs, rerankers and diffusion? | [jev-vs-models.md](docs/jev-vs-models.md) |
| How should quality, Calibration and efficiency be compared? | [evaluation.md](docs/evaluation.md) |

Methods remain separate from measured outcomes. We do not infer vendor internals from API behavior or compare unmatched benchmark numbers as a leaderboard.

<details>
<summary>Expand verified version / artifact milestones</summary>

Version milestones are not first-public dates. Official Jev is kept first; the remaining dated milestones are chronological.

| Date | Project | Milestone |
|---|---|---|
| Unknown | Official Jev | Official reference |
| 2026-09-18 | eve-rlcd | [Version/artifact](https://github.com/anthony-maio/eve-rlcd/releases/tag/data-v1) |
| 2026-09-19 | Laya | [Version/artifact](https://github.com/NandhaKishorM/laya/releases/tag/v0.2.0) |
| 2026-09-20 | Kev | [Version/artifact](https://github.com/jaredpalmer/kev/releases/tag/kev-family) |

</details>

## Related research

Primary research ordered by arXiv v1 date; these are related methods, not automatically Jev implementations.

| Date | Paper | Topic |
|---|---|---|
| 2017-06-14 | [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) | Calibration |
| 2018-10-11 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | Encoder / Masked LM |
| 2024-06-11 | [Simple and Effective Masked Diffusion Language Models](https://arxiv.org/abs/2406.07524) | Masked Diffusion |
| 2025-02-14 | [Large Language Diffusion Models](https://arxiv.org/abs/2502.09992) | Diffusion LM |
| 2025-07-22 | [Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty](https://arxiv.org/abs/2507.16806) | RLCR |
| 2025-08-11 | [GLiClass: Generalist Lightweight Model for Sequence Classification Tasks](https://arxiv.org/abs/2508.07662) | Runtime label classification |

## Official resources and tools

[TypeSafe](https://typesafe.ai/) · [Launch article](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [Documentation](https://docs.typesafe.ai/) · [Official GitHub](https://github.com/typesafe-ai). SDK source is not Jev model source. Current verification boundaries are retained in the [audit](docs/audit.md).

| Tool | Purpose |
|---|---|
| [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) | Python client and API schemas |
| [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) | JavaScript/TypeScript client |
| [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) | Ordinary LLM APIs behind a System One comparison interface |
| [skills](https://github.com/typesafe-ai/skills) | Question-design guidance and worked patterns; not a network specification |

Application example: [Jevenator 2](https://github.com/mmastrac/jevenator2) uses a separate decision endpoint for region-scan localization. It is not a new backbone or evidence of official Jev architecture.

<a id="contributing"></a>

## Contributing

Found a project or a mistake? Send a link, a short explanation and supporting evidence. **No YAML editing or three-language translation is required to open an issue.** Maintainers validate facts and synchronize translations before inclusion.

[Suggest a project](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=suggest-project.yml) · [Correct an entry](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml)

For a pull request, edit the YAML facts and regenerate the pages. [Contribution guide](CONTRIBUTING.md) · [Content license](LICENSE) · [Code license](LICENSE-CODE). Independent resource; not affiliated with TypeSafe AI.

## Awesome Awesome Jev 😄

An awesome list of awesome Jev lists. Known first-public dates first; Unknown does not mean unpublished.

| Repository | GitHub Stars | First Public | Languages | Focus | Notes |
|---|---:|---|---|---|---|
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | [141](https://github.com/OmniJev/awesome-jev-gallery/stargazers) | 2026-09 | English | Research / Ecosystem | Papers, open models, evaluations and ecosystem resources; canonical renamed repository. |
| [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev) | [1](https://github.com/Zhao-Tian-yi/awesome-jev/stargazers) | 2026-09-21 | English / 简体中文 / 日本語 | Research | Yes, this repo is now part of an awesome list of awesome Jev lists. |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | [853](https://github.com/yibie/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | Application-domain catalogue with explicit curation and evidence caveats. |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | [205](https://github.com/AnotiaWang/awesome-jev/stargazers) | Unknown | English / 简体中文 | Ecosystem | Bilingual catalogue of applications, libraries, tools and research. |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | [115](https://github.com/hellogumbo/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | Application and integration directory with a searchable companion site. |
