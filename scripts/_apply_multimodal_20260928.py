# One-time, reviewed migration; remove this file after the generated change is verified.
from pathlib import Path
import hashlib
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-09-28'

def blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()

assert blob_sha(ROOT / 'data/projects.yaml') == 'b12743f641cce3864ea9c3ab573f27bd7ae04c2f', 'Project source changed; reconcile before migration.'
assert blob_sha(ROOT / 'scripts/generate_readme.py') == 'dfd5de4362f6e241d1c074265a5ba1cd27bea708', 'Generator changed; review patch.'

def notes(en, zh, ja):
    return {'en': en, 'zh': zh, 'ja': ja}

def evidence(url, supports, level='Author implementation documentation'):
    return {'url': url, 'supports': supports, 'level': level}

def media(summary, image, video, audio, training, rl, execution, source, note, artifact=None):
    return dict(summary=summary, image=image, video=video, audio=audio, training=training, rl=rl,
                execution=execution, source=source, checked_at=DATE, notes=note, artifact=artifact)

def project(id, name, repo, backbone, params, architecture, training, rl, mechanism, weights, note, m,
            hf=None, paper=None, outputs=None, props=None, rl_status=None, extra=None, milestones=None):
    properties = dict(typed='yes', dynamic='yes', variable='yes', native='yes', calibration='partial',
                      shared_state='unknown', multi_q='yes', parallel_q='partial', non_ar='yes')
    properties.update(props or {})
    github = 'https://github.com/' + repo if repo else None
    return dict(id=id, name=name, official=False, release_date=None, release_evidence=milestones or [],
        github=github, website=hf if not repo else None, paper=paper, huggingface=hf,
        backbone=backbone, params=params, architecture=architecture, training=training,
        rl=rl, rl_status=rl_status or rl, ar='Yes' if properties['non_ar']=='no' else 'No',
        decision_mechanism=mechanism, outputs=outputs or ['Noul','Choice','Score'], weights=weights,
        properties=properties, evidence=[evidence(m['source'], ['media_input','training','decision_path','limitations'])] + (extra or []),
        notes=note, media=m)

vsource='https://github.com/guanxuyu-sv/Visual-Jev/blob/main/README.md'
valsource='https://github.com/Liuziyu77/Valen/blob/main/docs/technical.md'
valrl='https://github.com/Liuziyu77/Valen/blob/06251f9d9d3c06ea690be93b8696ccc66471f8c9/valen/training/rlcd.py'
omsource='https://github.com/tinnel123666888/OmniJev/blob/14dbec4f71e194852c8d7b88ab36ef639493f400/README.md'
spatialsource='https://github.com/Fr0zenCrane/jev-spatial/blob/main/README.md'
llmsource='https://github.com/Yinsongxu/LLM2Jev/blob/main/README.md'
mlxsource='https://github.com/hr98w/jev-visual/blob/main/README.md'
andsource='https://github.com/andrueandersoncs/visual-jev/blob/main/README.md'
localsource='https://github.com/jev-skills/openjev-multimodal/blob/main/README.md'
hfsource='https://huggingface.co/akhilaaa3/Jev-Omni'
hfcommit='https://huggingface.co/akhilaaa3/Jev-Omni/commit/6028e1fde1604c3442f5394e7d0eb3b534a7afe9'
groundsource='https://github.com/xyzzzh/GroundingJev/blob/main/README.md'

new=[]
new.append(project('visual-jev-yu', 'Visual Jev (Yu & Yao)', 'guanxuyu-sv/Visual-Jev', 'Qwen3-VL', '4B / 8B',
 'AR VLM', 'LoRA / answer SFT', 'No', 'Existing LM-head candidate-token logits', 'Partial',
 notes('The recommended system uses answer-supervised LoRA and the existing LM head, not a new typed head or diffusion. The published 4B adapter and reproduction scripts are linked. Gains are concentrated on trained task families; batch-amortized speed is not single-request latency.',
       '推荐版本是答案监督 LoRA 与原有 LM head，不是新 typed head 或 diffusion。已发布 4B adapter；收益主要集中在训练任务族，批摊销耗时不等于单请求延迟。',
       '推奨構成は回答 SFT の LoRA と既存 LM head。新しい typed head や diffusion ではない。4B adapter を公開。学習済みタスクの改善とバッチ償却時間を単一リクエストの性能と混同しない。'),
 media('Text + image','Native image input','Not documented','Not documented','Answer-supervised LoRA','No RL in recommended recipe',
       'One visual/public prefix; isolated suffixes batched',vsource,
       notes('Choice quickstart supports 2–16 options. A matched typed-head control is experimental. No claim that SFT guarantees calibration.',
             '快速示例支持 2–16 选项 Choice；独立 typed head 是实验对照，不是默认系统，SFT 不保证校准。',
             'Quickstart は 2–16 候補の Choice。typed head は比較実験であり既定構成ではない。SFT は校正を保証しない。'),
       'https://huggingface.co/guanxuyu/visual-jev-4b-answer-sft'),
 hf='https://huggingface.co/guanxuyu/visual-jev-4b-answer-sft',paper='https://arxiv.org/abs/2609.25845',outputs=['Choice','Probability Distribution'],
 props={'calibration':'unknown','shared_state':'yes'},
 rl_status='Answer SFT; no RLCD in the recommended system',
 extra=[evidence('https://arxiv.org/abs/2609.25845',['method','paper_date'],'Primary arXiv abstract')],
 milestones=[{'url':'https://arxiv.org/abs/2609.25845','kind':'Paper v1; earlier code publication not established','date':'2026-09-22','first_public':False}]))

