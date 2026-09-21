# Diffusion Jev-like Models

Diffusion language models are especially interesting for System-One decisions because multiple unknown decision slots can be evaluated in parallel rather than generated left-to-right.

## OpenJev / DiffusionGemma

- Repository: [razorback16/openjev](https://github.com/razorback16/openjev)
- Backbone: **DiffusionGemma 26B-A4B**
- Training: no Jev-specific model training in the baseline
- Mechanism: insert one masked/noisy answer slot per question and directly read the probability distribution over allowed label tokens.

Conceptually:

```
q1: [MASK]   q2: [MASK]   q3: [MASK]
      ↓            ↓            ↓
   P(y1)         P(y2)         P(y3)
```

The implementation supports one or several denoising/read steps and can average repeated noisy reads.

## Why this category matters

A diffusion decision model offers a different architectural hypothesis from causal shared-prefix models:

- no left-to-right answer decoding;
- naturally parallel answer slots;
- bidirectional context;
- possible adaptive one-step/few-step decision inference.

A major open research direction is to move from **zero-shot diffusion slot readout** to a model explicitly post-trained for:
- dynamic candidate scoring,
- calibrated probabilities,
- parallel question isolation,
- RLCD-style optimization.
