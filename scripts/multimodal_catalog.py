# SPDX-License-Identifier: MIT
"""Render modality evidence from the canonical project and paper records."""
from __future__ import annotations

MEDIA_LINK = {
    'en': '[Multimodal models: image, video, audio and grounding](docs/multimodal.md)',
    'zh': '[多模态专题：图像、视频、音频与定位](docs/multimodal.md)',
    'ja': '[マルチモーダル：画像・動画・音声・位置推定](docs/multimodal.md)',
}
MEDIA_GOALS = {
    'en': ['Start with image-native decisions', 'Train visual decisions and inspect RL', 'Study spatial decisions and grounding', 'Compare video and audio input paths'],
    'zh': ['直接使用图像决策', '训练视觉决策与核查 RL', '研究空间决策与视觉定位', '比较视频与音频输入路径'],
    'ja': ['画像から直接判断する', '視覚判断の学習と RL を調べる', '空間判断と位置推定を調べる', '動画と音声の入力経路を比較する'],
}
MEDIA_INSPECT = {
    'en': ['Pixels versus captions; cache reuse', 'LM head versus learned head; sampled RL versus calibration loss', 'Choice grids versus direct box regression', 'Sampled frames, mosaics, spectrograms and native audio'],
    'zh': ['像素输入与文字转述；缓存复用', '原有 LM head 与新决策头；采样 RL 与校准损失', '分层网格选择与直接边界框回归', '采样帧、拼图、频谱图与原生音频'],
    'ja': ['画素入力とテキスト化・キャッシュ再利用', '既存 LM head と学習済み head・RL と校正損失', '階層的グリッド選択と直接 bbox 回帰', 'フレーム抽出・モザイク・スペクトログラム・音声入力'],
}
MEDIA_ROUTES = [
    (['jev-visual-mlx', 'llm2jev', 'openjev-multimodal'], 'docs/multimodal.md'),
    (['visual-jev-yu', 'valen', 'omnijev'], 'docs/multimodal.md'),
    (['jev-spatial', 'groundingjev'], 'docs/multimodal.md'),
    (['jev-omni', 'omnijev', 'valen'], 'docs/multimodal.md'),
]


def project_url(project):
    """HF-hosted code is not a GitHub repository and must not receive fake stars."""
    for field in ('github', 'website', 'huggingface', 'paper'):
        if project.get(field):
            return project[field]
    raise ValueError('Project has no public source: ' + project['id'])


def backbone_cell(project):
    text = f"{project['backbone']}<br>{project['params']}"
    media = project.get('media')
    if media:
        text += '<br>Input: ' + media['summary']
    return text


