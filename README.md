# Awesome Jev / System One Decision Models

A curated list of **open-source Jev-like / System One decision models**, architectures, training recipes, calibration methods, and reproducible implementations.

> **Scope.** This repository focuses on models that implement or study the core Jev-style interface:
>
> `state + runtime-defined question + candidates → typed probability distribution`
>
> It does **not** attempt to catalog every application that merely calls the TypeSafe API.

## Why this list?

Jev reframes many small software and agent decisions as direct probabilistic judgments rather than autoregressive text generation. The open-source ecosystem is evolving quickly, but projects differ substantially in architecture:

- frozen AR LLM + direct option-logit readout;
- shared-state / parallel-branch causal models;
- dedicated encoder / pointer-head decision models;
- diffusion LMs with masked decision slots;
- calibration-only post-training;
- genuine reinforcement learning for calibrated decisions.

This list tries to keep those distinctions explicit.

## RLCD terminology used here

TypeSafe has publicly named **RLCD — Reinforcement Learning for Calibrated Decisions**, but its exact proprietary algorithm has not been released.

To avoid conflating different methods, this repository uses:

- **RLCD-RL ✅** — explicit sampling/rollout + reward + policy-gradient style optimization.
- **RLCD prototype 🟡** — an experimental RLCD-style stage exists, but it is not the main released training recipe.
- **Calibration-only ⚠️** — CE/Brier/temperature-scaling or other directly differentiable calibration objectives; useful, but not reinforcement learning.
- **None ❌** — no RLCD-style training reported.

## Comparison

