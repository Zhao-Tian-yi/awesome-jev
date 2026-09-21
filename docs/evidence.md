# Project evidence and version notes

[Home](../README.md) · [Full comparison](comparison.md) · [Audit limitations](audit.md)

Generated from `data/projects.yaml`. Source inspection, documentation and author claims are distinguished below. Links are not an endorsement; no new technical audit is implied by a layout update.

## official-jev

**[Official Jev](https://github.com/typesafe-ai)** · First public: Unknown

Official reference, not an open model. Parallel API behavior does not establish diffusion, a one-forward implementation, or a particular cache layout. Launch date and RLCD internals need primary-source re-verification.

**RL status:** Vendor terminology; proprietary algorithm not verified

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Official+Jev&project=Official+Jev)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md) | outputs, dynamic_options, no_text_generation, question_independence | Official documentation |
| [Source 2](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | rlcd_vendor_terminology | Previously cited official page; live retrieval failed in this audit |

## semif

**[SemIf](https://github.com/TheoLeeCJ/SemIf)** · First public: Unknown

Frozen candidate-token readout. Shared mode prefills once, duplicates the native cache, then batches suffixes; it is not diffusion or a single total forward. No project-trained weights; upstream weights are required.

**RL status:** Frozen inference path

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+SemIf&project=SemIf)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/TheoLeeCJ/SemIf/blob/master/docs/METHOD.md) | backbone, training, outputs, uncalibrated | Method documentation |
| [Source 2](https://github.com/TheoLeeCJ/SemIf/blob/master/src/semif_phase1/direct.py) | decision_mechanism, no_decoding | Source inspected |
| [Source 3](https://github.com/TheoLeeCJ/SemIf/blob/master/src/semif_phase1/shared.py) | shared_state, batched_suffixes | Source inspected |

| Date | Artifact / limitation |
|---|---|
| Unknown | [No GitHub releases returned; no first-public date established](https://api.github.com/repos/TheoLeeCJ/SemIf/releases?per_page=5) |

## openjev-diffusiongemma

**[OpenJev / DiffusionGemma](https://github.com/razorback16/openjev)** · First public: Unknown

Reads allowed labels at answer slots; optional denoising and noisy rereads. Joint slots/chunks are not evidence of Jev-style question isolation. Sample averaging and entropy confidence are not calibration guarantees. Linked weights belong to the upstream model.

**RL status:** No Jev-specific training in the documented baseline

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+OpenJev+%2F+DiffusionGemma&project=OpenJev+%2F+DiffusionGemma)

**Model/artifact link:** https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4 (project-weight status: No; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/razorback16/openjev/blob/main/README.md) | backbone, masked_slots, steps, rereads, outputs, limits | Implementation documentation |

| Date | Artifact / limitation |
|---|---|
| Unknown | [No GitHub releases returned; not evidence of first publication](https://api.github.com/repos/razorback16/openjev/releases?per_page=10) |

## kev

**[Kev](https://github.com/jaredpalmer/kev)** · First public: Unknown

Qwen3 uses packed block-causal branches. Qwen3.5 uses separate cached rows because recurrent DeltaNet layers do not obey an attention mask. Released artifacts are adapters plus a head, not standalone base weights.

**RL status:** Released recipe uses supervised cross-entropy

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Kev&project=Kev)

**Model/artifact link:** https://huggingface.co/jaredpalmer/kev-4b (project-weight status: Partial; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/jaredpalmer/kev/blob/main/README.md) | backbone, lora, pointer_head, variants, isolation, weights | Implementation documentation |

| Date | Artifact / limitation |
|---|---|
| 2026-09-20 | [Version milestone; earlier prototype publication remains unverified](https://github.com/jaredpalmer/kev/releases/tag/kev-family) |

## nanojev

**[NanoJev](https://github.com/TianyuCodings/NanoJev)** · First public: Unknown

Candidate paths are tensor-batched. The paired proper-reward estimator is compared with CE and direct Brier; it is not recovered TypeSafe RLCD. Game-policy preference and event-success probabilities are different targets.

**RL status:** Independent RLCD-inspired prototype; not the main supervised release

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+NanoJev&project=NanoJev)

**Model/artifact link:** https://huggingface.co/C-Tianyu/NanoJev (project-weight status: Yes; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/TianyuCodings/NanoJev/blob/main/README.md) | backbone, outputs, weights, main_recipe | Release documentation |
| [Source 2](https://github.com/TianyuCodings/NanoJev/blob/618cea6d906d54e128360786d12f703fff2b1245/docs/RLCD_EXPERIMENT.md) | sampled_reward, estimator, limitations, batched_candidates | Detailed experimental specification |

## jevlike

**[jevlike](https://github.com/vinnylarouge/jevlike)** · First public: Unknown

Each option queries context tokens before a shared scorer and softmax. ECE reporting is not calibration training. Shared context across options is not shared-state multi-question inference; game checkpoints are task-specific.

**RL status:** Supervised option scoring

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+jevlike&project=jevlike)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/vinnylarouge/jevlike/blob/main/README.md) | architecture, training, outputs, encoder_variants | Implementation documentation |

## laya

**[Laya](https://github.com/NandhaKishorM/laya)** · First public: Unknown

The notebook samples Gaussian logit perturbations and uses detached rewards plus soft CE; no PPO clipped ratio in the inspected block. Temperature fitting selects from all_items, the training list, so a held-out calibration guarantee is not established.

**RL status:** Gaussian-logit policy gradient + soft CE; not standard GRPO

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Laya&project=Laya)

**Model/artifact link:** https://huggingface.co/convaiinnovations/laya (project-weight status: Yes; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/NandhaKishorM/laya/blob/42626c348753fbb17572a813127df2278a1ec527/README.md) | backbone, params, outputs, weights | Author documentation |
| [Source 2](https://github.com/NandhaKishorM/laya/blob/42626c348753fbb17572a813127df2278a1ec527/notebooks/laya_finetune_typed_decisions_2xT4_kaggle.ipynb) | sampled_logits, policy_gradient, soft_ce, temperature_fitting | Training source inspected |

| Date | Artifact / limitation |
|---|---|
| 2026-09-19 | [Model-routing version release, not first project publication](https://github.com/NandhaKishorM/laya/releases/tag/v0.2.0) |

## von

**[Von](https://github.com/wfzyx/von)** · First public: Unknown

README calls CE+Brier RLCD, but that is a supervised objective. OptionMarker and von-1.0 NLI are distinct backends; do not assign one checkpoint's parameters or scores to the other. No universal calibration guarantee is inferred.

**RL status:** Public CE + Brier recipe is not policy-gradient RL

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Von&project=Von)

**Model/artifact link:** https://huggingface.co/wfzyx/von-1.0 (project-weight status: Partial; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/wfzyx/von/blob/14d09878e89b103bfbbe641f9bed02e4d72c8830/README.md) | training, variants, outputs | Author documentation |
| [Source 2](https://github.com/wfzyx/von/blob/14d09878e89b103bfbbe641f9bed02e4d72c8830/src/von/engine.py) | separate_nli_and_marker_backends | Source excerpt inspected |

## decider

**[decider](https://github.com/Mapika/decider)** · First public: Unknown

Corrected the old no-RL entry: 2B v10 adds PPO, proper-log-score belief learning and consistency; 35B remains supervised. RLCR-like describes the objective family, not reproduction of the RLCR paper or TypeSafe RLCD.

**RL status:** 2B v10 has PPO + belief calibration; 35B v1 has no RL

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+decider&project=decider)

**Model/artifact link:** https://huggingface.co/Mapika/decider-2b (project-weight status: Yes; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/Mapika/decider/blob/c4daaac28af9fea95d627015cffa2dd5a5926ee6/README.md) | backbone, variants, readout, caching, weights | Implementation documentation |
| [Source 2](https://github.com/Mapika/decider/blob/c4daaac28af9fea95d627015cffa2dd5a5926ee6/MODEL_CARD.md) | ppo, proper_log_score, version_specific_rl | Model card |

## mini-jev

**[mini-Jev](https://github.com/r-ms/mini-jev)** · First public: Unknown

No AR decoding for bounded enums/Booleans. Optional strings and numbers still use generated output, outside this row. Score was not measured; normalized candidate scores are explicitly uncalibrated.

**RL status:** Frozen comparison study

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+mini-Jev&project=mini-Jev)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/r-ms/mini-jev/blob/main/README.md) | backbone, enum_readout, generated_extensions, score_not_measured | Experimental method documentation |

## litjev

**[LitJev](https://github.com/zhengxuyu/litjev)** · First public: Unknown

Direct output-head scoring with optional temperature fitting. The configured Qwen default is recorded as the repository's declaration, not as an independent validation of every supported checkpoint or shared-state speedup.

**RL status:** Frozen direct-readout path

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+LitJev&project=LitJev)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/zhengxuyu/litjev/blob/main/README.md) | configured_backbone, training, outputs, optional_calibration | Author documentation |

| Date | Artifact / limitation |
|---|---|
| Unknown | [Citation metadata inspected; no date-released field](https://github.com/zhengxuyu/litjev/blob/main/CITATION.cff) |

## zhihz-openjev

**[Open JEV (zhihz)](https://github.com/zhihz/openjev)** · First public: Unknown

Questions are sequential and re-encode context; shared computation is planned, not delivered. Choice/Binary are the documented paths; experimental Score is not quality-validated.

**RL status:** Explicitly no RLCD implementation

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Open+JEV+%28zhihz%29&project=Open+JEV+%28zhihz%29)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/zhihz/openjev/blob/main/README.md) | backbone, sequential_questions, reencoding, outputs, no_rlcd | Implementation documentation |

## dasein-openjev

**[open-jev (daseinlabs)](https://github.com/daseinlabs/open-jev)** · First public: Unknown

Scores all tokens of supplied continuations with teacher forcing, not only the first label token. AR factorization does not imply sampled decoding. Cache is shared across options within a question; optional CE-trained attention head is separate.

**RL status:** Optional supervised head training

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+open-jev+%28daseinlabs%29&project=open-jev+%28daseinlabs%29)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/daseinlabs/open-jev/blob/main/README.md) | backbone, teacher_forced_likelihood, option_batch_cache, head_training | Implementation documentation |

## reflex

**[reflex](https://github.com/kshetrajna12/reflex)** · First public: Unknown

Current stable recipe is frozen 4B, two option orders, no adapter and no calibration file. Historical LoRA/distillation experiments do not mean the stable release is fine-tuned. A moving tag is not an immutable release.

**RL status:** Stable manifest selects frozen weights

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+reflex&project=reflex)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/kshetrajna12/reflex/blob/main/README.md) | stable_recipe, two_order_ensemble, no_adapter, no_calibration_file | Release documentation |

## verdict

**[Verdict / OpenJev](https://github.com/Heman10x-NGU/Verdict-open-jev)** · First public: Unknown

Jointly encodes context and labels; do not infer an independent dual-encoder from the author's head name. Published calibration objectives are not proof of policy-gradient RL. The separate 2.0 repository requires version-specific auditing.

**RL status:** CE + Brier; RLCD branding does not establish RL

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Verdict+%2F+OpenJev&project=Verdict+%2F+OpenJev)

**Model/artifact link:** https://huggingface.co/heman10x/rlcd-modernbert-151m (project-weight status: Yes; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/Heman10x-NGU/Verdict-open-jev/blob/main/README.md) | backbone, joint_encoding, outputs, weights, calibration | Author documentation |

## eve-rlcd

**[eve-rlcd](https://github.com/anthony-maio/eve-rlcd)** · First public: Unknown

Samples an option; correctness feedback c gives reward c-p(a), with a leave-one-out baseline. This is an independent REINFORCE calibration experiment. Score scaling and wire fields are not identical to TypeSafe's API.

**RL status:** Independent bandit REINFORCE recipe; not official TypeSafe RLCD

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+eve-rlcd&project=eve-rlcd)

**Model/artifact link:** https://huggingface.co/anthonym21/qwen3-0.6b-rlcd-decision (project-weight status: Yes; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/anthony-maio/eve-rlcd/blob/main/README.md) | backbone, readout, bandit_feedback, reward, weights, shared_cache | Detailed experimental specification |
| [Source 2](https://github.com/anthony-maio/eve-rlcd/blob/57a179b7b1bedc80f65bf42ccda129dd1888272f/rlcd/rewards.py) | reward_definition | Source excerpt inspected |

| Date | Artifact / limitation |
|---|---|
| 2026-09-18 | [Dataset release; its September 17 build date is not the public release date](https://github.com/anthony-maio/eve-rlcd/releases/tag/data-v1) |

## minojev

**[minojev](https://github.com/zeredy879/minojev)** · First public: Unknown

Updated from the stale 547K-only description. Current documented release freezes Qwen3-1.7B, caches candidate features and trains a roughly 0.8M scorer; a separate zero-training logit path is available. Domain transfer is limited in the reported tests.

**RL status:** Distribution losses and post-hoc temperature

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+minojev&project=minojev)

**Model/artifact link:** https://huggingface.co/zeredy879/minojev (project-weight status: Partial; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/zeredy879/minojev/blob/main/README.md) | current_backbone, cached_features, head_training, calibration | Release documentation |

## luce

**[Luce](https://github.com/scienthoon/luce)** · First public: Unknown

Recipe for task-specific synthesis/annotation, LoRA and a decision head. Several modes exist; do not assign one attention layout to all. Public code is verified, but a downloadable project checkpoint was not verified in this audit.

**RL status:** Teacher-generated or annotated supervised data

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Luce&project=Luce)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/scienthoon/luce/blob/main/README.md) | backbone, training, modes, outputs, calibration, transfer_limits | Method documentation |

## poorjev

**[poorjev](https://github.com/rupeshpoojary9/poorjev)** · First public: Unknown

NLI-based decision interface with temperature and abstention utilities. Finite-set ECE and conformal coverage are different claims; neither makes every probability universally calibrated. Multi-question batching is not demonstrated shared representation reuse.

**RL status:** Post-hoc calibration; no RL shown

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+poorjev&project=poorjev)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/rupeshpoojary9/poorjev/blob/main/README.md) | nli_route, outputs, calibration_evaluation | Author documentation |

## jevbetter

**[jevbetter](https://github.com/olanotolu/jevbetter)** · First public: Unknown

Hashed character n-grams, two-layer context Transformer, option interaction and gated MLP. Context sharing concerns candidates in one menu, not independently isolated questions. No general released checkpoint verified.

**RL status:** Supervised learning and temperature scaling

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+jevbetter&project=jevbetter)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/olanotolu/jevbetter/blob/main/README.md) | architecture, training, option_interaction, calibration | Implementation documentation |

## jevforge

**[JevForge](https://github.com/zwliJay/jev-forge)** · First public: Unknown

Expands each question into K repeated-state candidate rows, pools the last valid token and applies a shared GELU scorer. RLCD is a preliminary independent path; it is not the official reward recipe or native shared-state execution.

**RL status:** Preliminary grouped sampling + utility + Brier + KL

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+JevForge&project=JevForge)

**Model/artifact link:** https://huggingface.co/AndeyTait/JevForge-0.8B (project-weight status: Yes; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/zwliJay/jev-forge/blob/main/README.md) | backbone, k_rows, two_layer_head, sft, rl_prototype, weights | Implementation documentation |

## system-one-open

**[System One Open](https://github.com/mithalouni/system-one-open)** · First public: Unknown

One-pass label slots for up to 52 candidates; larger sets use chunks and a final round. README says weights reside on the author's Modal volume and HF upload is pending, so public project weights are not marked available.

**RL status:** CE + Brier and temperature fitting

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+System+One+Open&project=System+One+Open)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/mithalouni/system-one-open/blob/main/README.md) | backbone, training, slot_readout, chunking, weights_pending | Implementation documentation |
