# RLCD and Calibration Research

TypeSafe publicly uses the name **RLCD — Reinforcement Learning for Calibrated Decisions**, but has not released the exact proprietary training algorithm.

This page therefore distinguishes genuine RL from calibration losses.

## RLCD-RL

### eve-rlcd
- Repository: [anthony-maio/eve-rlcd](https://github.com/anthony-maio/eve-rlcd)
- Backbone: Qwen3-0.6B-Base
- Pattern: SFT → sampled categorical decision → proper-scoring reward → policy-gradient update
- Why it matters: one of the clearest public implementations of literal reinforcement learning for calibrated decisions.

### Laya
- Repository: [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
- Backbone: ModernBERT/mmBERT family
- Public description: proper-scoring-rule rewards with GRPO-style optimization.
- Also uses post-hoc probability calibration.

## RLCD prototypes

### NanoJev
- Repository: [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev)
- Primary released training remains supervised decision training.
- RLCD-style / proper-reward work is experimental / roadmap-level in the public project.

### JevForge
- Repository: [zwliJay/jev-forge](https://github.com/zwliJay/jev-forge)
- Includes a preliminary RLCD-style baseline in a broader Qwen3.5 training stack.

## Calibration-only objectives

These are useful for probability quality but should not be confused with reinforcement learning:

- [Von](https://github.com/wfzyx/von) — CE + Brier + temperature scaling.
- [Verdict](https://github.com/Heman10x-NGU/Verdict-open-jev) — Brier-style calibration + temperature scaling.
- [system-one-open](https://github.com/mithalouni/system-one-open) — CE/Brier-style training and temperature scaling.

## Recommended metrics

For Jev-like models, accuracy alone is insufficient. Useful metrics include:

- NLL
- Brier score
- ECE / ACE
- reliability diagrams
- AURC
- accuracy@coverage
- calibration under distribution shift
- option-order robustness
- paraphrase consistency
