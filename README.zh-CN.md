# Awesome Jev

> **本仓库近期会高强度实时更新**，持续跟进 Jev / System One Models 的开源实现、模型架构、训练方法与评测进展。

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

**看清 Jev-like 模型怎么实现、怎么训练，以及哪些代码和权重可以使用。**

面向研究的 Jev 与 System One Model 技术图谱。对照架构、决策读出、RLCD 与 Calibration，并追溯每个技术标签背后的实现。

21 个社区实现 · 1 个官方参照 · 6 篇相关研究 · English / 中文 / 日本語

[模型比较](#models) · [按需求查找](#start-here) · [近期更新](#updates) · [训练核查](docs/training.md) · [参与贡献](#contributing)

收藏这份对照表，后续选模型、查训练方法和源码证据时方便回来查看。

<!-- Generated from data/*.yaml. See scripts/generate_readme.py. -->

## 什么是 Jev？

`State + 运行时定义的问题 + 选项 → 有类型的概率决策`。Noul 估计二元条件，Choice 比较给定候选，Score 返回有序等级分布及其期望。本仓库区分官方 API 与独立实现。**Non-AR 不等于 diffusion；直接输出概率不保证 Calibration。**

<a id="models"></a>

## 模型全景

官方 Jev 始终置顶。其余按已核实的首次公开日期升序排列；未知日期保留原策展顺序，不按 Stars 排名。

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

[完整技术对照表](docs/comparison.md) · [证据与版本说明](docs/evidence.md) · [核查限制](docs/audit.md)

<details>
<summary>展开字段定义、日期完整性与详细对照</summary>

**22/22 个首次公开日期仍未核实。** 保留 Unknown，不以仓库创建时间或后续版本日期代替。详细表的 **AR Decoding** 判断答案是否逐 token 生成，而非底座预训练方式。**Artifacts** 区分项目权重、adapter/head 与复用上游模型。RL 状态以具体版本为准，不能把社区 RLCD 名称直接当成官方配方。

技术核查日期：2026-09-21。

Stars 采集时间：2026-09-21T13:48:47Z；仅作关注度快照，不代表技术质量。[API 来源](data/github-stars.json)。刷新 Stars 不等于重新核查技术信息。

</details>

<details>
<summary>展开 Jev-like 能力矩阵</summary>

✅ 文档支持 · ⚠️ 部分、特定版本或普通 batch · ❌ 不支持 · ? 未核实。Shared State 指计算复用，Parallel Q 区分原生槽位与批处理行；Calibration 记录方法或证据，不代表普遍保证。

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

## 按需求查找

这是阅读入口，不是性能排名。使用前请查看所链接的版本与证据说明。

| 目标 | 阅读入口 | 重点检查 |
|---|---|---|
| 不训练，先做本地决策 | [SemIf](docs/evidence.md#semif) · [mini-Jev](docs/evidence.md#mini-jev) | [候选 logits 与共享前缀](docs/comparison.md) |
| 自己训练决策机制 | [Kev](docs/evidence.md#kev) · [NanoJev](docs/evidence.md#nanojev) · [Luce](docs/evidence.md#luce) | [Decision Head、数据格式与训练路径](docs/training.md) |
| 研究 encoder 决策路线 | [Laya](docs/evidence.md#laya) · [Von](docs/evidence.md#von) | [双向编码与动态候选](docs/architecture.md) |
| 研究 diffusion 回答槽位 | [OpenJev / DiffusionGemma](docs/evidence.md#openjev-diffusiongemma) | [Masked slots、去噪步数与问题隔离](docs/architecture.md) |
| 研究校准相关强化学习 | [eve-rlcd](docs/evidence.md#eve-rlcd) · [Laya](docs/evidence.md#laya) · [NanoJev](docs/evidence.md#nanojev) | [采样、reward、梯度与 checkpoint 范围](docs/training.md) |

<a id="updates"></a>

## 近期更新

这里记录本仓库的变化，不是上游项目的发布日期；仅刷新 Stars 不计入实质更新。[完整记录](docs/updates.md)。

| 日期 | 类型 | 变化 | 依据 |
|---|---|---|---|
| 2026-09-21 | Updated | 首页精简为八列，新增按需求查找、产物链接与轻量投稿入口；完整核查字段仍保留。 | [Source](docs/comparison.md) |
| 2026-09-21 | Added | 增加 GitHub Stars 数字快照与三语更新声明，不改变按时间策展的规则。 | [Source](https://github.com/Zhao-Tian-yi/awesome-jev/commit/fccf8a0ecd6c8d393acd2e734d6572f0c6d1e82c) |
| 2026-09-21 | Corrected | 使用统一 YAML 重建技术图谱，区分决策生成、底座架构与社区 RL 证据，并补充版本限制。 | [Source](https://github.com/Zhao-Tian-yi/awesome-jev/commit/5b64c6751e5b11597dde04ed73dafe47ba597c0f) |

## 研究导航

| 问题 | 资料 |
|---|---|
| 模型如何得到概率？ | [architecture.md](docs/architecture.md) |
| 不同实现中的 RLCD 到底是什么？ | [training.md](docs/training.md) |
| Jev 与 LLM、reranker、diffusion 有什么关系？ | [jev-vs-models.md](docs/jev-vs-models.md) |
| 如何公平比较能力、Calibration 与效率？ | [evaluation.md](docs/evaluation.md) |

训练机制与实测效果分开记录；不从 API 行为推断厂商内部架构，也不将不同条件下的 benchmark 数字拼成排行榜。

<details>
<summary>展开已核实的版本／产物里程碑</summary>

版本里程碑不等于首次公开日期。官方 Jev 置顶，其后已知日期升序排列。

| Date | Project | Milestone |
|---|---|---|
| Unknown | Official Jev | Official reference |
| 2026-09-18 | eve-rlcd | [Version/artifact](https://github.com/anthony-maio/eve-rlcd/releases/tag/data-v1) |
| 2026-09-19 | Laya | [Version/artifact](https://github.com/NandhaKishorM/laya/releases/tag/v0.2.0) |
| 2026-09-20 | Kev | [Version/artifact](https://github.com/jaredpalmer/kev/releases/tag/kev-family) |

</details>

## 相关研究

按 arXiv v1 日期排列的一手研究；相关方法不直接算作 Jev 实现。

| Date | Paper | Topic |
|---|---|---|
| 2017-06-14 | [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) | Calibration |
| 2018-10-11 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | Encoder / Masked LM |
| 2024-06-11 | [Simple and Effective Masked Diffusion Language Models](https://arxiv.org/abs/2406.07524) | Masked Diffusion |
| 2025-02-14 | [Large Language Diffusion Models](https://arxiv.org/abs/2502.09992) | Diffusion LM |
| 2025-07-22 | [Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty](https://arxiv.org/abs/2507.16806) | RLCR |
| 2025-08-11 | [GLiClass: Generalist Lightweight Model for Sequence Classification Tasks](https://arxiv.org/abs/2508.07662) | Runtime label classification |

## 官方资源与工具

[TypeSafe](https://typesafe.ai/) · [发布文章](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [官方文档](https://docs.typesafe.ai/) · [官方 GitHub](https://github.com/typesafe-ai)。SDK 源码不等于 Jev 模型源码；具体核实范围见[核查记录](docs/audit.md)。

| Tool | Purpose |
|---|---|
| [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) | Python 客户端与 API schema |
| [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) | JavaScript/TypeScript 客户端 |
| [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) | 把普通 LLM API 包装成 System One 比较接口 |
| [skills](https://github.com/typesafe-ai/skills) | 问题设计指南与实例，不是网络结构说明 |

应用示例：[Jevenator 2](https://github.com/mmastrac/jevenator2) 调用独立决策端点完成区域扫描定位；它不是新底座，也不能证明官方 Jev 的架构。

<a id="contributing"></a>

## 参与贡献

发现新项目或错误？提交链接、简短说明和证据即可。**提 Issue 不要求修改 YAML，也不要求翻译三种语言。** 维护者核查后再同步事实与翻译。

[推荐项目](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=suggest-project.yml) · [纠正条目](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml)

提交 PR 时修改 YAML 事实源并重新生成页面。[贡献指南](CONTRIBUTING.md) · [内容许可](LICENSE) · [代码许可](LICENSE-CODE)。本仓库为独立整理，与 TypeSafe AI 无隶属关系。

## Awesome Awesome Jev 😄

收集 awesome Jev lists 的 awesome list。已知首次公开日期优先；Unknown 不代表尚未公开。

| Repository | GitHub Stars | First Public | Languages | Focus | Notes |
|---|---:|---|---|---|---|
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | [141](https://github.com/OmniJev/awesome-jev-gallery/stargazers) | 2026-09 | English | Research / Ecosystem | 论文、开源模型、评测与生态资源；使用更名后的规范仓库地址。 |
| [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev) | [1](https://github.com/Zhao-Tian-yi/awesome-jev/stargazers) | 2026-09-21 | English / 简体中文 / 日本語 | Research | 是的，本仓库现在也是 awesome Jev 列表的 awesome list 的一员。 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | [853](https://github.com/yibie/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | 按应用领域组织，明确区分收录与质量背书。 |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | [205](https://github.com/AnotiaWang/awesome-jev/stargazers) | Unknown | English / 简体中文 | Ecosystem | 中英双语整理应用、库、工具与研究。 |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | [115](https://github.com/hellogumbo/awesome-jev/stargazers) | Unknown | English | Applications / Ecosystem | 应用与集成目录，配有可搜索的网站。 |