new.append(project('valen','Valen','Liuziyu77/Valen','Qwen3.5','0.8B / 2B + decision head',
 'Hybrid VLM + Decision Head','SFT + experimental RL','RLCD (claimed)','Shared candidate head; separate ordinal-level branches','Partial',
 notes('Qwen vision-language model with a trainable decision head. The inspected RL implementation samples categorical actions, freezes old log-probabilities/rewards, uses a clipped group-relative surrogate, reference KL and direct Brier loss. It uses labelled targets and is not the proprietary TypeSafe algorithm.',
       'Qwen 多模态骨干加决策头。已核查的 RL 代码包含类别动作采样、冻结旧策略和奖励、组相对 clipped surrogate、参考 KL 与直接 Brier 损失。训练使用标签，不是 TypeSafe 原版算法。',
       'Qwen のマルチモーダル基盤と判断 head。確認した RL は categorical sampling、固定した旧 log-prob/reward、group-relative clipping、参照 KL、直接 Brier 損失を使用。ラベル付き学習で、TypeSafe の非公開手法ではない。'),
 media('Text + image + video','Native image input','Processor video path documented; temporal evaluation unverified','Not documented',
       'Head warmup; LLM LoRA; optional merger/vision-top tuning','Inspected GRPO-style local RLCD + direct Brier',
       'State preparation shared; backbone recomputed per branch',valsource,
       notes('Choice/Noul use one branch per question; Score evaluates each level separately. Preparing state once is not shared backbone encoding. Preview-0923 requires the Qwen3.5-2B base. General and Sokoban results use different checkpoints.',
             'Choice/Noul 每题一分支，Score 每等级独立前向；state 预处理复用不等于骨干共享。Preview-0923 仍需 Qwen3.5-2B 底座；通用与推箱子评测使用不同 checkpoint。',
             'Choice/Noul は質問ごと、Score はレベルごとの forward。state 前処理の再利用は backbone 共有ではない。Preview-0923 は別途 Qwen3.5-2B を必要とし、汎用評価と倉庫番は異なる checkpoint。'),
       'https://huggingface.co/Valen-Team/Valen-Preview-0923'),
 hf='https://huggingface.co/Valen-Team/Valen-Preview-0923',props={'shared_state':'no'},
 rl_status='Experimental, source-inspected categorical clipped policy gradient + KL + direct Brier; labelled feedback; checkpoint-specific',
 extra=[evidence(valrl,['sampling','reward','policy_gradient','direct_brier','reference_kl'],'Source inspected'),
        evidence('https://github.com/Liuziyu77/Valen/blob/main/README.md',['weights','datasets','media'],'Author documentation')]))

new.append(project('omnijev','OmniJev (Qwen)','tinnel123666888/OmniJev','Qwen3.5','0.8B / 2B / 4B',
 'Hybrid VLM + Decision/ordinal heads','LoRA + Calibration Training','No','Typed decision heads; prefix branches','Partial',
 notes('The reviewed v1.1 family uses rank-32 LoRA, decision/ordinal heads and probability-scoring training followed by temperature calibration. No RLCD stage is documented in this recipe. Offline replay demonstrations are not validated closed-loop robot or game control.',
       '核查的 v1.1 家族采用 rank-32 LoRA、decision/ordinal heads、概率评分训练及温度校准；该配方未列出 RLCD。离线回放不能作为闭环机器人或游戏控制证据。',
       'v1.1 は rank-32 LoRA、decision/ordinal head、確率スコアによる学習と温度校正。確認した配方に RLCD はない。オフライン再生を閉ループ制御の検証と扱わない。'),
 media('Image + frame mosaic + spectrogram','Native images; multi-image panels','16 timestamped frames rendered as one mosaic','Spectrogram / waveform images',
       'LoRA + heads; probability scoring + temperature fit','No RL stage documented',
       'Prefix-branch inference; panels and checkpoint-dependent path',omsource,
       notes('Audio is represented visually, not passed to a native audio encoder. video_state constructs a 16-frame mosaic. Base weights must be downloaded separately. v1.1 aggregates use capped/unequal subsets and include withdrawn label-defect results; not a cross-model leaderboard.',
             '音频以频谱图/波形图输入，不是原生音频编码器；video_state 生成 16 帧拼图。需另下底座。v1.1 汇总涉及截断及不等规模子集，部分标签缺陷结果已撤回，不能拼成统一排行榜。',
             '音声はスペクトログラム等の画像として入力。video_state は 16 フレームのモザイクを作る。基盤重みは別途必要。v1.1 の集計は上限付き・非等量の部分集合で、ラベル不備による撤回もある。'),
       'https://huggingface.co/tinnel123/OmniJev'),
 hf='https://huggingface.co/tinnel123/OmniJev',props={'shared_state':'partial'},
 rl_status='Probability-scoring training and post-hoc temperature fitting documented; no RLCD attribution established',
 extra=[evidence('https://github.com/tinnel123666888/OmniJev/releases/tag/v1.1',['release_artifacts'],'Author release link')],
 milestones=[{'url':omsource,'kind':'v1.1 results dated in README, not first-public date','date':'2026-09-26','first_public':False}]))

