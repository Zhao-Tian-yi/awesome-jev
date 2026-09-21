# Contributing

This is a research map, not a ranking. Submit an inspectable implementation,
relevant paper, benchmark, metadata correction, or broken-link fix. A thin API
wrapper, application, or tutorial belongs outside the core model table. Forks
without a distinct technical contribution are not separate models.

## Evidence first

Edit `data/projects.yaml`, not the generated READMEs. Include a primary repository,
model card, or source path for every important technical claim. Prefer pinned
commit URLs. Identify the version and whether you inspected source code, a code
excerpt, a method description, or an author claim. Unknown is preferable to a guess.

Required project fields: `id`, `name`, `official`, `release_date`,
`release_evidence`, `github`, `website`, `paper`, `huggingface`, `backbone`,
`params`, `architecture`, `training`, `rl`, `rl_status`, `ar`,
`decision_mechanism`, `outputs`, `weights`, `properties`, `evidence`, and
`notes.en/zh/ja`. Keep null fields; do not silently remove missing information.

`release_date` is the earliest supported first-public date, not a paper acceptance,
latest commit, repository creation proxy, or later checkpoint release. Use
YYYY-MM-DD, YYYY-MM when only the month is supported, or null. Store version
milestones separately in `release_evidence`, without presenting them as first
publication. Official Jev is always first. Other known dates are ascending;
unknowns follow in existing curation order, which carries no priority claim.

`ar` describes whether the scoped decision path needs token-by-token answer
generation. An AR-pretrained backbone with direct logit readout has `ar: 'No'`.
Document optional generative paths separately. Ordinary tensor batching is
`parallel_q: partial`, not native multi-question parallelism. Shared state means
reused computation, not merely the same JSON field. See `docs/architecture.md`.

Reserve unqualified `RLCD` for the official vendor terminology. For third-party
claims use `RLCD (claimed)` plus the actual sampling, reward and optimizer evidence.
A Brier/NLL loss or temperature fitting alone is not RL. A prototype is not proof
that every released checkpoint used it. Do not label a method as an official
RLCD reproduction. See `docs/training.md`.

`weights` describes project-specific artifacts: Yes, No, Partial, API only, or
Unknown. A frozen inference project can have No here and still use an open
upstream model. Partial covers adapters/heads that require separate base weights.
Avoid copying unverified parameter counts across variants or confusing MoE total
and activated counts.

## Updating the generated pages

```bash
python -m pip install PyYAML==6.0.3
python scripts/generate_readme.py
python scripts/validate.py
python scripts/generate_readme.py --check
# Optional network check; blocked/rate-limited hosts are reported separately.
python scripts/validate.py --links
```

All three READMEs must have identical project facts and URLs. Only descriptions,
headings, legends and notes are localized. The generator also produces the evidence
index. Add related papers to `data/papers.yaml`, not to the implementation table;
add resource lists to `data/awesome-lists.yaml`.

Keep one type of change per PR when practical. Explain evidence conflicts and
limitations. Do not submit stars, scores, endorsements, unsupported speed claims,
or third-party benchmark numbers as directly comparable results.

Original list/data/docs contributions use CC BY 4.0; scripts/workflows use MIT.
Do not relicense upstream models, code, or datasets.
