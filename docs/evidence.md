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
| [Source 2](https://github.com/razorback16/openjev/blob/main/README.md) | media_support, current_inference_scope | Author documentation reviewed 2026-09-28 |

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

**RL status:** 2B v10 has PPO + belief calibration; 35B v1 has no RL; 2026-09-28: vision is a separate v5-transplant + PPO path; 4B/35B and later text versions must be scoped separately

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+decider&project=decider)

**Model/artifact link:** https://huggingface.co/Mapika/decider-2b (project-weight status: Yes; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/Mapika/decider/blob/c4daaac28af9fea95d627015cffa2dd5a5926ee6/README.md) | backbone, variants, readout, caching, weights | Implementation documentation |
| [Source 2](https://github.com/Mapika/decider/blob/c4daaac28af9fea95d627015cffa2dd5a5926ee6/MODEL_CARD.md) | ppo, proper_log_score, version_specific_rl | Model card |
| [Source 3](https://github.com/Mapika/decider/blob/23579f7a7e8f10e1045be492af3c1c05a005d67c/MODEL_CARD_VISION.md) | vision_backbone, vision_training, ppo, version_scope | Author model card |
| [Source 4](https://github.com/Mapika/decider/blob/main/README.md) | current_variants, gguf | Author changelog reviewed 2026-09-28 |

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
| [Source 2](https://github.com/zhengxuyu/litjev/blob/main/README.md) | media_support, current_inference_scope | Author documentation reviewed 2026-09-28 |

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
| [Source 2](https://github.com/kshetrajna12/reflex/blob/main/README.md) | media_support, current_inference_scope | Author documentation reviewed 2026-09-28 |

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

## visual-jev-yu

**[Visual Jev (Yu & Yao)](https://github.com/guanxuyu-sv/Visual-Jev)** · First public: Unknown

The recommended system uses answer-supervised LoRA and the existing LM head, not a new typed head or diffusion. The published 4B adapter and reproduction scripts are linked. Gains are concentrated on trained task families; batch-amortized speed is not single-request latency.

**RL status:** Answer SFT; no RLCD in the recommended system

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Visual+Jev+%28Yu+%26+Yao%29&project=Visual+Jev+%28Yu+%26+Yao%29)

**Model/artifact link:** https://huggingface.co/guanxuyu/visual-jev-4b-answer-sft (project-weight status: Partial; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/guanxuyu-sv/Visual-Jev/blob/main/README.md) | media_input, training, decision_path, limitations | Author implementation documentation |
| [Source 2](https://arxiv.org/abs/2609.25845) | method, paper_date | Primary arXiv abstract |

| Date | Artifact / limitation |
|---|---|
| 2026-09-22 | [Paper v1; earlier code publication not established](https://arxiv.org/abs/2609.25845) |

## valen

**[Valen](https://github.com/Liuziyu77/Valen)** · First public: Unknown

Qwen vision-language model with a trainable decision head. The inspected RL implementation samples categorical actions, freezes old log-probabilities/rewards, uses a clipped group-relative surrogate, reference KL and direct Brier loss. It uses labelled targets and is not the proprietary TypeSafe algorithm.

**RL status:** Experimental, source-inspected categorical clipped policy gradient + KL + direct Brier; labelled feedback; checkpoint-specific

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Valen&project=Valen)

**Model/artifact link:** https://huggingface.co/Valen-Team/Valen-Preview-0923 (project-weight status: Partial; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/Liuziyu77/Valen/blob/main/docs/technical.md) | media_input, training, decision_path, limitations | Author implementation documentation |
| [Source 2](https://github.com/Liuziyu77/Valen/blob/06251f9d9d3c06ea690be93b8696ccc66471f8c9/valen/training/rlcd.py) | sampling, reward, policy_gradient, direct_brier, reference_kl | Source inspected |
| [Source 3](https://github.com/Liuziyu77/Valen/blob/main/README.md) | weights, datasets, media | Author documentation |

## omnijev

**[OmniJev (Qwen)](https://github.com/tinnel123666888/OmniJev)** · First public: Unknown

The reviewed v1.1 family uses rank-32 LoRA, decision/ordinal heads and probability-scoring training followed by temperature calibration. No RLCD stage is documented in this recipe. Offline replay demonstrations are not validated closed-loop robot or game control.

**RL status:** Probability-scoring training and post-hoc temperature fitting documented; no RLCD attribution established

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+OmniJev+%28Qwen%29&project=OmniJev+%28Qwen%29)

**Model/artifact link:** https://huggingface.co/tinnel123/OmniJev (project-weight status: Partial; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/tinnel123666888/OmniJev/blob/14dbec4f71e194852c8d7b88ab36ef639493f400/README.md) | media_input, training, decision_path, limitations | Author implementation documentation |
| [Source 2](https://github.com/tinnel123666888/OmniJev/releases/tag/v1.1) | release_artifacts | Author release link |

| Date | Artifact / limitation |
|---|---|
| 2026-09-26 | [v1.1 results dated in README, not first-public date](https://github.com/tinnel123666888/OmniJev/blob/14dbec4f71e194852c8d7b88ab36ef639493f400/README.md) |

## jev-spatial

**[Jev-Spatial](https://github.com/Fr0zenCrane/jev-spatial)** · First public: Unknown

Spatial relations, numeric ranges and pointing share a LayerNorm/linear choice head. Numeric output takes two rounds; pointing takes three 3x3 decisions with crop refill. There is no generated answer text, but the complete task is not always one forward pass.

**RL status:** One supervised CE objective; no RLCD in the documented recipe

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Jev-Spatial&project=Jev-Spatial)

**Model/artifact link:** https://huggingface.co/Fr0zencr4nE/jev-spatial (project-weight status: Yes; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/Fr0zenCrane/jev-spatial/blob/main/README.md) | media_input, training, decision_path, limitations | Author implementation documentation |

## llm2jev

**[LLM2Jev](https://github.com/Yinsongxu/LLM2Jev)** · First public: Unknown

Training-free local scorer with SGLang, Transformers and MLX backends. Text/image requests are supported; cache reuse is backend- and scheduling-dependent. It is an inspectable inference mechanism, not newly trained Jev weights.

**RL status:** No

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+LLM2Jev&project=LLM2Jev)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/Yinsongxu/LLM2Jev/blob/main/README.md) | media_input, training, decision_path, limitations | Author implementation documentation |

| Date | Artifact / limitation |
|---|---|
| 2026-09-22 | [Documented text/image support milestone](https://github.com/Yinsongxu/LLM2Jev/blob/main/README.md) |
| 2026-09-23 | [Documented MLX-VLM backend milestone](https://github.com/Yinsongxu/LLM2Jev/blob/main/README.md) |

## jev-visual-mlx

**[Jev Visual (MLX)](https://github.com/hr98w/jev-visual)** · First public: Unknown

Frozen Qwen3.5 MLX visual scoring. Image/context prefill is reused by copied KV/recurrent state and batched question suffixes. There is no project-specific training or calibration; only the Qwen3.5 adapter is verified by the author.

**RL status:** No

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Jev+Visual+%28MLX%29&project=Jev+Visual+%28MLX%29)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/hr98w/jev-visual/blob/main/README.md) | media_input, training, decision_path, limitations | Author implementation documentation |

## visual-jev-anderson

**[Visual Jev (Anderson)](https://github.com/andrueandersoncs/visual-jev)** · First public: Unknown

Independent implementation, not the Yu/Yao paper. Documentation describes image-native packed isolated branches, language LoRA, a pointer head and held-out temperature fitting. A public promoted checkpoint was not verified; missing registry weights fail closed.

**RL status:** Supervised/head/calibration pipeline documented; no RLCD evidence inspected

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Visual+Jev+%28Anderson%29&project=Visual+Jev+%28Anderson%29)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/andrueandersoncs/visual-jev/blob/main/README.md) | media_input, training, decision_path, limitations | Author implementation documentation |

## openjev-multimodal

**[OpenJev Multimodal](https://github.com/jev-skills/openjev-multimodal)** · First public: Unknown

Local llama.cpp/Metal decision engine with inspectable constrained-label readout. It generates one answer token per question, not zero tokens; Python constructs typed results. No new model training or RLCD is documented.

**RL status:** Frozen upstream model; one-token constrained decoding, no RLCD

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+OpenJev+Multimodal&project=OpenJev+Multimodal)

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/jev-skills/openjev-multimodal/blob/main/README.md) | media_input, training, decision_path, limitations | Author implementation documentation |

## jev-omni

**[Jev-Omni (Gemma)](https://huggingface.co/akhilaaa3/Jev-Omni)** · First public: Unknown

HF-hosted inference code and weights; no canonical GitHub repository was verified. A finite slot head scores runtime options without text generation. The author reports a 30k-question fine-tune; the complete training recipe and RLCD attribution were not established.

**RL status:** No complete training recipe or RLCD source verified; author reports fine-tuning

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+Jev-Omni+%28Gemma%29&project=Jev-Omni+%28Gemma%29)

**Model/artifact link:** https://huggingface.co/akhilaaa3/Jev-Omni (project-weight status: Yes; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://huggingface.co/akhilaaa3/Jev-Omni) | media_input, training, decision_path, limitations | Author implementation documentation |
| [Source 2](https://huggingface.co/akhilaaa3/Jev-Omni/commit/6028e1fde1604c3442f5394e7d0eb3b534a7afe9) | classifier_head, unified_bf16, native_audio_components, packaging_correction | Primary source diff inspected |
| [Source 3](https://huggingface.co/akhilaaa3/Jev-Omni/blob/main/processor_config.json) | audio_processor, image_processor, video_processor | Primary configuration excerpt |

## groundingjev

**[GroundingJev (task-specific)](https://github.com/xyzzzh/GroundingJev)** · First public: Unknown

Explicit Jev-inspired visual grounding, not a general typed probability model. An MLP reads the last valid hidden state and regresses normalized cxcywh. Training uses weighted L1/GIoU, first head adaptation then language/visual-merger/head tuning; other vision parameters stay frozen.

**RL status:** Supervised weighted L1/GIoU; not RLCD

[Report a correction](https://github.com/Zhao-Tian-yi/awesome-jev/issues/new?template=metadata-correction.yml&title=Correction%3A+GroundingJev+%28task-specific%29&project=GroundingJev+%28task-specific%29)

**Model/artifact link:** https://huggingface.co/xyzzzh/GroundingJev (project-weight status: Yes; upstream links are identified in the notes).

| Source | Supports | Evidence level |
|---|---|---|
| [Source 1](https://github.com/xyzzzh/GroundingJev/blob/main/README.md) | media_input, training, decision_path, limitations | Author implementation documentation |
