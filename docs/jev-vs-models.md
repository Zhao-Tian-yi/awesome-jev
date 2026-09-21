# Jev and adjacent model families

[Home](../README.md) · [Architecture](architecture.md)

Jev is a product/interface reference here, not an identified neural architecture.
The comparisons below explain distinctions, not a claim that any existing family
is incapable of implementing typed decisions.

| Comparison | Useful distinction | Boundary |
|---|---|---|
| BERT / encoder | Representation learning versus an interface for runtime questions and candidates | Encoders can learn dynamic label scorers; they are not inherently fixed-label classifiers |
| Cross-encoder / reranker | Context-question-candidate relevance scores resemble option-wise decisions | Ranking quality and softmax normalization do not establish calibrated event probabilities |
| AR LLM | Free-text decoding versus directly reading supplied-candidate logits | A causal backbone can produce a decision without generating answer tokens |
| Masked / diffusion LM | Multiple masked positions can be read or denoised in parallel | Non-AR does not imply diffusion; masked pretraining is not proof of a deployed diffusion sampler |
| Reward model / value model | A scalar utility, preference, or return estimate versus a specified typed decision distribution | Probability of choosing an action is not probability that the action succeeds |

For dynamic options the set can change at inference time without installing a new
fixed-class head. This interface capability does not imply robust generalization to
unseen labels, descriptions, languages, or domains; those need evaluation.

For a finite menu, softmax over allowed logits describes a distribution conditional
on that menu. A model can assign most of this mass to a wrong or incomplete option
set. Include coverage/abstention controls and distinguish an uncertainty statistic
from a calibrated correctness estimate. Multiple acceptable options may also share
mass without indicating a failure.

Native numerical readout and a model writing “0.82” as text are different output
mechanisms. Neither is calibrated just because it is numerical. CE/NLL and Brier
are proper prediction objectives, but finite data, misspecification, optimization,
and deployment shift can still cause miscalibration.

Primary reading: [BERT](https://arxiv.org/abs/1810.04805),
[GLiClass](https://arxiv.org/abs/2508.07662),
[MDLM](https://arxiv.org/abs/2406.07524),
[LLaDA](https://arxiv.org/abs/2502.09992),
[On Calibration](https://arxiv.org/abs/1706.04599).
The [SemIf method](https://github.com/TheoLeeCJ/SemIf/blob/master/docs/METHOD.md)
provides a concrete generation-free causal-model example.