new.append(project('jev-spatial','Jev-Spatial','Fr0zenCrane/jev-spatial','Molmo2-ER','Not separately verified',
 'AR VLM + Decision Head','LoRA + Decision Head','No','Unified choice head; hierarchical scalar/point decisions','Yes',
 notes('Spatial relations, numeric ranges and pointing share a LayerNorm/linear choice head. Numeric output takes two rounds; pointing takes three 3x3 decisions with crop refill. There is no generated answer text, but the complete task is not always one forward pass.',
       '空间关系、数值区间与指点共享 LayerNorm/Linear 选择头。数值两轮、指点三轮 3×3 网格并重新裁图；不生成答案文本，但完整任务并非一次前向。',
       '空間関係・数値範囲・pointing は共通の LayerNorm/Linear head。数値は 2 回、pointing は crop refill を伴う 3 回の 3×3 選択。文章生成はないが全タスクが単一 forward ではない。'),
 media('Image(s) + spatial question','Native images and selected crops','Not documented','Not documented','LLM LoRA + unified head; vision/projector frozen',
       'Supervised cross-entropy; no RLCD','Shared image cache; same-round crop batching',spatialsource,
       notes('Pointing is a grid path, not direct continuous box regression. Against a shared-prefix AR baseline the 24-crop path can be slower; provisional RoboSpatial numbers are explicitly flagged by the author.',
             '指点输出来自网格路径，不是连续 bbox 回归；对比同样共享前缀的 AR 基线，24-crop 路径可能更慢。作者明确标记 RoboSpatial 数字待核实。',
             'Pointing はグリッド経路であり連続 bbox 回帰ではない。共有 prefix の AR 基準より 24-crop 経路が遅い場合がある。RoboSpatial の数値には作者の未検証注記がある。'),
       'https://huggingface.co/Fr0zencr4nE/jev-spatial'),
 hf='https://huggingface.co/Fr0zencr4nE/jev-spatial',outputs=['Choice','Regression'],
 props={'native':'partial','calibration':'unknown','shared_state':'yes'},rl_status='One supervised CE objective; no RLCD in the documented recipe')))

new.append(project('llm2jev','LLM2Jev','Yinsongxu/LLM2Jev','Configurable LLM / VLM (Qwen examples)','Configuration-dependent',
 'AR/Hybrid VLM / Option Scorer','None','No','Candidate binary scoring from prefill logits','No',
 notes('Training-free local scorer with SGLang, Transformers and MLX backends. Text/image requests are supported; cache reuse is backend- and scheduling-dependent. It is an inspectable inference mechanism, not newly trained Jev weights.',
       '无需训练的本地打分器，支持 SGLang、Transformers、MLX 和图文请求。缓存复用取决于后端与调度；这是可检查的推理实现，不是新训练的 Jev 权重。',
       'SGLang・Transformers・MLX に対応する学習不要のローカル scorer。画像入力とキャッシュ再利用は経路に依存する。新しい学習済み Jev 重みではなく推論実装。'),
 media('Text + image','Native images in state/instructions','Not documented','Not documented','Frozen backbone','No RLCD',
       'Staged SGLang candidate cache; explicit MLX prefix reuse',llmsource,
       notes('September 22 documents multimodal support; September 23 adds MLX-VLM. These are version milestones, not first-public dates. Native probabilities are not a calibration guarantee.',
             '9 月 22 日记录图文支持、23 日增加 MLX-VLM，均为版本进展而非首次发布日期。原生概率不保证校准。',
             '9 月 22 日に画像対応、23 日に MLX-VLM を記録。初回公開日ではなく機能更新。確率の直接出力だけでは校正を保証しない。')),
 props={'calibration':'unknown','shared_state':'partial'},
 milestones=[{'url':llmsource,'kind':'Documented text/image support milestone','date':'2026-09-22','first_public':False},
             {'url':llmsource,'kind':'Documented MLX-VLM backend milestone','date':'2026-09-23','first_public':False}]))

