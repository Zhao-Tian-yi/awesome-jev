# Contributing

Help readers find the implementation behind the label. This is a research map,
not a ranking, an endorsement, or a catalogue of every Jev API application.

## The easiest way: send a useful lead

[Suggest a project](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=suggest-project.yml)
or [correct an entry](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml).
A repository URL, a short explanation and a primary source are enough.
**No YAML editing or three-language translation is required to open an issue.**
English, 中文 and 日本語 are welcome. Unknown facts can remain unknown.
Maintainers check the evidence, prepare the structured record and synchronize
translations before inclusion. Please never post API keys or private data.

A project author can correct their entry using the prefilled link in
[the evidence index](docs/evidence.md). Please identify the affected version.

## What belongs here?

Submit an inspectable decision-model implementation, relevant paper, benchmark,
metadata correction or broken-link fix. Core model entries need a dedicated
runtime-defined semantic decision mechanism or technical research on that
mechanism. Applications, demos, API wrappers and tutorials are separate resources.
Forks without a distinct technical contribution are not separate models.

## Editing the data directly

Edit `data/projects.yaml`, not generated READMEs. Required fields remain:
`id`, `name`, `official`, `release_date`, `release_evidence`, `github`, `website`,
`paper`, `huggingface`, `backbone`, `params`, `architecture`, `training`, `rl`,
`rl_status`, `ar`, `decision_mechanism`, `outputs`, `weights`, `properties`,
`evidence`, and `notes.en/zh/ja`.

A contributor may submit a draft PR in one language and request translation help.
**The merged data must pass the three-language checks.** Maintainers complete
missing translations and metadata; the easier submission path does not relax
technical inclusion standards.

For each important claim, link to a model card, source file, training script or
release. Prefer commit permalinks. Distinguish source inspection, method
documentation and an author's claim. Do not use stars as technical evidence.

### Dates and order

`release_date` is the earliest supported first-public date. Do not substitute a
repository creation date, paper acceptance date or later model release. Use
YYYY-MM-DD, YYYY-MM, or null. Store version milestones in `release_evidence`.
Official Jev stays first; known dates are ascending; unknowns keep the existing
curation order. Stars, model size and subjective quality never change that order.

### Architecture and execution

`ar` describes token-by-token decision generation, not backbone pretraining. A
causally pretrained model with direct logits can have `ar: 'No'`; the detailed
comparison calls this column **AR Decoding** to avoid ambiguity.
Ordinary tensor batching is `parallel_q: partial`, not evidence of native
multi-question slots. Shared State means computation reuse, not the same input
string. Document optional and historical variants separately.
See [architecture](docs/architecture.md).

### Training and availability

Reserve unqualified `RLCD` for the official vendor term. Community
`RLCD (claimed)` must include the actual sampling, reward, gradient and version
scope in `rl_status` and evidence. NLL/Brier or temperature scaling alone is not
RL; a prototype does not establish how every released checkpoint was trained.
See [the training audit](docs/training.md).

`weights` records **project-specific artifacts**: Yes, No, Partial, API only or
Unknown. A frozen model wrapper can have No and still use open upstream weights.
The homepage makes that distinction explicit. Partial means adapter/head, not a
standalone base model. Keep total and active MoE parameter counts separate.

## Generate and check

```bash
python -m pip install PyYAML==6.0.3
python scripts/generate_readme.py
python scripts/validate.py
python scripts/test_presentation.py
python scripts/generate_readme.py --check
# Optional network check; blocked/rate-limited hosts are reported separately.
python scripts/validate.py --links
```

The generator produces three READMEs, the full comparison, the evidence index and
the curation log. They share facts, order and URLs. Add papers to
`data/papers.yaml` and resource lists to `data/awesome-lists.yaml`.

For a substantive addition, correction or presentation change, add a short entry
to `data/updates.yaml` with a source. These are **curation dates**, not upstream
release dates. Star-only refreshes are not substantive updates. Do not change the
technical audit date merely because stars or presentation changed.

The existing GitHub Stars workflow refreshes metadata and regenerates pages on
relevant pushes to branches in this repository, or when manually dispatched. It
uses normal fast-forward pushes and does not rewrite the generator or force-push.
External PRs must run the commands above; no write workflow runs on fork PRs.

Keep one kind of change per PR where practical. Explain evidence conflicts and
limitations. Do not turn incomparable benchmark figures into a leaderboard.
Original list/data/docs contributions use CC BY 4.0; scripts/workflows use MIT.
Upstream code, model weights and datasets keep their respective licenses.
