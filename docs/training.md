# Training, Calibration, RLCD and RLCR

[Home](../README.md) · [Evidence index](evidence.md)

## Vocabulary used in the landscape

| Label | Required interpretation |
|---|---|
| None / Prompt-only | No project-specific parameter training in the scoped path |
| Head-only / LoRA / SFT / Full FT | Which parameters/objectives the documented recipe trains |
| Distillation | Teacher supervision; do not assume on-policy distillation |
| Calibration Training | Direct probability losses or post-hoc fitting; not necessarily RL |
| RLCD | Official vendor terminology only; algorithm remains unverified |
| RLCD (claimed) | Independent community method; actual evidence and scope stated separately |
| RLCR-like | Descriptive calibration-aware RL family, not a claim to reproduce the RLCR paper |
| No / Unknown | No RL in the scoped recipe, or insufficient information |

## Official RLCD

RLCD expands to **Reinforcement Learning for Calibrated Decisions** in the
previously cited TypeSafe launch material. The exact reward, sampling process,
optimizer and training data recipe have not been verified in this audit. The
[launch page](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
could not be retrieved here; the [official skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md)
confirms the calibrated-decision product framing, not those internals.
**Technical details not publicly disclosed in the materials reviewed.** No
community algorithm below is labelled the recovered proprietary recipe.

## What the inspected community material actually supports

| Project / version | Actual mechanism | Evidence boundary |
|---|---|---|
| Laya notebook | Gaussian noisy-logit sampling, detached proper-score advantages, score-function loss plus soft CE | Author says GRPO-style; inspected block has no standard PPO/GRPO clipped ratio |
| eve-rlcd | Categorical bandit sampling; REINFORCE reward `correct - p(action)` with detached reward | Independent Brier-gradient estimator, not vendor RLCD |
| NanoJev experiment | Paired independent predictive draws with a sampled Brier-gradient estimator | Separate experimental arm, not every gameplay checkpoint |
| decider 2B v10 | PPO outcome objective plus proper log-score belief term and consistency | 35B v1 remains supervised; do not transfer the RL label across releases |
| JevForge | Documented grouped-action RL prototype, utility, Brier objective and KL anchoring | Prototype distinguished from the main supervised release |
| Von / Verdict / system-one-open | Documented CE/Brier losses and temperature fitting | Renaming a differentiable loss “RLCD” does not demonstrate RL |

Source paths:
[Laya training notebook](https://github.com/NandhaKishorM/laya/blob/42626c348753fbb17572a813127df2278a1ec527/notebooks/laya_finetune_typed_decisions_2xT4_kaggle.ipynb),
[eve reward](https://github.com/anthony-maio/eve-rlcd/blob/57a179b7b1bedc80f65bf42ccda129dd1888272f/rlcd/rewards.py),
[NanoJev experiment](https://github.com/TianyuCodings/NanoJev/blob/618cea6d906d54e128360786d12f703fff2b1245/docs/RLCD_EXPERIMENT.md),
[decider model card](https://github.com/Mapika/decider/blob/c4daaac28af9fea95d627015cffa2dd5a5926ee6/MODEL_CARD.md),
[JevForge](https://github.com/zwliJay/jev-forge#preliminary-rlcd-support).

A sampled reward can depend on the model's probabilities. Whether it is detached
matters: a policy-gradient estimator is not automatically the total derivative of
the expected reward expression. Record the loss and gradient treatment, not merely
a function called `reward`. With complete finite labels, directly differentiating
NLL/Brier is an essential control rather than something that needs RL by default.

**Calibration split caveat.** In the inspected Laya notebook, temperature fitting
selects `all_items[::15][:400]` after training on `all_items`. This particular notebook
does not demonstrate a disjoint calibration holdout. Do not generalize that finding
to all historical Laya checkpoints, or call its fit a held-out guarantee.

## RLCR: a distinct paper and mechanism

**Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty** was first
posted on **2025-07-22**; this audit also consulted its v2 method. RLCR expands to
**Reinforcement Learning with Calibration Rewards**. The paper combines correctness
with a calibration reward, including a Brier penalty, and studies a modified GRPO
recipe with Qwen2.5-7B-Base. Its model generates reasoning, a prediction, and numerical
confidence: this is not native option-head probability readout. Related experiments
use additional backbones; do not assign one recipe to all variants.
[Paper](https://arxiv.org/abs/2507.16806) ·
[v2 method](https://arxiv.org/html/2507.16806v2) ·
[Author code](https://github.com/damanimehul/RLCR).

**RLCR and RLCD share a calibration-oriented objective, but no evidence currently
establishes that they are the same algorithm.** The paper's claim has assumptions
on rewards; it is not a guarantee for arbitrary scoring rules or deployment shifts.

## Measurement is separate from training

For probabilities p and label y, NLL is `-log p[y]` and multiclass Brier is
`sum_k (p[k] - 1[k=y])**2`. State normalization conventions: the two-class vector
Brier is twice the scalar Bernoulli Brier. ECE depends on binning and the type of
confidence being calibrated. Risk-coverage assesses selective use, not a universal
safety guarantee. Temperature scaling changes probability sharpness without adding
semantic evidence. See [On Calibration](https://arxiv.org/abs/1706.04599).
