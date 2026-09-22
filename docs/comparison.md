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
| [decider](evidence.md#decider) | Unknown | Qwen3.5 family | 0.8B / 2B / 34.7B total, 3B active | Hybrid + Decision Head | Multi-stage | RLCR-like | No | Label-token projection | N/C/S | Yes |
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
<!-- properties:end -->
