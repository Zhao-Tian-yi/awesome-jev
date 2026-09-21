# Inference-only Jev-like Models

These projects reuse a pretrained model without training a dedicated Jev-style model.

## Common pattern

```
state → prefill / representation
          ├─ question → candidate logits
          ├─ question → candidate logits
          └─ question → candidate logits
```

The key idea is to **avoid autoregressive answer generation** and read decision probabilities directly.

## Projects

- [SemIf](https://github.com/TheoLeeCJ/SemIf) — frozen Qwen/MiniCPM; direct final-position option logits; shared-state KV reuse.
- [mini-jev](https://github.com/r-ms/mini-jev) — frozen Qwen; A/B/C label-token readout.
- [LitJev](https://github.com/zhengxuyu/litjev) — training-free Qwen decision server with direct label scoring.
- [openjev](https://github.com/zhihz/openjev) — frozen Qwen candidate-letter scoring.
- [reflex](https://github.com/kshetrajna12/reflex) — shared state cache plus independent question branches.
- [open-jev](https://github.com/daseinlabs/open-jev) — shared prefill and option continuation likelihood; optional trainable head.

## Strengths

- no or very little training;
- inherits pretrained LLM semantics;
- easy to reproduce;
- strong latency baseline.

## Limitations

- candidate probabilities are not automatically calibrated;
- answer-token verbalizers and option order can matter;
- causal backbones may still need branch-specific suffix computation.