new.append(project('jev-visual-mlx','Jev Visual (MLX)','hr98w/jev-visual','Qwen3.5-0.8B','0.8B; documented 4-bit path',
 'Hybrid VLM / Option Scorer','None','No','Candidate-label / sequence logits','No',
 notes('Frozen Qwen3.5 MLX visual scoring. Image/context prefill is reused by copied KV/recurrent state and batched question suffixes. There is no project-specific training or calibration; only the Qwen3.5 adapter is verified by the author.',
       '冻结 Qwen3.5 的 MLX 视觉打分。图像及上下文 prefill 后复制 KV/循环状态并批处理问题后缀。无项目训练与校准；作者仅核实 Qwen3.5 adapter。',
       '凍結 Qwen3.5 の MLX 視覚 scorer。画像/context の prefill 後に KV/再帰状態をコピーし suffix をバッチ処理。追加学習・校正はなく、作者が確認した adapter は Qwen3.5。'),
 media('Text + image / camera frame','Native pixels','Per-frame camera demos; no temporal-video claim','Not documented','None','No RLCD',
       'Shared prefill; copied cache; suffix batches',mlxsource,
       notes('Supports 1–64 questions and 2–26 options. Reused state is copied, not zero-copy. Simplified game demos and throughput measurements do not establish general game-playing quality.',
             '支持 1–64 问题、2–26 候选。缓存是复制复用而非零拷贝；简化游戏演示和吞吐测试不代表通用游戏能力。',
             '1–64 質問、2–26 候補。キャッシュはコピーされ、zero-copy ではない。簡略化ゲームやスループット測定を汎用ゲーム能力と解釈しない。')),
 props={'calibration':'no','shared_state':'yes'}))

new.append(project('visual-jev-anderson','Visual Jev (Anderson)','andrueandersoncs/visual-jev','Qwen3-VL','Size depends on registry checkpoint',
 'AR VLM + Pointer Head','LoRA + Decision Head + Calibration Training','No','Learned option pointer head','Unknown',
 notes('Independent implementation, not the Yu/Yao paper. Documentation describes image-native packed isolated branches, language LoRA, a pointer head and held-out temperature fitting. A public promoted checkpoint was not verified; missing registry weights fail closed.',
       '独立实现，不是 Yu/Yao 的论文代码。文档描述原生图像、packed 隔离分支、语言 LoRA、pointer head 与留出温度拟合。未核实可公开获取的 promoted checkpoint；缺少本地权重会拒绝启动。',
       'Yu/Yao 論文とは別実装。画像・分離 packed 分岐・言語 LoRA・pointer head・holdout 温度校正を文書化。公開 promoted checkpoint の取得は未確認で、重み欠如時は停止する。'),
 media('Image(s) + text','Native one/multiple images (documented)','Not documented','Not documented','Documented LoRA + pointer head; temperature fit',
       'No RLCD evidence in reviewed documentation','Packed isolated question branches (documented)',andsource,
       notes('Treat it as an inspectable research implementation, not a verified downloadable release. The registry label is not release-date evidence. Candidate-token inference is a separate uncalibrated baseline.',
             '作为可检查的研究实现收录，不声称已有可下载的正式模型。registry 名称不作为发布日期；候选 token 读出是单独未校准基线。',
             'コードを調査可能な研究実装として収録し、取得可能な正式重みとは主張しない。registry 名は公開日の根拠にしない。token readout は別の未校正 baseline。')),
 props={'shared_state':'partial','parallel_q':'partial'},rl_status='Supervised/head/calibration pipeline documented; no RLCD evidence inspected'))

new.append(project('openjev-multimodal','OpenJev Multimodal','jev-skills/openjev-multimodal','Qwen VLM family via llama.cpp','0.8B / 4B default profiles; larger optional',
 'AR/Hybrid VLM','None','No','One generated label token + candidate probabilities','No',
 notes('Local llama.cpp/Metal decision engine with inspectable constrained-label readout. It generates one answer token per question, not zero tokens; Python constructs typed results. No new model training or RLCD is documented.',
       '本地 llama.cpp/Metal 决策引擎，使用可检查的受限标签读出。每题生成一个答案 token，不是零 token；Python 组装结构化结果。未训练新模型，也无 RLCD。',
       'llama.cpp/Metal の制約付きラベル読出し。質問ごとに 1 token を生成し、ゼロ token ではない。型付き結果は Python が構築。追加学習や RLCD はない。'),
 media('Text + image / sampled frames','Native PNG/JPEG/WebP','Sampled images only; native video unsupported','Unsupported in reviewed backend','None','No RLCD',
       'One output token/question; local serialized-resource default',localsource,
       notes('Supports complete candidate probabilities and image inputs. Audio and native video are explicitly unsupported. This row retains AR Decoding=Yes for its actual one-token path; no long prose/JSON decoding is implied.',
             '支持完整候选概率及图像输入；明确不支持音频和原生视频。由于确实生成一个标签 token，AR Decoding 标为 Yes，但并不生成长文本或 JSON。',
             '画像と全候補確率に対応。音声・ネイティブ動画は明示的に非対応。1 ラベル token を生成するため AR Decoding=Yes とするが、長文や JSON 生成ではない。')),
 props={'calibration':'no','shared_state':'partial','parallel_q':'no','non_ar':'no'},rl_status='Frozen upstream model; one-token constrained decoding, no RLCD'))

