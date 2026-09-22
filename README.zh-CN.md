# Awesome Jev

> **本仓库近期会高强度实时更新**，持续跟进 Jev / System One Models 的开源实现、模型架构、训练方法与评测进展。

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

面向研究的 Jev 与 System One Model 技术图谱，整理开源实现、模型架构、训练方法及可用代码与权重。

[模型全景](#models) · [按需求查找](#start-here) · [官方资源与工具](#official) · [Awesome Awesome Jev 😄](#awesome-awesome-jev)

<!-- Generated from data/*.yaml. See scripts/generate_readme.py. -->

<a id="models"></a>

## 模型全景

官方 Jev 始终置顶。其余按已核实的首次公开日期升序排列；未知日期保留原策展顺序，不按 Stars 排名。

<!-- landscape:start -->
| Project | GitHub Stars | First Public | Backbone / Size | Decision Architecture | Training / RL | Artifacts | Evidence |
|---|---:|---|---|---|---|---|---|
| [Official Jev](https://github.com/typesafe-ai) | — | Unknown | Not disclosed<br>Not disclosed | Custom / Not Disclosed<br>Not disclosed | Not disclosed<br>RL: RLCD | [API only](https://typesafe.ai/) | [Sources](docs/evidence.md#official-jev) |
| [SemIf](https://github.com/TheoLeeCJ/SemIf) | [3,341](https://github.com/TheoLeeCJ/SemIf/stargazers) | Unknown | Qwen3.5 / MiniCPM5 / Qwen3<br>0.6B / 2B / 4B | AR LLM<br>Next-token logits | None<br>RL: No | [Upstream model / setup](https://github.com/TheoLeeCJ/SemIf) | [Sources](docs/evidence.md#semif) |
| [OpenJev / DiffusionGemma](https://github.com/razorback16/openjev) | [285](https://github.com/razorback16/openjev/stargazers) | Unknown | DiffusionGemma 26B-A4B<br>26B total / approximately 4B active | Diffusion / Masked<br>Masked decision slots | None<br>RL: No | [Upstream weights](https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4) | [Sources](docs/evidence.md#openjev-diffusiongemma) |
| [Kev](https://github.com/jaredpalmer/kev) | [2,607](https://github.com/jaredpalmer/kev/stargazers) | Unknown | Qwen3.5; earlier Qwen3<br>0.8B / 4B / 9B | AR LLM + Pointer Head<br>Pointer head | LoRA + Decision Head<br>RL: No | [Adapter/head](https://huggingface.co/jaredpalmer/kev-4b) | [Sources](docs/evidence.md#kev) |
| [NanoJev](https://github.com/TianyuCodings/NanoJev) | [1,852](https://github.com/TianyuCodings/NanoJev/stargazers) | Unknown | Qwen3-0.6B<br>0.6B + heads | AR LLM + Decision Head<br>Option-wise scoring | SFT; RL prototype<br>RL: RLCD (claimed) | [Project weights](https://huggingface.co/C-Tianyu/NanoJev) | [Sources](docs/evidence.md#nanojev) |
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

技术核查：**2026-09-21** · Stars 快照：**2026-09-22T03:56:53Z**（[API 来源](data/github-stars.json)）。Unknown 表示首次公开日期未核实；Stars 不代表技术质量。

[完整技术对照表](docs/comparison.md) · [证据与版本说明](docs/evidence.md) · [核查限制](docs/audit.md)

<a id="start-here"></a>

## 按需求查找

这是阅读入口，不是性能排名。使用前请查看所链接的版本与证据说明。

| 目标 | 阅读入口 | 重点检查 |
|---|---|---|
| 不训练，先做本地决策 | [SemIf](docs/evidence.md#semif) · [mini-Jev](docs/evidence.md#mini-jev) | [候选 logits 与共享前缀](docs/comparison.md) |
| 自己训练决策机制 | [Kev](docs/evidence.md#kev) · [NanoJev](docs/evidence.md#nanojev) · [Luce](docs/evidence.md#luce) | [Decision Head、数据格式与训练路径](docs/training.md) |
| 研究 encoder 决策路线 | [Laya](docs/evidence.md#laya) · [Von](docs/evidence.md#von) | [双向编码与动态候选](docs/architecture.md) |
| 研究 diffusion 回答槽位 | [OpenJev / DiffusionGemma](docs/evidence.md#openjev-diffusiongemma) | [Masked slots、去噪步数与问题隔离](docs/architecture.md) |
| 研究校准相关强化学习 | [eve-rlcd](docs/evidence.md#eve-rlcd) · [Laya](docs/evidence.md#laya) · [NanoJev](docs/evidence.md#nanojev) | [采样、reward、梯度与 checkpoint 范围](docs/training.md) |

<a id="official"></a>

## 官方资源与工具

[TypeSafe](https://typesafe.ai/) · [发布文章](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [官方文档](https://docs.typesafe.ai/) · [官方 GitHub](https://github.com/typesafe-ai)。SDK 源码不等于 Jev 模型源码；具体核实范围见[核查记录](docs/audit.md)。

| Tool | Purpose |
|---|---|
| [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) | Python 客户端与 API schema |
| [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) | JavaScript/TypeScript 客户端 |
| [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) | 把普通 LLM API 包装成 System One 比较接口 |
| [skills](https://github.com/typesafe-ai/skills) | 问题设计指南与实例，不是网络结构说明 |

<a id="awesome-awesome-jev"></a>

## Awesome Awesome Jev 😄

收集 awesome Jev lists 的 awesome list。已知首次公开日期优先；Unknown 不代表尚未公开。

| Repository | GitHub Stars | First Public | Languages | Focus | Notes |
|---|---:|---|---|---|---|
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | [155](https://github.com/OmniJev/awesome-jev-gallery/stargazers) | 2026-09 | English | Research / Ecosystem | 论文、开源模型、评测与生态资源；使用更名后的规范仓库地址。 |
| [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev) | [1](https://github.com/Zhao-Tian-yi/awesome-jev/stargazers) | 2026-09-21 | English / 简体中文 / 日本語 | Research | 是的，本仓库现在也是 awesome Jev 列表的 awesome list 的一员。 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | [1,028](https://github.com/yibie/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | 按应用领域组织，明确区分收录与质量背书。 |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | [257](https://github.com/AnotiaWang/awesome-jev/stargazers) | Unknown | English / 简体中文 | Ecosystem | 中英双语整理应用、库、工具与研究。 |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | [127](https://github.com/hellogumbo/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | 应用与集成目录，配有可搜索的网站。 |
