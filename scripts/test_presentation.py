#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Offline regression checks for the four-section homepage and retained details."""
from __future__ import annotations

import copy
import re
import unittest
from urllib.parse import parse_qs, urlsplit

import yaml
import generate_readme as g
from github_stars import NOTICE, load_snapshot


def block(text, marker):
    return text.split(f'<!-- {marker}:start -->', 1)[1].split(f'<!-- {marker}:end -->', 1)[0]


def cells(line):
    return [x.strip() for x in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


class PresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data, cls.papers, cls.lists = g.load_data()
        cls.snapshot = load_snapshot()
        cls.updates = g.load_updates()
        cls.pages = {lang: g.render_readme(lang, cls.data, cls.papers, cls.lists, cls.snapshot, cls.updates)
                     for lang in g.LANGUAGES}
        cls.generated = g.outputs()

    def test_eight_column_landscape(self):
        for text in self.pages.values():
            rows = [line for line in block(text, 'landscape').splitlines() if line.startswith('|')]
            self.assertEqual(len(rows), len(self.data['projects']) + 2)
            self.assertTrue(all(len(cells(row)) == 8 for row in rows))
            self.assertEqual(cells(rows[0])[1], 'GitHub Stars')

    def test_official_first_and_order_unchanged(self):
        expected = [p['name'] for p in g.ordered(self.data['projects'])]
        for text in self.pages.values():
            rows = [line for line in block(text, 'landscape').splitlines() if line.startswith('|')][2:]
            actual = [re.match(r'\[([^]]+)\]', cells(row)[0]).group(1) for row in rows]
            self.assertEqual(actual, expected)
            self.assertEqual(actual[0], 'Official Jev')

    def test_technical_tables_identical(self):
        self.assertEqual(len({block(text, 'landscape') for text in self.pages.values()}), 1)

    def test_three_language_url_parity(self):
        links = [set(re.findall(r'\]\(([^)]+)\)', text)) for text in self.pages.values()]
        self.assertTrue(all(x == links[0] for x in links))

    def test_notice_and_navigation(self):
        for lang, text in self.pages.items():
            self.assertTrue(text.startswith('# Awesome Jev\n\n> ' + NOTICE[lang]))
            self.assertIn('README.zh-CN.md', text)
            for target in ('models', 'start-here', 'official', 'awesome-awesome-jev'):
                self.assertIn(f'<a id="{target}"></a>', text)
                self.assertIn(f'](#{target})', text)
            self.assertNotIn('](#updates)', text)
            self.assertNotIn('](#contributing)', text)

    def test_exactly_four_sections(self):
        for lang, text in self.pages.items():
            expected = [g.TEXT[lang]['models'], g.TEXT[lang]['start'],
                        g.TEXT[lang]['official'], 'Awesome Awesome Jev 😄']
            self.assertEqual(re.findall(r'^## (.+)$', text, re.MULTILINE), expected)
            self.assertNotIn('<details>', text)
            self.assertNotIn('Jevenator', text)
            self.assertNotIn('arxiv.org', text)

    def test_capabilities_moved_to_details(self):
        for text in self.pages.values():
            self.assertNotIn('<!-- properties:start -->', text)
        comparison = self.generated['docs/comparison.md']
        self.assertEqual(block(comparison, 'properties').strip(), g.property_table(self.data['projects']))
        rows = [line for line in block(comparison, 'properties').splitlines() if line.startswith('|')]
        self.assertEqual(len(rows), len(self.data['projects']) + 2)

    def test_artifact_meaning(self):
        p = copy.deepcopy(next(x for x in self.data['projects'] if not x['official']))
        p.update(weights='No', training='None', huggingface=None)
        self.assertIn('Upstream model', g.artifact(p))
        p.update(training='SFT')
        self.assertEqual(g.artifact(p), 'No project-weight release')
        p.update(weights='Partial', huggingface='https://example.org/head')
        self.assertIn('Adapter/head', g.artifact(p))
        p.update(weights='Unknown')
        self.assertEqual(g.artifact(p), 'Availability unverified')

    def test_full_technical_fields_retained(self):
        text = g.full_table(self.data['projects'])
        self.assertIn('AR Decoding', text)
        self.assertIn(text, self.generated['docs/comparison.md'])
        for p in self.data['projects']:
            for key in ('backbone', 'params', 'architecture', 'training', 'rl', 'decision_mechanism'):
                self.assertIn(g.esc(p[key]), text)

    def test_date_and_audit_boundaries(self):
        for text in self.pages.values():
            self.assertIn(self.data['checked_at'], text)
            self.assertIn(self.snapshot['checked_at'], text)
            self.assertIn('docs/audit.md', text)
        for p in self.data['projects']:
            if p['release_date'] is None:
                row = next(line for line in block(self.pages['en'], 'landscape').splitlines()
                           if line.startswith('| [' + p['name'] + ']'))
                self.assertEqual(cells(row)[2], 'Unknown')

    def test_updates_retained_off_homepage(self):
        log = self.generated['docs/updates.md']
        for entry in self.updates:
            self.assertIn(entry['summary']['en'], log)
        for lang, text in self.pages.items():
            self.assertNotIn('docs/updates.md', text)
            for entry in self.updates:
                self.assertNotIn(entry['summary'][lang], text)
        self.assertEqual([e['date'] for e in self.updates], sorted([e['date'] for e in self.updates], reverse=True))

    def test_evidence_correction_links(self):
        text = g.render_evidence(self.data)
        targets = re.findall(r'\[Report a correction\]\(([^)]+)\)', text)
        self.assertEqual(len(targets), len(self.data['projects']))
        for target, project in zip(targets, g.ordered(self.data['projects'])):
            query = parse_qs(urlsplit(target).query)
            self.assertEqual(query['project'], [project['name']])
            self.assertEqual(query['template'], ['metadata-correction.yml'])

    def test_issue_templates(self):
        for filename in ('suggest-project.yml', 'metadata-correction.yml'):
            data = yaml.safe_load((g.ROOT / '.github/ISSUE_TEMPLATE' / filename).read_text())
            self.assertTrue(data['name'] and data['description'])
            ids = [field['id'] for field in data['body'] if 'id' in field]
            self.assertEqual(len(ids), len(set(ids)))
            self.assertIn('evidence', ids)

    def test_final_easter_egg_and_star_columns(self):
        for text in self.pages.values():
            self.assertEqual(text.rsplit('\n## ', 1)[-1].splitlines()[0], 'Awesome Awesome Jev 😄')
            self.assertEqual(text.count('| GitHub Stars |'), 2)

    def test_no_mutation_of_source_facts(self):
        before = copy.deepcopy((self.data, self.papers, self.lists, self.snapshot, self.updates))
        for lang in g.LANGUAGES:
            g.render_readme(lang, self.data, self.papers, self.lists, self.snapshot, self.updates)
        self.assertEqual((self.data, self.papers, self.lists, self.snapshot, self.updates), before)

    def test_navigation_anchors_exist(self):
        for text in self.pages.values():
            anchors = set(re.findall(r'<a id="([^"]+)"></a>', text))
            for target in re.findall(r'\]\(#([^)]+)\)', text):
                self.assertIn(target, anchors)


if __name__ == '__main__':
    unittest.main(verbosity=2)