new.append(project('jev-omni','Jev-Omni (Gemma)',None,'Gemma 4 12B IT','12B + 256-slot head',
 'Multimodal Backbone + Classification Head','Fine-tuning (author reported)','Unknown','Last-hidden-state 256-slot classifier','Yes',
 notes('HF-hosted inference code and weights; no canonical GitHub repository was verified. A finite slot head scores runtime options without text generation. The author reports a 30k-question fine-tune; the complete training recipe and RLCD attribution were not established.',
       '已核实 HF 托管的推理代码与权重，未核实规范 GitHub 仓库。有限槽位分类头读取运行时候选，不生成文本。作者报告 3 万题微调，但完整训练配方和 RLCD 归属未确认。',
       'HF 上の推論コードと重みを確認。公式 GitHub は未確認。有限スロット head で実行時候補を評価し文章を生成しない。3 万問の fine-tune は作者の報告で、完全な学習手順と RLCD は未確認。'),
 media('Text + image + audio + frames','Native image encoder','16-frame public helper; processor configuration is a separate path','Native Gemma audio components',
       'Reported fine-tuning; full training scope unverified','Unknown; do not infer RLCD from calibration metrics',
       'One question/call; no shared multi-question discount',hfsource,
       notes('Unlike OmniJev/Qwen, audio uses Gemma audio components, not spectrogram images. The inspected root conversion now loads unified BF16 weights plus head.pt, replacing the old FP32/separate-base path still described by some card text. 256 slots exist, but quality above 20 choices is not established.',
             '不同于 Qwen OmniJev，音频使用 Gemma 音频组件而非频谱图。已核查的根目录迁移改为统一 BF16 权重加 head.pt；部分模型卡仍描述旧 FP32/另下底座路径。可容纳 256 槽位，不等于超过 20 候选也有可靠效果。',
             'Qwen OmniJev と違い Gemma 音声コンポーネントを使用。確認した更新では root の統合 BF16 と head.pt を読み、旧 FP32/別 base 経路を置き換える。256 スロット対応でも 20 候補超の品質は未確立。'),hfsource),
 hf=hfsource, outputs=['Choice','Probability Distribution'],
 props={'typed':'partial','shared_state':'no','multi_q':'no','parallel_q':'no'},
 rl_status='No complete training recipe or RLCD source verified; author reports fine-tuning',
 extra=[evidence(hfcommit,['classifier_head','unified_bf16','native_audio_components','packaging_correction'],'Primary source diff inspected'),
        evidence('https://huggingface.co/akhilaaa3/Jev-Omni/blob/main/processor_config.json',['audio_processor','image_processor','video_processor'],'Primary configuration excerpt')]))

new.append(project('groundingjev','GroundingJev (task-specific)','xyzzzh/GroundingJev','Qwen3.5-0.8B','0.8B + regression head',
 'Hybrid VLM + Regression Head','Head-only then joint SFT','No','Continuous normalized bounding-box regression','Yes',
 notes('Explicit Jev-inspired visual grounding, not a general typed probability model. An MLP reads the last valid hidden state and regresses normalized cxcywh. Training uses weighted L1/GIoU, first head adaptation then language/visual-merger/head tuning; other vision parameters stay frozen.',
       '明确受 Jev 启发的视觉定位，不是通用概率决策模型。MLP 读取最后有效 hidden state，直接回归归一化 cxcywh。训练使用 L1/GIoU，先适配头再调语言骨干、视觉 merger 与头，其余视觉参数冻结。',
       'Jev に着想を得た視覚 grounding だが汎用確率判断モデルではない。最後の有効 hidden state から MLP で cxcywh を回帰。L1/GIoU により head 適応後、言語・visual merger・head を学習。'),
 media('Image + referring expression','Native pixels','Not documented','Not documented','Head adaptation + joint language/merger/head training',
       'No RLCD; L1/GIoU supervision','One-pass box regression; no multi-Q reuse established',groundsource,
       notes('Dynamic Options and Native Probability are absent in this scoped path. Bbox accuracy and inference speed are author results, not directly comparable to Choice accuracy or calibrated probabilities.',
             '当前路径没有 Dynamic Options 或 Native Probability。bbox 精度和速度是作者实验，不能与 Choice 准确率或校准概率直接比较。',
             'この経路には Dynamic Options と Native Probability がない。bbox の精度・速度は作者の実験であり Choice 正答率や校正確率とは別の指標。'),
       'https://huggingface.co/xyzzzh/GroundingJev'),
 hf='https://huggingface.co/xyzzzh/GroundingJev',outputs=['Regression'],
 props={'dynamic':'no','variable':'no','native':'no','calibration':'no','multi_q':'no','parallel_q':'no'},
 rl_status='Supervised weighted L1/GIoU; not RLCD'))

path=ROOT/'data/projects.yaml'
raw=path.read_text(encoding='utf-8')
data=yaml.safe_load(raw)
by_id={p['id']:p for p in data['projects']}
assert len(by_id)==22 and not any(p['id'] in by_id for p in new)

