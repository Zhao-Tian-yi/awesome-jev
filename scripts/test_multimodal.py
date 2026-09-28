# SPDX-License-Identifier: MIT
"""Checks for source-backed modality fields and HF-only project links."""
import datetime as dt
import unittest

import generate_readme as g
from github_stars import load_snapshot, star_cell
from multimodal_catalog import MEDIA_ROUTES, project_url, render_multimodal


class MultimodalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data, cls.papers, cls.lists = g.load_data()
        cls.by_id = {p['id']: p for p in cls.data['projects']}

    def test_evidence_and_localizations(self):
        for p in self.data['projects']:
            if not p.get('media'):
                continue
            m = p['media']
            for key in ('summary', 'image', 'video', 'audio', 'training', 'rl', 'execution', 'source', 'checked_at'):
                self.assertTrue(m[key], (p['id'], key))
            self.assertLessEqual(dt.date.fromisoformat(m['checked_at']), dt.date.fromisoformat(self.data['checked_at']))
            self.assertEqual(set(m['notes']), set(g.LANGUAGES))
            self.assertIn(m['source'], {e['url'] for e in p['evidence']})

    def test_hf_is_not_github(self):
        p = self.by_id['jev-omni']
        self.assertIsNone(p['github'])
        self.assertEqual(project_url(p), 'https://huggingface.co/akhilaaa3/Jev-Omni')
        self.assertEqual(star_cell(p['github'], load_snapshot()), '—')
        self.assertNotIn('](None)', g.landscape(self.data['projects'], load_snapshot()))

    def test_modality_boundaries(self):
        self.assertIn('Spectrogram', self.by_id['omnijev']['media']['audio'])
        self.assertIn('mosaic', self.by_id['omnijev']['media']['video'])
        self.assertIn('Native', self.by_id['jev-omni']['media']['audio'])
        self.assertIn('Unsupported', self.by_id['openjev-multimodal']['media']['audio'])
        self.assertEqual(self.by_id['groundingjev']['properties']['native'], 'no')
        self.assertEqual(self.by_id['groundingjev']['properties']['dynamic'], 'no')
        self.assertEqual(self.by_id['openjev-multimodal']['ar'], 'Yes')

    def test_route_targets_exist(self):
        for ids, path in MEDIA_ROUTES:
            self.assertEqual(path, 'docs/multimodal.md')
            for project_id in ids:
                self.assertIn(project_id, self.by_id)

    def test_no_unrelated_pixel_art_model(self):
        self.assertNotIn('https://github.com/joce-unity/pixeljev', [p['github'] for p in self.data['projects']])
        self.assertIsNone(next(p for p in self.papers if p['id'] == 'pixeljev-paper')['code'])

    def test_generated_document(self):
        text = render_multimodal(self.data, self.papers)
        self.assertEqual(text, g.outputs()['docs/multimodal.md'])
        for p in self.data['projects']:
            if p.get('media'):
                self.assertIn('### ' + p['id'], text)
                self.assertIn(p['media']['source'], text)
        for page in ('README.md', 'README.zh-CN.md', 'README.ja.md'):
            self.assertIn('docs/multimodal.md', g.outputs()[page])


if __name__ == '__main__':
    unittest.main(verbosity=2)
