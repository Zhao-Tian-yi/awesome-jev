# Multimodal Jev research map / 多模态 Jev 专题

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Full comparison](comparison.md) · [Training audit](training.md)

Targeted source review: **2026-09-28**. This page is generated from `data/projects.yaml` and `data/papers.yaml`. It does not add a fifth README section. Unlisted or unreviewed modalities are not silently treated as supported.

## Read the input path, not the model name

A native-image decision model sends pixels/visual features into its backbone. A system that first produces OCR, captions, an accessibility tree or simulator state and then sends text to Jev is a multimodal application, not evidence that the decision backbone sees pixels. Camera-frame decisions do not by themselves establish temporal video understanding.

Video frames, a frame mosaic and a dedicated video input path are different representations. Likewise, a spectrogram rendered as an image is not a native audio encoder. API parallelism is not proof of one total forward pass or shared backbone computation. Absence of text decoding does not imply diffusion.

中文口径：直接看图、采样帧、视频拼图、音频频谱图、原生音频及文字中介分别记录；演示回放不等于闭环控制，输出概率也不等于已经校准。

## Input and execution comparison

| Project / reviewed path | Image | Video | Audio | Training | RL evidence | Execution / sharing | Notes |
|---|---|---|---|---|---|---|---|
| [OpenJev / DiffusionGemma](https://github.com/razorback16/openjev) | Native; up to 8 images in documented API | Not documented | Not documented | Frozen DiffusionGemma readout | No Jev-specific RLCD | Joint slots in chunks; optional sequential/think paths change semantics | [Evidence](#openjev-diffusiongemma) |
| [decider](https://github.com/Mapika/decider) | Native decider-2b-vision | Game frames; no general video claim | Not documented | Vision: v5 text transplant + supervised tuning + PPO | Vision PPO from pixels; not vendor RLCD | Vision answer slots; do not inherit current text-engine cache guarantees | [Evidence](#decider) |
| [LitJev](https://github.com/zhengxuyu/litjev) | Native with vision checkpoint | Not established by reviewed documentation | Not documented | Frozen model; optional temperature fitting | No RLCD | Model/backend-dependent; do not infer sharing from one API call | [Evidence](#litjev) |
| [reflex](https://github.com/kshetrajna12/reflex) | Native with vision checkpoint | Not established in reviewed stable path | Not documented | Frozen stable Qwen3.5-4B | No RLCD in stable path | Shared state cache; independent question branches | [Evidence](#reflex) |
| [Visual Jev (Yu & Yao)](https://github.com/guanxuyu-sv/Visual-Jev) | Native image input | Not documented | Not documented | Answer-supervised LoRA | No RL in recommended recipe | One visual/public prefix; isolated suffixes batched | [Evidence](#visual-jev-yu) |
| [Valen](https://github.com/Liuziyu77/Valen) | Native image input | Processor video path documented; temporal evaluation unverified | Not documented | Head warmup; LLM LoRA; optional merger/vision-top tuning | Inspected GRPO-style local RLCD + direct Brier | State preparation shared; backbone recomputed per branch | [Evidence](#valen) |
| [OmniJev (Qwen)](https://github.com/tinnel123666888/OmniJev) | Native images; multi-image panels | 16 timestamped frames rendered as one mosaic | Spectrogram / waveform images | LoRA + heads; probability scoring + temperature fit | No RL stage documented | Prefix-branch inference; panels and checkpoint-dependent path | [Evidence](#omnijev) |
| [Jev-Spatial](https://github.com/Fr0zenCrane/jev-spatial) | Native images and selected crops | Not documented | Not documented | LLM LoRA + unified head; vision/projector frozen | Supervised cross-entropy; no RLCD | Shared image cache; same-round crop batching | [Evidence](#jev-spatial) |
| [LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) | Native images in state/instructions | Not documented | Not documented | Frozen backbone | No RLCD | Staged SGLang candidate cache; explicit MLX prefix reuse | [Evidence](#llm2jev) |
| [Jev Visual (MLX)](https://github.com/hr98w/jev-visual) | Native pixels | Per-frame camera demos; no temporal-video claim | Not documented | None | No RLCD | Shared prefill; copied cache; suffix batches | [Evidence](#jev-visual-mlx) |
| [Visual Jev (Anderson)](https://github.com/andrueandersoncs/visual-jev) | Native one/multiple images (documented) | Not documented | Not documented | Documented LoRA + pointer head; temperature fit | No RLCD evidence in reviewed documentation | Packed isolated question branches (documented) | [Evidence](#visual-jev-anderson) |
| [OpenJev Multimodal](https://github.com/jev-skills/openjev-multimodal) | Native PNG/JPEG/WebP | Sampled images only; native video unsupported | Unsupported in reviewed backend | None | No RLCD | One output token/question; local serialized-resource default | [Evidence](#openjev-multimodal) |
| [Jev-Omni (Gemma)](https://huggingface.co/akhilaaa3/Jev-Omni) | Native image encoder | 16-frame public helper; processor configuration is a separate path | Native Gemma audio components | Reported fine-tuning; full training scope unverified | Unknown; do not infer RLCD from calibration metrics | One question/call; no shared multi-question discount | [Evidence](#jev-omni) |
| [GroundingJev (task-specific)](https://github.com/xyzzzh/GroundingJev) | Native pixels | Not documented | Not documented | Head adaptation + joint language/merger/head training | No RLCD; L1/GIoU supervision | One-pass box regression; no multi-Q reuse established | [Evidence](#groundingjev) |

## Version-specific evidence

A family-level training label must not be inherited by every media checkpoint. The entries below state the reviewed variant; benchmark numbers were not rerun.

### openjev-diffusiongemma

**[OpenJev / DiffusionGemma](https://github.com/razorback16/openjev)** · Media checked: 2026-09-28

Reads allowed labels at answer slots; optional denoising and noisy rereads. Joint slots/chunks are not evidence of Jev-style question isolation. Sample averaging and entropy confidence are not calibration guarantees. Linked weights belong to the upstream model.

**Multimodal scope:** The default DiffusionGemma path reads masked answer slots. steps/samples and optional think/sequential modes are different compute paths; question independence is not guaranteed for joint slots. Laya/CLM/JevK5 endpoints are separately credited models, not DiffusionGemma variants.

**中文：** 默认 DiffusionGemma 路径读取 masked 槽位；steps/samples 与 think/sequential 改变计算过程，联合槽位不保证问题独立。其 Laya/CLM/JevK5 端点是其他模型，不是 DiffusionGemma 变体。

**日本語：** 既定の DiffusionGemma は masked slot 読出し。steps/samples/think/sequential は別経路で、共同スロットは質問独立性を保証しない。他のモデル endpoint は DiffusionGemma の派生ではない。

[Primary source](https://github.com/razorback16/openjev/blob/main/README.md) · [All evidence](evidence.md#openjev-diffusiongemma)

[Reviewed media artifact](https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4)

### decider

**[decider](https://github.com/Mapika/decider)** · Media checked: 2026-09-28

Corrected the old no-RL entry: 2B v10 adds PPO, proper-log-score belief learning and consistency; 35B remains supervised. RLCR-like describes the objective family, not reproduction of the RLCR paper or TypeSafe RLCD.

**Multimodal scope:** The vision card specifies v5 text weights, supervised multimodal data and then PPO on Breakout/Pong. Do not label it as current 2B v11 or inherit v10 belief-calibration results. The main repo now lists 4B v2.1, 2B v11 and September 27 GGUF support.

**中文：** 视觉模型卡明确是 v5 文本权重移植、图文监督后在 Breakout/Pong 做 PPO。不是当前 2B v11，也不能继承 v10 的 belief 校准结果。主库已列出 4B v2.1、2B v11 与 9 月 27 日 GGUF 支持。

**日本語：** 視覚版は v5 の言語重み、マルチモーダル教師学習、Breakout/Pong の PPO。2B v11 と同一ではなく v10 の belief 校正結果を引き継ぐとは言えない。主庫は 4B v2.1、2B v11、9/27 GGUF を追加。

[Primary source](https://github.com/Mapika/decider/blob/23579f7a7e8f10e1045be492af3c1c05a005d67c/MODEL_CARD_VISION.md) · [All evidence](evidence.md#decider)

[Reviewed media artifact](https://huggingface.co/Mapika/decider-2b-vision)

### litjev

**[LitJev](https://github.com/zhengxuyu/litjev)** · Media checked: 2026-09-28

Direct output-head scoring with optional temperature fitting. The configured Qwen default is recorded as the repository's declaration, not as an independent validation of every supported checkpoint or shared-state speedup.

**Multimodal scope:** The documented default is Qwen3.8-27B. Screenshot decisions require a vision checkpoint; plain text checkpoints do not become visual through the wrapper. Probabilities are uncalibrated by default.

**中文：** 文档默认 Qwen3.8-27B；截图决策必须使用视觉 checkpoint，普通文本模型不会因 wrapper 获得视觉能力。默认概率未校准。

**日本語：** 既定は Qwen3.8-27B。スクリーンショットには視覚 checkpoint が必要で、wrapper だけで text model は視覚化しない。既定確率は未校正。

[Primary source](https://github.com/zhengxuyu/litjev/blob/main/README.md) · [All evidence](evidence.md#litjev)

### reflex

**[reflex](https://github.com/kshetrajna12/reflex)** · Media checked: 2026-09-28

Current stable recipe is frozen 4B, two option orders, no adapter and no calibration file. Historical LoRA/distillation experiments do not mean the stable release is fine-tuned. A moving tag is not an immutable release.

**Multimodal scope:** The stable configuration uses frozen weights and two option orders. Earlier LoRA experiments are not its default release. A visual-capable checkpoint and actual image input are required.

**中文：** stable 配置使用冻结权重与两种候选顺序，早期 LoRA 实验不是当前默认版本；必须使用视觉 checkpoint 并实际输入图像。

**日本語：** stable は凍結重みと 2 種の候補順序。過去の LoRA 実験は既定版ではない。視覚 checkpoint と実際の画像入力が必要。

[Primary source](https://github.com/kshetrajna12/reflex/blob/main/README.md) · [All evidence](evidence.md#reflex)

### visual-jev-yu

**[Visual Jev (Yu & Yao)](https://github.com/guanxuyu-sv/Visual-Jev)** · Media checked: 2026-09-28

The recommended system uses answer-supervised LoRA and the existing LM head, not a new typed head or diffusion. The published 4B adapter and reproduction scripts are linked. Gains are concentrated on trained task families; batch-amortized speed is not single-request latency.

**Multimodal scope:** Choice quickstart supports 2–16 options. A matched typed-head control is experimental. No claim that SFT guarantees calibration.

**中文：** 快速示例支持 2–16 选项 Choice；独立 typed head 是实验对照，不是默认系统，SFT 不保证校准。

**日本語：** Quickstart は 2–16 候補の Choice。typed head は比較実験であり既定構成ではない。SFT は校正を保証しない。

[Primary source](https://github.com/guanxuyu-sv/Visual-Jev/blob/main/README.md) · [All evidence](evidence.md#visual-jev-yu)

[Reviewed media artifact](https://huggingface.co/guanxuyu/visual-jev-4b-answer-sft)

### valen

**[Valen](https://github.com/Liuziyu77/Valen)** · Media checked: 2026-09-28

Qwen vision-language model with a trainable decision head. The inspected RL implementation samples categorical actions, freezes old log-probabilities/rewards, uses a clipped group-relative surrogate, reference KL and direct Brier loss. It uses labelled targets and is not the proprietary TypeSafe algorithm.

**Multimodal scope:** Choice/Noul use one branch per question; Score evaluates each level separately. Preparing state once is not shared backbone encoding. Preview-0923 requires the Qwen3.5-2B base. General and Sokoban results use different checkpoints.

**中文：** Choice/Noul 每题一分支，Score 每等级独立前向；state 预处理复用不等于骨干共享。Preview-0923 仍需 Qwen3.5-2B 底座；通用与推箱子评测使用不同 checkpoint。

**日本語：** Choice/Noul は質問ごと、Score はレベルごとの forward。state 前処理の再利用は backbone 共有ではない。Preview-0923 は別途 Qwen3.5-2B を必要とし、汎用評価と倉庫番は異なる checkpoint。

[Primary source](https://github.com/Liuziyu77/Valen/blob/main/docs/technical.md) · [All evidence](evidence.md#valen)

[Reviewed media artifact](https://huggingface.co/Valen-Team/Valen-Preview-0923)

### omnijev

**[OmniJev (Qwen)](https://github.com/tinnel123666888/OmniJev)** · Media checked: 2026-09-28

The reviewed v1.1 family uses rank-32 LoRA, decision/ordinal heads and probability-scoring training followed by temperature calibration. No RLCD stage is documented in this recipe. Offline replay demonstrations are not validated closed-loop robot or game control.

**Multimodal scope:** Audio is represented visually, not passed to a native audio encoder. video_state constructs a 16-frame mosaic. Base weights must be downloaded separately. v1.1 aggregates use capped/unequal subsets and include withdrawn label-defect results; not a cross-model leaderboard.

**中文：** 音频以频谱图/波形图输入，不是原生音频编码器；video_state 生成 16 帧拼图。需另下底座。v1.1 汇总涉及截断及不等规模子集，部分标签缺陷结果已撤回，不能拼成统一排行榜。

**日本語：** 音声はスペクトログラム等の画像として入力。video_state は 16 フレームのモザイクを作る。基盤重みは別途必要。v1.1 の集計は上限付き・非等量の部分集合で、ラベル不備による撤回もある。

[Primary source](https://github.com/tinnel123666888/OmniJev/blob/14dbec4f71e194852c8d7b88ab36ef639493f400/README.md) · [All evidence](evidence.md#omnijev)

[Reviewed media artifact](https://huggingface.co/tinnel123/OmniJev)

### jev-spatial

**[Jev-Spatial](https://github.com/Fr0zenCrane/jev-spatial)** · Media checked: 2026-09-28

Spatial relations, numeric ranges and pointing share a LayerNorm/linear choice head. Numeric output takes two rounds; pointing takes three 3x3 decisions with crop refill. There is no generated answer text, but the complete task is not always one forward pass.

**Multimodal scope:** Pointing is a grid path, not direct continuous box regression. Against a shared-prefix AR baseline the 24-crop path can be slower; provisional RoboSpatial numbers are explicitly flagged by the author.

**中文：** 指点输出来自网格路径，不是连续 bbox 回归；对比同样共享前缀的 AR 基线，24-crop 路径可能更慢。作者明确标记 RoboSpatial 数字待核实。

**日本語：** Pointing はグリッド経路であり連続 bbox 回帰ではない。共有 prefix の AR 基準より 24-crop 経路が遅い場合がある。RoboSpatial の数値には作者の未検証注記がある。

[Primary source](https://github.com/Fr0zenCrane/jev-spatial/blob/main/README.md) · [All evidence](evidence.md#jev-spatial)

[Reviewed media artifact](https://huggingface.co/Fr0zencr4nE/jev-spatial)

### llm2jev

**[LLM2Jev](https://github.com/Yinsongxu/LLM2Jev)** · Media checked: 2026-09-28

Training-free local scorer with SGLang, Transformers and MLX backends. Text/image requests are supported; cache reuse is backend- and scheduling-dependent. It is an inspectable inference mechanism, not newly trained Jev weights.

**Multimodal scope:** September 22 documents multimodal support; September 23 adds MLX-VLM. These are version milestones, not first-public dates. Native probabilities are not a calibration guarantee.

**中文：** 9 月 22 日记录图文支持、23 日增加 MLX-VLM，均为版本进展而非首次发布日期。原生概率不保证校准。

**日本語：** 9 月 22 日に画像対応、23 日に MLX-VLM を記録。初回公開日ではなく機能更新。確率の直接出力だけでは校正を保証しない。

[Primary source](https://github.com/Yinsongxu/LLM2Jev/blob/main/README.md) · [All evidence](evidence.md#llm2jev)

### jev-visual-mlx

**[Jev Visual (MLX)](https://github.com/hr98w/jev-visual)** · Media checked: 2026-09-28

Frozen Qwen3.5 MLX visual scoring. Image/context prefill is reused by copied KV/recurrent state and batched question suffixes. There is no project-specific training or calibration; only the Qwen3.5 adapter is verified by the author.

**Multimodal scope:** Supports 1–64 questions and 2–26 options. Reused state is copied, not zero-copy. Simplified game demos and throughput measurements do not establish general game-playing quality.

**中文：** 支持 1–64 问题、2–26 候选。缓存是复制复用而非零拷贝；简化游戏演示和吞吐测试不代表通用游戏能力。

**日本語：** 1–64 質問、2–26 候補。キャッシュはコピーされ、zero-copy ではない。簡略化ゲームやスループット測定を汎用ゲーム能力と解釈しない。

[Primary source](https://github.com/hr98w/jev-visual/blob/main/README.md) · [All evidence](evidence.md#jev-visual-mlx)

### visual-jev-anderson

**[Visual Jev (Anderson)](https://github.com/andrueandersoncs/visual-jev)** · Media checked: 2026-09-28

Independent implementation, not the Yu/Yao paper. Documentation describes image-native packed isolated branches, language LoRA, a pointer head and held-out temperature fitting. A public promoted checkpoint was not verified; missing registry weights fail closed.

**Multimodal scope:** Treat it as an inspectable research implementation, not a verified downloadable release. The registry label is not release-date evidence. Candidate-token inference is a separate uncalibrated baseline.

**中文：** 作为可检查的研究实现收录，不声称已有可下载的正式模型。registry 名称不作为发布日期；候选 token 读出是单独未校准基线。

**日本語：** コードを調査可能な研究実装として収録し、取得可能な正式重みとは主張しない。registry 名は公開日の根拠にしない。token readout は別の未校正 baseline。

[Primary source](https://github.com/andrueandersoncs/visual-jev/blob/main/README.md) · [All evidence](evidence.md#visual-jev-anderson)

### openjev-multimodal

**[OpenJev Multimodal](https://github.com/jev-skills/openjev-multimodal)** · Media checked: 2026-09-28

Local llama.cpp/Metal decision engine with inspectable constrained-label readout. It generates one answer token per question, not zero tokens; Python constructs typed results. No new model training or RLCD is documented.

**Multimodal scope:** Supports complete candidate probabilities and image inputs. Audio and native video are explicitly unsupported. This row retains AR Decoding=Yes for its actual one-token path; no long prose/JSON decoding is implied.

**中文：** 支持完整候选概率及图像输入；明确不支持音频和原生视频。由于确实生成一个标签 token，AR Decoding 标为 Yes，但并不生成长文本或 JSON。

**日本語：** 画像と全候補確率に対応。音声・ネイティブ動画は明示的に非対応。1 ラベル token を生成するため AR Decoding=Yes とするが、長文や JSON 生成ではない。

[Primary source](https://github.com/jev-skills/openjev-multimodal/blob/main/README.md) · [All evidence](evidence.md#openjev-multimodal)

### jev-omni

**[Jev-Omni (Gemma)](https://huggingface.co/akhilaaa3/Jev-Omni)** · Media checked: 2026-09-28

HF-hosted inference code and weights; no canonical GitHub repository was verified. A finite slot head scores runtime options without text generation. The author reports a 30k-question fine-tune; the complete training recipe and RLCD attribution were not established.

**Multimodal scope:** Unlike OmniJev/Qwen, audio uses Gemma audio components, not spectrogram images. The inspected root conversion now loads unified BF16 weights plus head.pt, replacing the old FP32/separate-base path still described by some card text. 256 slots exist, but quality above 20 choices is not established.

**中文：** 不同于 Qwen OmniJev，音频使用 Gemma 音频组件而非频谱图。已核查的根目录迁移改为统一 BF16 权重加 head.pt；部分模型卡仍描述旧 FP32/另下底座路径。可容纳 256 槽位，不等于超过 20 候选也有可靠效果。

**日本語：** Qwen OmniJev と違い Gemma 音声コンポーネントを使用。確認した更新では root の統合 BF16 と head.pt を読み、旧 FP32/別 base 経路を置き換える。256 スロット対応でも 20 候補超の品質は未確立。

[Primary source](https://huggingface.co/akhilaaa3/Jev-Omni) · [All evidence](evidence.md#jev-omni)

[Reviewed media artifact](https://huggingface.co/akhilaaa3/Jev-Omni)

### groundingjev

**[GroundingJev (task-specific)](https://github.com/xyzzzh/GroundingJev)** · Media checked: 2026-09-28

Explicit Jev-inspired visual grounding, not a general typed probability model. An MLP reads the last valid hidden state and regresses normalized cxcywh. Training uses weighted L1/GIoU, first head adaptation then language/visual-merger/head tuning; other vision parameters stay frozen.

**Multimodal scope:** Dynamic Options and Native Probability are absent in this scoped path. Bbox accuracy and inference speed are author results, not directly comparable to Choice accuracy or calibrated probabilities.

**中文：** 当前路径没有 Dynamic Options 或 Native Probability。bbox 精度和速度是作者实验，不能与 Choice 准确率或校准概率直接比较。

**日本語：** この経路には Dynamic Options と Native Probability がない。bbox の精度・速度は作者の実験であり Choice 正答率や校正確率とは別の指標。

[Primary source](https://github.com/xyzzzh/GroundingJev/blob/main/README.md) · [All evidence](evidence.md#groundingjev)

[Reviewed media artifact](https://huggingface.co/xyzzzh/GroundingJev)

## Recent papers and systems

Dates here are arXiv v1 dates, not guessed first-public repository dates. Abstract-level evidence is distinguished from inspected repository material.

| arXiv v1 | Paper | Scope | Code / boundary |
|---|---|---|---|
| 2026-09-22 | [Visual Jev: Accurate and Efficient Decisions from Shared Visual Context](https://arxiv.org/abs/2609.25845) | Native-image decisions / shared context | [Author code](https://github.com/guanxuyu-sv/Visual-Jev); Existing LM-head readout with answer SFT and shared visual-prefix execution; the paper date does not establish earliest code publication. |
| 2026-09-24 | [From Text Decisions to Pixels: An Study of Jev-Style Visual Choice Model](https://arxiv.org/abs/2609.29283) | Native-image choice / adaptation / calibration | Author code not verified; Primary abstract reviewed. Frozen readout, language adaptation and calibration are separate controls. Author code not verified; the pixel-art repository with the same name is unrelated. |
| 2026-09-24 | [Jev-Mobile: Jev as an Executor for Mobile GUI Agents](https://arxiv.org/abs/2609.30186) | VLM planner + accessibility-tree decision executor | Author code not verified; Primary abstract reviewed. An agent system, not evidence that the Jev executor consumes raw screenshots. Canonical author code not verified. |
| 2026-09-24 | [Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](https://arxiv.org/abs/2609.30216) | Ecosystem study; not a model | Author code not verified; Primary abstract reviewed. Surveys the ecosystem using a September 22 GitHub snapshot; repository counts are not counts of independent decision models. |

## Name collisions and inclusion boundaries

- **Visual Jev is not a unique project name.** The Guanxu Yu/Yuhang Yao paper uses `guanxuyu-sv/Visual-Jev`; `andrueandersoncs/visual-jev` is an independent pointer-head implementation; `hr98w/jev-visual` is a frozen MLX implementation. They are not interchangeable releases.

- **OmniJev is not Jev-Omni.** The Qwen-based `tinnel123666888/OmniJev` and the Gemma-based `akhilaaa3/Jev-Omni` are different projects. The latter currently has verified HF-hosted inference code and weights, not a verified canonical GitHub repository. Its Stars cell is therefore a dash, not HF likes or an unrelated repository count.

- **PixelJev paper versus pixel-art app.** The [PixelJev paper](https://arxiv.org/abs/2609.29283) is about native-image choice prediction. [joce-unity/pixeljev](https://github.com/joce-unity/pixeljev) instead calls hosted Jev to select pixel-art shape attributes. That app is not the paper code and is not added as a separate decision backbone.

- **GroundingJev is task-specific.** It predicts continuous boxes rather than a distribution over runtime options. It is included as explicit Jev-inspired model research, with Dynamic Options and Native Probability marked absent; it is not a generic Noul/Choice/Score substitute.

- **Jev-Mobile is a system.** Its VLM planner plus accessibility-tree executor does not establish pixel input to the Jev executor. It remains related research, not a new multimodal Jev checkpoint.

- These third-party implementations do not reveal TypeSafe Jev's undisclosed architecture. Neither a diffusion-based community implementation nor a visual demo proves that the official model is diffusion or natively multimodal.

## Evaluation requirements

Use matched inputs, candidates, model versions, image resolution and hardware. Report single-request latency separately from batch-amortized time; include visual encoding and cache warm/cold costs. Replays, scripted candidate shortlists and cropped-image rounds must be disclosed. Test image removal/shuffling, wrong-image controls, blur, unseen questions/options and distribution shift; do not infer calibration from a confidence drop in one blur demo. Report accuracy, NLL/Brier, calibration and risk-coverage separately. Regional choices, pointing hit-rate and continuous-box IoU are not interchangeable metrics.

## Remaining gaps

Most first-public repository dates remain unverified; later papers, checkpoint labels and repository creation times are not substitutes. The HF Jev-Omni checkpoint is inspectable, but a complete reproducible training recipe and RLCD attribution were not established. This review inspected selected source blocks and author documentation; no upstream training, GPU inference or benchmark was rerun. Older rows without a media record were not exhaustively re-audited.