# Update only four existing rows; retain the other historical audit records unchanged.
changed={}
source='https://github.com/Mapika/decider/blob/23579f7a7e8f10e1045be492af3c1c05a005d67c/MODEL_CARD_VISION.md'
p=by_id['decider']
p['params']='0.8B / 2B / 4B / 34.7B total, 3B active (MoE)'
p['media']=media('Text; optional native-image variant','Native decider-2b-vision','Game frames; no general video claim','Not documented',
 'Vision: v5 text transplant + supervised tuning + PPO','Vision PPO from pixels; not vendor RLCD',
 'Vision answer slots; do not inherit current text-engine cache guarantees',source,
 notes('The vision card specifies v5 text weights, supervised multimodal data and then PPO on Breakout/Pong. Do not label it as current 2B v11 or inherit v10 belief-calibration results. The main repo now lists 4B v2.1, 2B v11 and September 27 GGUF support.',
       '视觉模型卡明确是 v5 文本权重移植、图文监督后在 Breakout/Pong 做 PPO。不是当前 2B v11，也不能继承 v10 的 belief 校准结果。主库已列出 4B v2.1、2B v11 与 9 月 27 日 GGUF 支持。',
       '視覚版は v5 の言語重み、マルチモーダル教師学習、Breakout/Pong の PPO。2B v11 と同一ではなく v10 の belief 校正結果を引き継ぐとは言えない。主庫は 4B v2.1、2B v11、9/27 GGUF を追加。'),
 'https://huggingface.co/Mapika/decider-2b-vision')
p['evidence'] += [evidence(source,['vision_backbone','vision_training','ppo','version_scope'],'Author model card'),
 evidence('https://github.com/Mapika/decider/blob/main/README.md',['current_variants','gguf'],'Author changelog reviewed 2026-09-28')]
p['rl_status'] += '; 2026-09-28: vision is a separate v5-transplant + PPO path; 4B/35B and later text versions must be scoped separately'
changed[p['id']]=p
for id, source, m in [
 ('openjev-diffusiongemma','https://github.com/razorback16/openjev/blob/main/README.md',
  media('Text + image','Native; up to 8 images in documented API','Not documented','Not documented','Frozen DiffusionGemma readout','No Jev-specific RLCD',
  'Joint slots in chunks; optional sequential/think paths change semantics','https://github.com/razorback16/openjev/blob/main/README.md',
  notes('The default DiffusionGemma path reads masked answer slots. steps/samples and optional think/sequential modes are different compute paths; question independence is not guaranteed for joint slots. Laya/CLM/JevK5 endpoints are separately credited models, not DiffusionGemma variants.',
        '默认 DiffusionGemma 路径读取 masked 槽位；steps/samples 与 think/sequential 改变计算过程，联合槽位不保证问题独立。其 Laya/CLM/JevK5 端点是其他模型，不是 DiffusionGemma 变体。',
        '既定の DiffusionGemma は masked slot 読出し。steps/samples/think/sequential は別経路で、共同スロットは質問独立性を保証しない。他のモデル endpoint は DiffusionGemma の派生ではない。'),
  'https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4')),
 ('reflex','https://github.com/kshetrajna12/reflex/blob/main/README.md',
  media('Text + image','Native with vision checkpoint','Not established in reviewed stable path','Not documented','Frozen stable Qwen3.5-4B','No RLCD in stable path',
  'Shared state cache; independent question branches','https://github.com/kshetrajna12/reflex/blob/main/README.md',
  notes('The stable configuration uses frozen weights and two option orders. Earlier LoRA experiments are not its default release. A visual-capable checkpoint and actual image input are required.',
        'stable 配置使用冻结权重与两种候选顺序，早期 LoRA 实验不是当前默认版本；必须使用视觉 checkpoint 并实际输入图像。',
        'stable は凍結重みと 2 種の候補順序。過去の LoRA 実験は既定版ではない。視覚 checkpoint と実際の画像入力が必要。'))),
 ('litjev','https://github.com/zhengxuyu/litjev/blob/main/README.md',
  media('Text + image (checkpoint-dependent)','Native with vision checkpoint','Not established by reviewed documentation','Not documented','Frozen model; optional temperature fitting','No RLCD',
  'Model/backend-dependent; do not infer sharing from one API call','https://github.com/zhengxuyu/litjev/blob/main/README.md',
  notes('The documented default is Qwen3.8-27B. Screenshot decisions require a vision checkpoint; plain text checkpoints do not become visual through the wrapper. Probabilities are uncalibrated by default.',
        '文档默认 Qwen3.8-27B；截图决策必须使用视觉 checkpoint，普通文本模型不会因 wrapper 获得视觉能力。默认概率未校准。',
        '既定は Qwen3.8-27B。スクリーンショットには視覚 checkpoint が必要で、wrapper だけで text model は視覚化しない。既定確率は未校正。'))),
]:
    p=by_id[id]
    p['media']=m
    p['evidence'].append(evidence(source,['media_support','current_inference_scope'],'Author documentation reviewed 2026-09-28'))
    changed[id]=p

# Preserve unchanged YAML blocks and comments, rather than rewriting all historical entries.
blocks=re.split(r'(?m)(?=^- id: )', raw)
assert len(blocks)==23
blocks[0]=blocks[0].replace("checked_at: '2026-09-21'", "checked_at: '2026-09-28'\n# Targeted multimodal update; untouched historical rows retain the 2026-09-21 audit scope.",1)
for i in range(1,len(blocks)):
    obj=yaml.safe_load(blocks[i])[0]
    if obj['id'] in changed:
        blocks[i]=yaml.safe_dump([changed[obj['id']]], allow_unicode=True, sort_keys=False, width=160)
