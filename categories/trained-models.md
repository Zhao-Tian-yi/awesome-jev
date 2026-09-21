# Trained Jev-like Decision Models

These projects explicitly train a model or decision head for runtime-defined semantic decisions.

## Causal / AR-backbone models

- [Kev](https://github.com/jaredpalmer/kev) — Qwen + LoRA + pointer head; shared state with isolated question branches.
- [NanoJev](https://github.com/TianyuCodings/NanoJev) — Qwen3-0.6B + typed dynamic decision heads.
- [Luce](https://github.com/scienthoon/luce) — teacher-generated training data + LoRA + decision head.
- [JevForge](https://github.com/zwliJay/jev-forge) — Qwen3.5-0.8B end-to-end training/evaluation stack.
- [decider](https://github.com/Mapika/decider) — Qwen3.5 runtime answer slots and direct label projection.

## Encoder / non-autoregressive models

- [Laya](https://github.com/NandhaKishorM/laya) — ModernBERT/mmBERT typed decision model.
- [Von](https://github.com/wfzyx/von) — bidirectional encoder + typed probability heads.
- [Verdict](https://github.com/Heman10x-NGU/Verdict-open-jev) — ModernBERT/GLiClass label scoring.
- [jevlike](https://github.com/vinnylarouge/jevlike) — option-as-query cross-attention scorer.
- [jevbetter](https://github.com/olanotolu/jevbetter) — lightweight rival-aware candidate scorer.
- [minojev](https://github.com/zeredy879/minojev) — very small custom Transformer trained from scratch.
