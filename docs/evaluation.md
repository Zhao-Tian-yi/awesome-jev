# Evaluation protocol

[Home](../README.md) · [Training and Calibration](training.md)

This page proposes a reporting protocol; it does not report newly run model
benchmarks. Upstream numbers were not rerun during this repository audit.

| Dimension | Report | Controls |
|---|---|---|
| Task performance | Accuracy, macro F1, AUROC when meaningful | Majority/random and same-backbone direct-logit baselines |
| Probability quality | NLL, Brier, ECE, reliability diagram | Binning, zero handling, calibration split, scalar/vector conventions |
| Selective prediction | Risk-coverage, AURC, accuracy at stated coverage | Tune thresholds without test labels; report retained sample count |
| Runtime generalization | Unseen questions/options/descriptions/domains | Split by source, customer, page or episode, not just individual rows |
| Option robustness | Permutations, paraphrases, distractors, candidate coverage | Align distributions by semantic IDs, not label-token positions |
| High cardinality | 2, 5, 10, 50, 100, 255 options where supported | Report refusals, chunking and extra rounds; do not hide unsupported K |
| Efficiency | Latency p50/p95, throughput, memory, FLOPs if measured | Hardware, dtype, batch, question/option counts, input lengths, warm/cold path |
| Parallel semantics | Packed vs separate, shared-prefix vs fresh | Compare probabilities; distinguish numerical changes from information leakage |

Keep supervised in-domain specialization separate from zero-shot general-purpose
performance. A small task-specific model outperforming Jev on its training-domain
games is not a general architecture comparison. Never combine unmatched slices,
reference-agreement metrics and hard-label accuracy into one leaderboard number.

## Readout controls

Compare the same prompt and backbone when isolating the effect of readout. A
400-token generated explanation is not a fair latency comparator for a one-label
answer unless that difference is the task being studied. Record any changes in
argmax between readout paths. The
[SemIf method](https://github.com/TheoLeeCJ/SemIf/blob/master/docs/METHOD.md) and
[mini-Jev study](https://github.com/r-ms/mini-jev) document such distinctions.

“Zero output tokens” need not mean zero expensive computation. One shared request
may require a prefill, cache duplication, batched suffix forwards, candidate
chunks, denoising iterations, or repeats. API billing counters may count serialized
responses or scored candidate tokens, rather than sampled tokens.

## Probability semantics

A Choice distribution compares mutually exclusive supplied alternatives. It is not
necessarily a vector of independent action-success probabilities. A Noul forecasts
a defined binary condition. An ordered Score can return an expected level, which
is different from a most-likely label or a normalized 0–1 score; verify the project's
contract. Neither entropy concentration nor an option margin is automatically
P(correct). The [official skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md)
warns that typed output guarantees the interface, not truth.

## Useful inspectable artifacts

| Source | Use | Limitation |
|---|---|---|
| [SemIf benchmark bundle](https://github.com/TheoLeeCJ/SemIf/tree/master/benchmarks) | Frozen fixtures, selection IDs, readout and systems experiments | Selected public TypeSafe rows are not the full vendor aggregate |
| [mini-Jev](https://github.com/r-ms/mini-jev) | Preregistered letter-readout versus constrained generation | Scope is the documented model and task population |
| [NanoJev probability experiment](https://github.com/TianyuCodings/NanoJev/blob/618cea6d906d54e128360786d12f703fff2b1245/docs/RLCD_EXPERIMENT.md) | Direct CE/Brier versus sampled gradient controls | Narrow event families and limited seeds |
| [eve-rlcd](https://github.com/anthony-maio/eve-rlcd) | Bandit feedback, reward ablations, dataset release | Different RLVR learning rates and in-distribution evaluation require qualification |
| [TypeSafe evaluations](https://evals.typesafe.ai/) | Vendor comparison resource | Endpoint contents and full protocol not re-verified in this audit |