path.write_text(''.join(blocks).rstrip()+'\n'+yaml.safe_dump(new,allow_unicode=True,sort_keys=False,width=160),encoding='utf-8')
updated=yaml.safe_load(path.read_text())
assert len(updated['projects'])==32

papers=yaml.safe_load((ROOT/'data/papers.yaml').read_text())
recent=[
 dict(id='visual-jev-paper',title='Visual Jev: Accurate and Efficient Decisions from Shared Visual Context',date='2026-09-22',
      paper='https://arxiv.org/abs/2609.25845',code='https://github.com/guanxuyu-sv/Visual-Jev',topic='Native-image decisions / shared context',multimodal_related=True,
      notes=notes('Existing LM-head readout with answer SFT and shared visual-prefix execution; the paper date does not establish earliest code publication.',
                  '原有 LM head、答案 SFT 与视觉前缀共享；论文日期不等于最早代码公开日期。',
                  '既存 LM head、回答 SFT、視覚 prefix 共有。論文日付は最初のコード公開日を示さない。')),
 dict(id='pixeljev-paper',title='From Text Decisions to Pixels: An Study of Jev-Style Visual Choice Model',date='2026-09-24',
      paper='https://arxiv.org/abs/2609.29283',code=None,topic='Native-image choice / adaptation / calibration',multimodal_related=True,
      notes=notes('Primary abstract reviewed. Frozen readout, language adaptation and calibration are separate controls. Author code not verified; the pixel-art repository with the same name is unrelated.',
                  '依据一手摘要，区分冻结读出、语言适配与校准对照。未核实作者代码；同名像素画仓库不是论文实现。',
                  '一次摘要を確認。凍結読出し・言語適応・校正を区別。作者コード未確認。同名 pixel-art repo は論文実装ではない。')),
 dict(id='jev-mobile-paper',title='Jev-Mobile: Jev as an Executor for Mobile GUI Agents',date='2026-09-24',
      paper='https://arxiv.org/abs/2609.30186',code=None,topic='VLM planner + accessibility-tree decision executor',multimodal_related=True,
      notes=notes('Primary abstract reviewed. An agent system, not evidence that the Jev executor consumes raw screenshots. Canonical author code not verified.',
                  '依据一手摘要：VLM 规划器加 accessibility-tree 决策执行器，属于系统研究，不能证明 Jev 直接看截图；未核实作者代码。',
                  '一次摘要を確認。VLM planner と accessibility-tree executor のシステムで、Jev が画素を読む証拠ではない。作者コード未確認。')),
 dict(id='jev-wild-paper',title="Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem",date='2026-09-24',
      paper='https://arxiv.org/abs/2609.30216',code=None,topic='Ecosystem study; not a model',multimodal_related=True,
      notes=notes('Primary abstract reviewed. Surveys the ecosystem using a September 22 GitHub snapshot; repository counts are not counts of independent decision models.',
                  '依据一手摘要，使用 9 月 22 日 GitHub 快照研究生态；仓库总量不等于独立决策模型数量。',
                  '一次摘要を確認。9/22 の GitHub snapshot に基づく生態系分析で、repo 数は独立判断モデル数ではない。')),
]
assert not ({p['id'] for p in recent}&{p['id'] for p in papers['papers']})
papers['papers'].extend(recent)
papers['papers'].sort(key=lambda p:p['date'])
(ROOT/'data/papers.yaml').write_text('# SPDX-License-Identifier: CC-BY-4.0\n'+yaml.safe_dump(papers,allow_unicode=True,sort_keys=False,width=160),encoding='utf-8')

# Integrate one canonical modality renderer, retaining exactly four homepage sections.
p=ROOT/'scripts/generate_readme.py'
text=p.read_text(encoding='utf-8')
def replace_once(old,new):
    global text
    assert text.count(old)==1, ('Patch target changed',old[:100])
    text=text.replace(old,new,1)
replace_once('from github_stars import NOTICE, load_snapshot, star_cell\n',
 'from github_stars import NOTICE, load_snapshot, star_cell\nfrom multimodal_catalog import (MEDIA_LINK, MEDIA_GOALS, MEDIA_INSPECT, MEDIA_ROUTES,\n                                project_url, backbone_cell, render_multimodal)\n')
# Only link destinations use a fallback; GitHub star lookup continues to use github (including null).
assert text.count("({p['github']})") >= 3
text=text.replace("({p['github']})",'({project_url(p)})')
replace_once('p[\'release_date\'] or \'Unknown\', f"{p[\'backbone\']}<br>{p[\'params\']}",',
             "p['release_date'] or 'Unknown', backbone_cell(p),")
replace_once('\n\ndef load_data(root: Path = ROOT):',
 "\n\nfor _lang in LANGUAGES:\n    TEXT[_lang]['goals'] += MEDIA_GOALS[_lang]\n    TEXT[_lang]['inspect'] += MEDIA_INSPECT[_lang]\n    TEXT[_lang]['details'] += ' · ' + MEDIA_LINK[_lang]\nROUTES += MEDIA_ROUTES\n\n\ndef load_data(root: Path = ROOT):")
