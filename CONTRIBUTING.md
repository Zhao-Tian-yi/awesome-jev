# Contributing to Awesome Jev

Thanks for helping maintain this list.

## Scope

This repository focuses on **open-source Jev-like / System One decision models and training methods**.

Please do **not** submit:
- ordinary applications that only call the TypeSafe API;
- generic classifiers or rerankers with no Jev/System-One connection;
- wrappers that add no inspectable model, architecture, training, inference, or calibration contribution.

## Required fields

For a new model or implementation, please provide:

- **Project name**
- **Repository URL**
- **Backbone**
- **Architecture**
- **Training** — none / head-only / LoRA / full fine-tuning / from scratch
- **AR status** — causal AR / encoder / diffusion / hybrid
- **Output mechanism** — token logits / pointer head / candidate scorer / decision slot / other
- **RLCD status**
  - `RLCD-RL`: explicit sampled actions or rollouts + reward + policy-gradient-style optimization
  - `RLCD prototype`: experimental RLCD stage exists but is not the primary released model
  - `Calibration-only`: CE/Brier/temperature scaling/etc.; useful, but not RL
  - `None`
- **Calibration method**
- **Evidence** — README, code path, model card, training script, or technical note supporting the classification

## Evidence standard

Prefer claims directly supported by:
1. source code,
2. model cards,
3. training scripts,
4. project documentation,
5. reproducible evaluation artifacts.

Avoid inferring hidden architecture from branding alone.

In particular, TypeSafe has not publicly released the full Jev architecture or proprietary RLCD algorithm. Do not label a method as a reproduction of TypeSafe RLCD unless that claim is explicitly supportable.

## Pull request format

Please keep descriptions concise and factual.

Example:

```md
| Project | Backbone | Architecture | Train? | AR? | Output | RLCD | Calibration |
|---|---|---|---:|:---:|---|---|---|
| ExampleJev | Qwen-X | shared-state pointer head | LoRA + head | ✅ | candidate softmax | ❌ | temperature scaling |
```

If a project spans multiple architecture families, describe the default/released path and add a note.