def render_multimodal(data, papers):
    def esc(value):
        return str(value).replace('|', r'\|').replace('\n', ' ')

    def table(headers, rows):
        return '\n'.join(['| ' + ' | '.join(headers) + ' |',
                          '|' + '|'.join('---' for _ in headers) + '|'] +
                         ['| ' + ' | '.join(esc(x) for x in row) + ' |' for row in rows])

    projects = [p for p in data['projects'] if p.get('media')]
    parts = ['# Multimodal Jev research map / 多模态 Jev 专题',
             '[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Full comparison](comparison.md) · [Training audit](training.md)',
             'Targeted source review: **2026-09-28**. This page is generated from `data/projects.yaml` and `data/papers.yaml`. It does not add a fifth README section. Unlisted or unreviewed modalities are not silently treated as supported.',
             '## Read the input path, not the model name',
             'A native-image decision model sends pixels/visual features into its backbone. A system that first produces OCR, captions, an accessibility tree or simulator state and then sends text to Jev is a multimodal application, not evidence that the decision backbone sees pixels. Camera-frame decisions do not by themselves establish temporal video understanding.',
             'Video frames, a frame mosaic and a dedicated video input path are different representations. Likewise, a spectrogram rendered as an image is not a native audio encoder. API parallelism is not proof of one total forward pass or shared backbone computation. Absence of text decoding does not imply diffusion.',
             '中文口径：直接看图、采样帧、视频拼图、音频频谱图、原生音频及文字中介分别记录；演示回放不等于闭环控制，输出概率也不等于已经校准。',
             '## Input and execution comparison']
    rows = []
    for p in projects:
        m = p['media']
        rows.append([f"[{p['name']}]({project_url(p)})", m['image'], m['video'], m['audio'],
                     m['training'], m['rl'], m['execution'],
                     f"[Evidence](#{p['id']})"])
    parts.append(table(['Project / reviewed path', 'Image', 'Video', 'Audio', 'Training', 'RL evidence', 'Execution / sharing', 'Notes'], rows))
    parts += ['## Version-specific evidence',
              'A family-level training label must not be inherited by every media checkpoint. The entries below state the reviewed variant; benchmark numbers were not rerun.']
    for p in projects:
        m = p['media']
        parts += ['### ' + p['id'], f"**[{p['name']}]({project_url(p)})** · Media checked: {m['checked_at']}",
                  p['notes']['en'], '**Multimodal scope:** ' + m['notes']['en'],
                  '**中文：** ' + m['notes']['zh'],
                  '**日本語：** ' + m['notes']['ja'],
                  f"[Primary source]({m['source']}) · [All evidence](evidence.md#{p['id']})"]
        if m.get('artifact'):
            parts.append(f"[Reviewed media artifact]({m['artifact']})")
    parts += ['## Recent papers and systems',
              'Dates here are arXiv v1 dates, not guessed first-public repository dates. Abstract-level evidence is distinguished from inspected repository material.']
    selected = [p for p in papers if p.get('multimodal_related')]
    parts.append(table(['arXiv v1', 'Paper', 'Scope', 'Code / boundary'], [
        [p['date'], f"[{p['title']}]({p['paper']})", p['topic'],
         (f"[Author code]({p['code']})" if p.get('code') else 'Author code not verified') + '; ' + p['notes']['en']]
        for p in selected]))
    parts += ['## Name collisions and inclusion boundaries',
              '- **Visual Jev is not a unique project name.** The Guanxu Yu/Yuhang Yao paper uses `guanxuyu-sv/Visual-Jev`; `andrueandersoncs/visual-jev` is an independent pointer-head implementation; `hr98w/jev-visual` is a frozen MLX implementation. They are not interchangeable releases.',
              '- **OmniJev is not Jev-Omni.** The Qwen-based `tinnel123666888/OmniJev` and the Gemma-based `akhilaaa3/Jev-Omni` are different projects. The latter currently has verified HF-hosted inference code and weights, not a verified canonical GitHub repository. Its Stars cell is therefore a dash, not HF likes or an unrelated repository count.',
              '- **PixelJev paper versus pixel-art app.** The [PixelJev paper](https://arxiv.org/abs/2609.29283) is about native-image choice prediction. [joce-unity/pixeljev](https://github.com/joce-unity/pixeljev) instead calls hosted Jev to select pixel-art shape attributes. That app is not the paper code and is not added as a separate decision backbone.',
              '- **GroundingJev is task-specific.** It predicts continuous boxes rather than a distribution over runtime options. It is included as explicit Jev-inspired model research, with Dynamic Options and Native Probability marked absent; it is not a generic Noul/Choice/Score substitute.',
              '- **Jev-Mobile is a system.** Its VLM planner plus accessibility-tree executor does not establish pixel input to the Jev executor. It remains related research, not a new multimodal Jev checkpoint.',
              '- These third-party implementations do not reveal TypeSafe Jev\'s undisclosed architecture. Neither a diffusion-based community implementation nor a visual demo proves that the official model is diffusion or natively multimodal.',
              '## Evaluation requirements',
              'Use matched inputs, candidates, model versions, image resolution and hardware. Report single-request latency separately from batch-amortized time; include visual encoding and cache warm/cold costs. Replays, scripted candidate shortlists and cropped-image rounds must be disclosed. Test image removal/shuffling, wrong-image controls, blur, unseen questions/options and distribution shift; do not infer calibration from a confidence drop in one blur demo. Report accuracy, NLL/Brier, calibration and risk-coverage separately. Regional choices, pointing hit-rate and continuous-box IoU are not interchangeable metrics.',
              '## Remaining gaps',
              'Most first-public repository dates remain unverified; later papers, checkpoint labels and repository creation times are not substitutes. The HF Jev-Omni checkpoint is inspectable, but a complete reproducible training recipe and RLCD attribution were not established. This review inspected selected source blocks and author documentation; no upstream training, GPU inference or benchmark was rerun. Older rows without a media record were not exhaustively re-audited.']
    return '\n\n'.join(parts) + '\n'
