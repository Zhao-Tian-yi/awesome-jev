# Audit record — 2026-09-21

[Home](../README.md) · [Evidence by project](evidence.md)

## Scope and verification level

This revision curates **one official reference and 21 community implementations**.
It is not a claim of exhaustive coverage of every repository containing “Jev”.
The previous list was re-read and corrected using primary repository documentation,
selected implementation/training excerpts, model cards and release metadata.
Per-field evidence records distinguish code inspected, excerpts, author method
claims, and pages that could not be fetched. They are not interchangeable.

No GPU training, live Jev inference, upstream test suite, benchmark reproduction,
or download/license audit of every checkpoint was performed. Repo code availability
does not certify a runnable release. Branch URLs can change; pinned evidence is
used where a revision was available.

## Corrections to the previous version

| Earlier issue | Correction |
|---|---|
| Qwen-backed projects all labelled AR | AR now describes answer generation; direct readout is No while architecture remains AR LLM or Hybrid |
| “Parallel” used for every multi-question request | Native slots, batched suffixes and sequential evaluation are distinguished |
| Shared JSON state treated as shared compute | Only documented reuse is marked supported; repeated candidate rows are not reuse |
| decider labelled no RL | 2B v10 has PPO plus a belief-scoring objective; 35B v1 remains supervised |
| minojev represented only as a 547K toy | Current head-trained path uses frozen Qwen3-1.7B with an approximately 0.8M head |
| Laya simply called GRPO | Inspected notebook uses Gaussian-logit policy gradient plus soft CE; it is a community RLCD claim |
| Laya temperature fitting treated as held-out | Inspected notebook selects a subset of the training items for temperature fitting |
| Von/Verdict calibration objectives called RL | Documented CE/Brier and temperature fitting do not establish RL |
| All public model links treated as released project weights | Upstream weights, adapters/heads, API-only and inaccessible author-volume artifacts are separate |
| Jev inferred to be diffusion from parallel behavior | Official architecture stays Not disclosed; third-party diffusion implementations prove feasibility only |
| Stale reflex recipe | Current documented stable path is frozen readout with two option orders, not the earlier LoRA release |
| zhihz/openjev treated as shared/parallel | Its current documentation explicitly says questions run sequentially and repeat context |

## First-public dates remain unresolved

**All 22 core first-public dates are Unknown in this revision.** This is a material
limitation, not a claim that all projects launched together or lack public releases.
The first-public identity could not be established reliably from the inspected
metadata. No timestamp was invented to produce an attractive chronology.

In particular, repository `created_at` is not sufficient evidence of when a private
repository first became public. Old commit timestamps can predate public access;
a later release can postdate earlier public code. Paper dates in the related-research
section are arXiv v1 submission dates, not acceptance dates.

| Checked artifact | What is actually established |
|---|---|
| SemIf GitHub releases | Empty release list; no first-public date follows |
| DiffusionGemma OpenJev releases | Empty release list; no first-public date follows |
| LitJev CITATION.cff | Version present, no date-released |
| eve-rlcd data-v1 | Published 2026-09-18; dataset build 2026-09-17 is a different event |
| Laya v0.2.0 | Published 2026-09-19; model-routing update is not proof of first publication |
| Kev family | Published/updated 2026-09-20; earlier prototypes remain separately relevant |

Sources: [SemIf releases](https://api.github.com/repos/TheoLeeCJ/SemIf/releases),
[OpenJev releases](https://api.github.com/repos/razorback16/openjev/releases),
[LitJev citation](https://github.com/zhengxuyu/litjev/blob/main/CITATION.cff),
[eve dataset release](https://github.com/anthony-maio/eve-rlcd/releases/tag/data-v1),
[Laya release](https://github.com/NandhaKishorM/laya/releases/tag/v0.2.0),
[Kev release](https://github.com/jaredpalmer/kev/releases/tag/kev-family).

The generator pins Official Jev first, sorts known first-public dates ascending,
and places unknowns last in stable curation order. Ordering within the Unknown
block is neither chronology nor endorsement. The timeline explicitly shows
**verified version milestones**, not substituted first-public dates. For a month-only
date, first-of-month is a display-order convention, not an inferred launch day.

## Official sources and access limitations

The TypeSafe skill was readable through GitHub. The linked launch article and
model-limit pages did not return usable live content during this audit. Their
previously quoted dates, 32k/64k limits, and supposed architectural implications
were therefore not promoted to newly verified facts. A stale pre-launch homepage
is not evidence that the currently discussed service is still in stealth.

RLCD remains the previously cited vendor term, with a retrieval caveat in the data;
its proprietary recipe is not reconstructed here. Unknown does not mean disproved.

## Discovery and placement decisions

Repository searches covered Jev/OpenJev, System One, diffusion and RLCD terms,
plus the existing model set. Related arXiv and model-card sources were consulted.
Unreviewed name matches and plain forks were not automatically admitted.

[mmastrac/jevenator2](https://github.com/mmastrac/jevenator2) was inspected and placed
under Applications: it performs region scans through an external decision endpoint,
not a new decision backbone. Additional diffusion-name matches such as
[Saik0s/diffusiongemma-jev-macos](https://github.com/Saik0s/diffusiongemma-jev-macos)
remain discovery leads, not audited core entries.

The old OmniJev/awesome-jev URL resolves to
[OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery), whose
README explicitly gives a September 2026 launch month. The current repository's
public creation was observed in this authorized session on 2026-09-21. Service
access dates mentioned by other lists were not reused as those lists' launch dates.

## Maintenance boundary

Validation catches structural mistakes, stale generated files and some broken
links; it cannot prove an architectural or scientific claim. Network restrictions,
HTTP 403/429 and cache misses are reported as unverified, not dead links. A passing
CI run is not a model-quality endorsement. No background monitoring is configured.
