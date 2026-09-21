# Architecture and inference taxonomy

[Home](../README.md) · [Per-project evidence](evidence.md)

## Three independent axes

A useful description separates the **backbone**, the **decision readout**, and the
**execution schedule**. “Does not generate text” identifies none of the three by
itself. The landscape's AR column concerns answer generation, not pretraining.

| Axis | Examples | What it does not establish |
|---|---|---|
| Backbone | causal Transformer, recurrent/attention hybrid, encoder, masked diffusion | Whether a decision is generated as text |
| Readout | label-token logits, pointer, option scorer, masked answer slots | Whether probabilities are calibrated |
| Schedule | individual forwards, batched rows, shared-prefix branches, native slots | Constant latency or independence between questions |

## Implemented patterns

**Direct AR-logit readout.** SemIf runs a causal model on supplied state, question
and option descriptions, then normalizes the logits of verified answer-label
tokens. No answer token needs to be sampled. In shared mode it first computes a
prefix, duplicates its cache and then batches suffixes. That is not a single total
forward or evidence that cache memory is physically shared. Sources:
[direct.py](https://github.com/TheoLeeCJ/SemIf/blob/master/src/semif_phase1/direct.py),
[shared.py](https://github.com/TheoLeeCJ/SemIf/blob/master/src/semif_phase1/shared.py).

**Trained pointer/decision heads.** Kev scores the question's decide representation
against option representations. Its Qwen3 path packs isolated block-causal
branches. Qwen3.5 instead uses separate rows and cached state: DeltaNet recurrent
layers cannot be isolated by an attention mask alone. This is a version-specific
difference, not a universal property of Qwen-based replicas.
[Kev method](https://github.com/jaredpalmer/kev#how-it-works).

**Option-wise scorers.** JevForge expands each question into candidate rows and
applies a shared scalar head before question-local normalization. Repeating a
state in a batch is not shared-state encoding. jevlike instead makes each option
query an encoded context. Candidate parallelism is not automatically multi-question
parallelism. Sources: [JevForge](https://github.com/zwliJay/jev-forge#decision-architecture),
[jevlike](https://github.com/vinnylarouge/jevlike#architecture).

**Encoder-based decisions.** Laya uses encoder representations and option markers;
Von exposes NLI and OptionMarker variants; Verdict uses ModernBERT/GLiClass-derived
label scoring. A project describing a head as a bi-encoder is not sufficient to
claim independently encoded text and labels when its documented input is jointly
encoded. See their linked source-level records in the evidence index.

**Diffusion answer slots.** The independent DiffusionGemma OpenJev reads allowed
label probabilities at masked answer slots. Additional denoising or repeated noisy
reads are optional. Its joint slots and chunked reads do not establish the isolation
contract of official Jev. More steps are not free, and denoising is not AR answer
sampling. [Implementation description](https://github.com/razorback16/openjev#how-it-works).

## Parallelism checklist

The property matrix uses ✅ for documented support, ⚠️ for partial, variant-specific
or batched support, ❌ for absent support, and ? when not established. For official
Jev, public behavior is recorded without upgrading it to a source-audited internal
mechanism. “Native probabilities” only excludes a number generated as text; it
does not certify semantic correctness or Calibration.

Check whether state computation is reused, whether each question is a batch row,
whether multiple decision positions are scored within one sequence, and whether
questions can affect each other's representations or answers. These are separate
properties. Computational answer isolation is not a claim that real-world events
are statistically independent.

## What is not known about official Jev

The [official skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md)
describes independent parallel questions and typed outputs, not a network diagram.
No reviewed primary source establishes that Jev uses diffusion, LLaDA, a particular
pointer head, or one total forward. The public LLaDA fork is a repository relationship,
not proof of use in the product. One API request may contain several server-side
model invocations. Previous 32k/64k architectural deductions require fresh primary
documentation verification and are not facts in this catalogue.