| Project | Backbone | Architecture | Train? | AR? | Output | RLCD | Calibration | Notes |
|---|---|---|---:|:---:|---|---|---|---|
| [SemIf](https://github.com/TheoLeeCJ/SemIf) | Qwen3.5-4B, MiniCPM5-2B, Qwen3 | Frozen LM; direct final-position option-token logits; shared-state KV cache + parallel suffix branches | ❌ | ✅ | Next-token candidate logits | ❌ | Explicitly uncalibrated decision probabilities | Strong zero-training baseline |
| [OpenJev / DiffusionGemma](https://github.com/razorback16/openjev) | DiffusionGemma 26B-A4B | Diffusion canvas with masked answer slots; one/few-step parallel readout | ❌ | ❌ | Masked decision-slot distributions | ❌ | Entropy-triggered rereads / sample averaging | Strong diffusion baseline |
| [Kev](https://github.com/jaredpalmer/kev) | Qwen3.5 0.8B / 4B / 9B | LoRA + pointer head; shared state; isolated question branches; dynamic option scoring | ✅ | ✅ | Pointer-head probabilities | ❌ | Calibration/eval utilities | Strong trained causal baseline |
| [NanoJev](https://github.com/TianyuCodings/NanoJev) | Qwen3-0.6B | Shared typed decision heads; Choice uses candidate scoring / set interaction | ✅ | ✅ | Dynamic decision heads | 🟡 | CE/Brier-style calibration + RLCD pilot | Full data→train→serve pipeline |
| [jevlike](https://github.com/vinnylarouge/jevlike) | Tiny byte encoder or frozen HF encoder | Each option acts as query → attends context → shared scorer → softmax | ✅ | Encoder | Option-attention head | ❌ | ECE evaluation | Clean dynamic-candidate baseline |
| [Laya](https://github.com/NandhaKishorM/laya) | ModernBERT / mmBERT | Bidirectional encoder + typed decision head | ✅ | ❌ | Single-pass typed probabilities | ✅ RLCD-RL | Proper-scoring-rule reward + fitting | Important open RLCD reference |
| [Von](https://github.com/wfzyx/von) | Bidirectional encoder | Encoder + option-marker / decision head | ✅ | ❌ | Typed option probabilities | ⚠️ Calibration-only | CE + Brier + temperature scaling | Project uses RLCD terminology, but public recipe is not policy-gradient RL |
| [decider](https://github.com/Mapika/decider) | Qwen3.5-2B | Runtime answer slots + direct label projection; shared-state caching | ✅ | Hybrid | One-pass typed slots | ❌ | Proper scoring / temperature fitting | Mature engineering reference |
| [mini-jev](https://github.com/r-ms/mini-jev) | Qwen3-4B-Instruct | Frozen LLM; direct A/B/C… token logits; shared prefix | ❌ | ✅ | Option-token logits | ❌ | Not claimed calibrated | Simple mechanism baseline |
| [LitJev](https://github.com/zhengxuyu/litjev) | Qwen family | Off-the-shelf Qwen + direct output-head scoring + shared prefill | ❌ | ✅ | Direct label logits | ❌ | Optional temperature fit | Training-free local Jev-style server |
| [openjev](https://github.com/zhihz/openjev) | Qwen3-4B-Instruct | Frozen LLM; per-question candidate-letter logits | ❌ | ✅ | Candidate logits | ❌ | Probability / robustness evaluation | Bilingual experimental implementation |
| [open-jev](https://github.com/daseinlabs/open-jev) | Gemma 3 4B | Shared prefill + expanded KV cache + option likelihood; optional trainable scoring head | Optional | ✅ | Sequence log-prob / scoring head | ❌ | ECE / trainable head | Useful candidate-scoring reference |
| [reflex](https://github.com/kshetrajna12/reflex) | Qwen family | Shared state cache + independent question branches + label logits | Mostly no | ✅ | Label logits | ❌ | Temperature fitting | Fast branch-scoring implementation |
| [Verdict / OpenJev](https://github.com/Heman10x-NGU/Verdict-open-jev) | ModernBERT-base + GLiClass | Bidirectional joint/bi-encoder label scoring | ✅ | ❌ | Candidate similarity → softmax | ⚠️ Calibration-only | Brier + temperature scaling | Strong encoder-style alternative |
| [eve-rlcd](https://github.com/anthony-maio/eve-rlcd) | Qwen3-0.6B-Base | Shared-state prefill + categorical label policy | ✅ SFT→RL | ✅ | Label-token policy | ✅ RLCD-RL | Proper-scoring reward | Important bandit-style RLCD implementation |
| [minojev](https://github.com/zeredy879/minojev) | Small custom Transformer | Runtime-defined candidate scorer trained from scratch | ✅ | Transformer | Typed distributions | ❌ | Per-primitive temperature | Minimal-scale reference |
| [Luce](https://github.com/scienthoon/luce) | Qwen3-4B-Base | Teacher-synthesized data + LoRA + decision head | ✅ | ✅ | One-pass Choice / Score / Boolean | ❌ | ECE / post-hoc calibration | Practical low-cost recipe |
| [poorjev](https://github.com/rupeshpoojary9/poorjev) | Zero-shot NLI encoders | Candidate-wise entailment scoring → typed distribution | Minimal | ❌ | NLI candidate probabilities | ❌ | Temperature + conformal abstention | Good calibration baseline |
| [jevbetter](https://github.com/olanotolu/jevbetter) | Lightweight custom encoder | Hashed n-gram encoder + rival-aware attention + gated scorer | ✅ | ❌ | Variable-option scorer | ❌ | Temperature scaling | Lightweight baseline |
| [JevForge](https://github.com/zwliJay/jev-forge) | Qwen3.5-0.8B | Jev-style decision training + OOD eval + local serving | ✅ | ✅ | Structured decision head | 🟡 | Calibration pipeline | Research-oriented end-to-end stack |
| [system-one-open](https://github.com/mithalouni/system-one-open) | Gemma family | Slot-logit scorer + candidate chunking | ✅ | Backbone-dependent | Slot logits | ⚠️ Calibration-only | CE + Brier + temperature scaling | Trained slot-style baseline |

## Architecture families

### 1. Inference-only AR readout

These methods keep an autoregressive LLM frozen but **do not decode an answer**. They read candidate-token logits directly:

- [SemIf](https://github.com/TheoLeeCJ/SemIf)
- [mini-jev](https://github.com/r-ms/mini-jev)
- [LitJev](https://github.com/zhengxuyu/litjev)
- [openjev](https://github.com/zhihz/openjev)
- [reflex](https://github.com/kshetrajna12/reflex)

Typical abstraction:

```
state → shared prefill / KV
            ├─ question 1 → option logits
            ├─ question 2 → option logits
            └─ question N → option logits
```

### 2. Trained causal decision models

These retain a causal/AR backbone but train a dedicated decision mechanism:

- [Kev](https://github.com/jaredpalmer/kev)
- [NanoJev](https://github.com/TianyuCodings/NanoJev)
- [Luce](https://github.com/scienthoon/luce)
- [JevForge](https://github.com/zwliJay/jev-forge)

### 3. Encoder / non-autoregressive decision models

These treat Jev-style prediction as a discriminative semantic-decision problem:

- [Laya](https://github.com/NandhaKishorM/laya)
- [Von](https://github.com/wfzyx/von)
- [Verdict](https://github.com/Heman10x-NGU/Verdict-open-jev)
- [jevlike](https://github.com/vinnylarouge/jevlike)
- [jevbetter](https://github.com/olanotolu/jevbetter)
- [poorjev](https://github.com/rupeshpoojary9/poorjev)

### 4. Diffusion decision models

The clearest open example so far is:

- [OpenJev / DiffusionGemma](https://github.com/razorback16/openjev)

It uses diffusion-LM answer slots instead of left-to-right answer generation:

```
q1: [MASK]   q2: [MASK]   q3: [MASK]
      ↓            ↓            ↓
   P(y1)         P(y2)         P(y3)
```

This is especially relevant to the hypothesis that System One models may benefit from masked/bidirectional representations and massively parallel decision readout.

### 5. RLCD / calibration research

- [eve-rlcd](https://github.com/anthony-maio/eve-rlcd) — explicit action sampling + proper-scoring reward + policy-gradient style training.
- [Laya](https://github.com/NandhaKishorM/laya) — reports proper-scoring-rule rewards with GRPO-style optimization.
- [NanoJev](https://github.com/TianyuCodings/NanoJev) — RLCD-style prototype/roadmap work.
- [Von](https://github.com/wfzyx/von) and [Verdict](https://github.com/Heman10x-NGU/Verdict-open-jev) — useful calibration objectives, but public recipes are closer to CE+Brier than to reinforcement learning.

## Official TypeSafe resources

- [TypeSafe](https://typesafe.ai/)
- [Jev launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- [TypeSafe documentation](https://docs.typesafe.ai/)
- [TypeSafe GitHub organization](https://github.com/typesafe-ai)
- [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python)
- [JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js)
- [System One adapter](https://github.com/typesafe-ai/system-one-adapter-python)
- [Agent skills](https://github.com/typesafe-ai/skills)
- [TypeSafe's public LLaDA fork](https://github.com/typesafe-ai/LLaDA)

## What counts as a Jev-like model here?

A project should satisfy most of the following:

1. Takes unstructured or semi-structured **state**.
2. Accepts a runtime-defined **question / criterion**.
3. Supports runtime-defined **candidate answers**, Boolean judgments, or ordered score levels.
4. Returns a **probability distribution or calibrated score**, not only generated prose.
5. Avoids or substantially reduces ordinary autoregressive answer decoding.
6. Is open source or provides enough public code to inspect the mechanism.

## Contributing

PRs are welcome. Please include:

- repository URL;
- backbone;
- architecture;
- whether any parameters are trained;
- AR / encoder / diffusion status;
- decision readout mechanism;
- calibration method;
- whether RLCD is genuine RL, a prototype, or calibration-only.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

This is an independent community resource and is **not affiliated with TypeSafe AI**.  
“Jev”, “TypeSafe”, and related marks belong to their respective owners.

Architecture descriptions reflect public repositories and documentation and may change as projects evolve. TypeSafe has not publicly disclosed Jev's full internal architecture or RLCD algorithm.