replace_once("'docs/updates.md': log}","'docs/updates.md': log, 'docs/multimodal.md': render_multimodal(data, papers)}")
text=text.replace('Technical audit: **{audit}**', 'Metadata update: **{audit}** (targeted multimodal review; older rows not fully re-audited)')
text=text.replace('技术核查：**{audit}**', '元数据更新：**{audit}**（本轮重点核查多模态，旧条目未全部重审）')
text=text.replace('技術検証：**{audit}**', 'メタデータ更新：**{audit}**（今回はマルチモーダル中心。旧項目の全面再検証ではありません）')
p.write_text(text,encoding='utf-8')

updates_path=ROOT/'data/updates.yaml'
updates=yaml.safe_load(updates_path.read_text())
updates['updates'].insert(0,dict(id='multimodal-review-20260928',date=DATE,kind='Added',url='docs/multimodal.md',
 summary=notes('Add ten source-backed visual/multimodal implementations, update four existing media paths and decider versions, and record four recent papers. Distinguish native audio, spectrogram images, video mosaics, one-token readout and task-specific grounding.',
               '新增十个有来源的视觉/多模态实现，更新四个旧项目的媒体路径与 decider 版本，补充四篇近期论文；区分原生音频、频谱图、视频拼图、单 token 读出和专用定位。',
               '根拠付きの視覚/マルチモーダル実装を 10 件追加し、既存 4 件の media 経路と decider の版、最近の論文 4 件を更新。音声・スペクトログラム・動画 mosaic・1 token 読出し・専用 grounding を区別。')))
updates_path.write_text(yaml.safe_dump(updates,allow_unicode=True,sort_keys=False,width=160),encoding='utf-8')

# Keep the new generated page synchronized during ordinary star refreshes and CI.
for relative in ('.github/workflows/refresh-stars.yml','.github/workflows/validate.yml'):
    path=ROOT/relative
    text=path.read_text()
    old='python scripts/test_presentation.py' if 'python scripts/test_presentation.py' in text else 'python3 scripts/test_presentation.py'
    if old in text:
        text=text.replace(old,old+'\n          '+old.replace('test_presentation.py','test_multimodal.py'))
    else:
        raise AssertionError('Presentation check missing in '+relative)
    if relative.endswith('refresh-stars.yml'):
        text=text.replace('docs/comparison.md docs/updates.md','docs/comparison.md docs/updates.md docs/multimodal.md')
        text=text.replace('      - scripts/test_presentation.py','      - scripts/test_presentation.py\n      - scripts/multimodal_catalog.py\n      - scripts/test_multimodal.py')
    path.write_text(text,encoding='utf-8')

# Supporting documents retain historical evidence and gain a clearly dated update note.
with (ROOT/'docs/audit.md').open('a',encoding='utf-8') as f:
    f.write('\n\n## Targeted update — 2026-09-28\n\nTen implementations were added and four existing media paths were reviewed. See [multimodal scope and sources](multimodal.md). The catalog now contains 32 rows (one official reference, 31 independent implementations), including one HF-hosted project without a verified canonical GitHub repo and one task-specific box-regression model. Four new paper records are maintained separately. The update did not rerun upstream models or globally re-audit every historical row. First-public dates remain unknown unless supported independently; paper/version milestones are not substituted.\n')
with (ROOT/'docs/training.md').open('a',encoding='utf-8') as f:
    f.write('\n\n## Multimodal additions — 2026-09-28\n\n[Valen source](https://github.com/Liuziyu77/Valen/blob/06251f9d9d3c06ea690be93b8696ccc66471f8c9/valen/training/rlcd.py) samples categorical actions, freezes old log-probabilities/rewards, applies a clipped group-relative policy loss, reference KL and direct Brier loss. Labels are available: this is a local RLCD-inspired design, not recovered TypeSafe training. Visual Jev (Yu/Yao) recommends answer SFT and the existing LM head. OmniJev/Qwen documents probability-scoring training and temperature calibration without an established RLCD stage. Jev-Spatial uses CE; GroundingJev uses L1/GIoU. The decider vision model card documents supervised tuning followed by PPO from pixels and a v5 language transplant, not the latest text-model checkpoint. Jev-Omni/Gemma has a public classifier and multimodal weights, but its complete training recipe/RLCD attribution was not verified. See [version-specific comparison](multimodal.md).\n')
with (ROOT/'CONTRIBUTING.md').open('a',encoding='utf-8') as f:
    f.write('\n\n## Multimodal evidence\n\nOptional `media` records in `data/projects.yaml` drive the modality tags and `docs/multimodal.md`. Include `summary`, `image`, `video`, `audio`, `training`, `rl`, `execution`, `source`, `checked_at` and `notes.en/zh/ja`. The source must also appear in project evidence. Distinguish native pixels/audio, frame sampling, mosaics, spectrogram images and text mediation. One generated label token is not zero-token readout; a game replay is not closed-loop control. `github: null` is allowed for inspectable HF-hosted code/weights when no canonical GitHub repo is verified; supply the real `website`/`huggingface` link, and do not substitute HF likes for GitHub Stars. Run `python scripts/test_multimodal.py` alongside existing validation.\n')
print('Applied source-backed multimodal update: 10 additions, 4 media updates, 4 papers. Regenerate and validate before publishing.')
