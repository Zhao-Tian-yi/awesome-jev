# Full technical comparison

[Home](../README.md) · [Evidence](evidence.md) · [Training audit](training.md)

All fields are retained from the audited YAML. AR Decoding refers to token-by-token answer generation, not the backbone. Project Weights excludes reused upstream weights. Unknown dates remain unknown.

| Project | First Public | Backbone | Params | Architecture | Training | RL / RLCD | AR Decoding | Decision Mechanism | Outputs | Project Weights |
|---|---|---|---|---|---|---|---|---|---|---|
| [Official Jev](evidence.md#official-jev) | Unknown | Not disclosed | Not disclosed | Custom / Not Disclosed | Not disclosed | RLCD | No | Not disclosed | N/C/S | API only |
| [SemIf](evidence.md#semif) | Unknown | Qwen3.5 / MiniCPM5 / Qwen3 | 0.6B / 2B / 4B | AR LLM | None | No | No | Next-token logits | C/B/P | No |
| [OpenJev / DiffusionGemma](evidence.md#openjev-diffusiongemma) | Unknown | DiffusionGemma 26B-A4B | 26B total / approximately 4B active | Diffusion / Masked | None | No | No | Masked decision slots | N/C/S | No |
| [Kev](evidence.md#kev) | Unknown | Qwen3.5; earlier Qwen3 | 0.8B / 4B / 9B | AR LLM + Pointer Head | LoRA + Decision Head | No | No | Pointer head | N/C/S | Partial |
| [NanoJev](evidence.md#nanojev) | Unknown | Qwen3-0.6B | 0.6B + heads | AR LLM + Decision Head | SFT; RL prototype | RLCD (claimed) | No | Option-wise scoring | C/B/S | Yes |
| [jevlike](evidence.md#jevlike) | Unknown | Custom / frozen HF encoder | Configuration-dependent | Option Scorer | Head-only / from scratch | No | No | Option-wise scoring | C/P | Partial |
| [Laya](evidence.md#laya) | Unknown | ModernBERT / mmBERT | 421M / 322M (author-reported) | Encoder-based | Full FT + RL | RLCD (claimed) | No | Option-marker head | N/C/S | Yes |
| [Von](evidence.md#von) | Unknown | ModernBERT variants | 395M (OptionMarker; author-reported) | Encoder-based / Cross-Encoder | Calibration Training | No | No | Option-marker / NLI | N/C/S | Partial |
| [decider](evidence.md#decider) | Unknown | Qwen3.5 family | 0.8B / 2B / 4B / 34.7B total, 3B active (MoE) | Hybrid + Decision Head | Multi-stage | RLCR-like | No | Label-token projection | N/C/S | Yes |
| [mini-Jev](evidence.md#mini-jev) | Unknown | Qwen3-4B-Instruct-2507 | 4B | AR LLM | None | No | No | Next-token logits / Verbalizer | C/B | No |
| [LitJev](evidence.md#litjev) | Unknown | Qwen family | 27B default; configurable | AR LLM | None | No | No | Next-token logits | N/C/S | No |
| [Open JEV (zhihz)](evidence.md#zhihz-openjev) | Unknown | Qwen3-4B-Instruct-2507 | 4B | AR LLM | None | No | No | Next-token logits / Verbalizer | C/B | No |
| [open-jev (daseinlabs)](evidence.md#dasein-openjev) | Unknown | Gemma 3 4B | 4B + optional head | AR LLM / Option Scorer | None / Head-only | No | No | Option likelihood / head | N/C/S | No |
| [reflex](evidence.md#reflex) | Unknown | Qwen3.5-4B (stable) | 4B default | AR LLM | None | No | No | Next-token logits | N/C/S | No |
| [Verdict / OpenJev](evidence.md#verdict) | Unknown | ModernBERT-base + GLiClass | 151M (author-reported) | Encoder-based | Calibration Training | No | No | Joint label / context scoring head | N/C/S | Yes |
| [eve-rlcd](evidence.md#eve-rlcd) | Unknown | Qwen3-0.6B-Base | 0.6B | AR LLM | SFT + RL | RLCD (claimed) | No | Next-token logits / Verbalizer | N/C/S | Yes |
| [minojev](evidence.md#minojev) | Unknown | Qwen3-1.7B | 1.7B + approximately 0.8M head | AR LLM + Decision Head | Head-only | No | No | Option-wise scoring | C/B/S | Partial |
| [Luce](evidence.md#luce) | Unknown | Qwen3 / Qwen2.5 | 4B default | AR LLM + Decision Head | Distillation + LoRA + Head | No | No | Decision Head / Verbalizer | N/C/S | Unknown |
| [poorjev](evidence.md#poorjev) | Unknown | Zero-shot NLI encoders | Configuration-dependent | Cross-Encoder | Calibration Training | No | No | NLI option-wise scoring | N/C/S | No |
| [jevbetter](evidence.md#jevbetter) | Unknown | Custom / frozen HF encoder | Configuration-dependent | Option Scorer | SFT / Head-only | No | No | Option-wise scoring | C/R/P | Unknown |
| [JevForge](evidence.md#jevforge) | Unknown | Qwen3.5-0.8B / Qwen3-0.6B | 0.8B + scorer | AR LLM + Decision Head | SFT; RL prototype | RLCD (claimed) | No | Option-wise scoring | N/C/S | Yes |
| [System One Open](evidence.md#system-one-open) | Unknown | Gemma 4 E2B / Gemma 3 270M | E2B (vendor label) / 270M | AR LLM + Decision Head | LoRA / SFT | No | No | Label-token slots | N/C/S | No |
| [Visual Jev (Yu & Yao)](evidence.md#visual-jev-yu) | Unknown | Qwen3-VL | 4B / 8B | AR VLM | LoRA / answer SFT | No | No | Existing LM-head candidate-token logits | C/P | Partial |
| [Valen](evidence.md#valen) | Unknown | Qwen3.5 | 0.8B / 2B + decision head | Hybrid VLM + Decision Head | SFT + experimental RL | RLCD (claimed) | No | Shared candidate head; separate ordinal-level branches | N/C/S | Partial |
| [OmniJev (Qwen)](evidence.md#omnijev) | Unknown | Qwen3.5 | 0.8B / 2B / 4B | Hybrid VLM + Decision/ordinal heads | LoRA + Calibration Training | No | No | Typed decision heads; prefix branches | N/C/S | Partial |
| [Jev-Spatial](evidence.md#jev-spatial) | Unknown | Molmo2-ER | Not separately verified | AR VLM + Decision Head | LoRA + Decision Head | No | No | Unified choice head; hierarchical scalar/point decisions | C/Reg | Yes |
| [LLM2Jev](evidence.md#llm2jev) | Unknown | Configurable LLM / VLM (Qwen examples) | Configuration-dependent | AR/Hybrid VLM / Option Scorer | None | No | No | Candidate binary scoring from prefill logits | N/C/S | No |
| [Jev Visual (MLX)](evidence.md#jev-visual-mlx) | Unknown | Qwen3.5-0.8B | 0.8B; documented 4-bit path | Hybrid VLM / Option Scorer | None | No | No | Candidate-label / sequence logits | N/C/S | No |
| [Visual Jev (Anderson)](evidence.md#visual-jev-anderson) | Unknown | Qwen3-VL | Size depends on registry checkpoint | AR VLM + Pointer Head | LoRA + Decision Head + Calibration Training | No | No | Learned option pointer head | N/C/S | Unknown |
| [OpenJev Multimodal](evidence.md#openjev-multimodal) | Unknown | Qwen VLM family via llama.cpp | 0.8B / 4B default profiles; larger optional | AR/Hybrid VLM | None | No | Yes | One generated label token + candidate probabilities | N/C/S | No |
| [Jev-Omni (Gemma)](evidence.md#jev-omni) | Unknown | Gemma 4 12B IT | 12B + 256-slot head | Multimodal Backbone + Classification Head | Fine-tuning (author reported) | Unknown | No | Last-hidden-state 256-slot classifier | C/P | Yes |
| [GroundingJev (task-specific)](evidence.md#groundingjev) | Unknown | Qwen3.5-0.8B | 0.8B + regression head | Hybrid VLM + Regression Head | Head-only then joint SFT | No | No | Continuous normalized bounding-box regression | Reg | Yes |

## Jev-like capability matrix

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
| [Visual Jev (Yu & Yao)](https://github.com/guanxuyu-sv/Visual-Jev) | ✅ | ✅ | ✅ | ✅ | ? | ✅ | ✅ | ⚠️ | ✅ |
| [Valen](https://github.com/Liuziyu77/Valen) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ✅ | ⚠️ | ✅ |
| [OmniJev (Qwen)](https://github.com/tinnel123666888/OmniJev) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ |
| [Jev-Spatial](https://github.com/Fr0zenCrane/jev-spatial) | ✅ | ✅ | ✅ | ⚠️ | ? | ✅ | ✅ | ⚠️ | ✅ |
| [LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) | ✅ | ✅ | ✅ | ✅ | ? | ⚠️ | ✅ | ⚠️ | ✅ |
| [Jev Visual (MLX)](https://github.com/hr98w/jev-visual) | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ⚠️ | ✅ |
| [Visual Jev (Anderson)](https://github.com/andrueandersoncs/visual-jev) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ |
| [OpenJev Multimodal](https://github.com/jev-skills/openjev-multimodal) | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ | ✅ | ❌ | ❌ |
| [Jev-Omni (Gemma)](https://huggingface.co/akhilaaa3/Jev-Omni) | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ | ❌ | ✅ |
| [GroundingJev (task-specific)](https://github.com/xyzzzh/GroundingJev) | ✅ | ❌ | ❌ | ❌ | ❌ | ? | ❌ | ❌ | ✅ |
<!-- properties:end -->
