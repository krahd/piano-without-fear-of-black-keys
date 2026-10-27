"""Validate actual manuscript tables, independently of the PDF renderer.

Run: python3 -m unittest discover -s tests -v
"""
from collections import Counter
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
LETTERS = 'CDEFGAB'
NATURALS = (0, 2, 4, 5, 7, 9, 11)
ROOTS = 'C Db D Eb E F F# G Ab A Bb B'.split()
CHORDS = {
    'Major triad': '1 3 5', 'Minor triad': '1 b3 5',
    'Diminished triad': '1 b3 b5', 'Augmented triad': '1 3 #5',
    'Major 7': '1 3 5 7', 'Dominant 7': '1 3 5 b7',
    'Minor 7': '1 b3 5 b7', 'Half-diminished 7': '1 b3 b5 b7',
    'Diminished 7': '1 b3 b5 bb7',
}


def accidental(text):
    return text.count('#') - text.count('b')


def pitch(note):
    match = re.fullmatch(r'([A-G])([#b]*)', note)
    if not match:
        raise ValueError(f'Invalid note: {note!r}')
    return (NATURALS[LETTERS.index(match[1])] + accidental(match[2])) % 12


def discrepancies(root, formula, notes):
    degrees, notes = formula.split(), notes.split()
    if len(degrees) != len(notes):
        return [f'length: {len(degrees)} degrees, {len(notes)} notes']
    errors = []
    for degree, note in zip(degrees, notes):
        m = re.fullmatch(r'([#b]*)([1-9][0-9]*)', degree)
        if not m:
            raise ValueError(f'Invalid degree: {degree!r}')
        index = (int(m[2]) - 1) % 7
        letter = LETTERS[(LETTERS.index(root[0]) + index) % 7]
        expected_pc = (pitch(root) + NATURALS[index] + accidental(m[1])) % 12
        if note[0] != letter:
            errors.append(f'{degree}: {note} has wrong letter; expected {letter}')
        if pitch(note) != expected_pc:
            errors.append(f'{degree}: {note} has wrong pitch class; expected {expected_pc}')
    return errors


def rows(text):
    """Yield each scale row or chord-family cell in Appendices A-C."""
    appendix = section = None
    header = None
    for line in text.splitlines():
        if line.startswith('# Appendix '):
            appendix = line.split()[2]
        if line.startswith('##'):
            section = line.lstrip('# ').strip()
            header = None
        if appendix not in ('A', 'B', 'C') or not line.startswith('|'):
            continue
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if cells[0] == 'Root':
            header = cells
            continue
        if set(cells[0]) <= {'-', ':'}:
            continue
        if header is None or len(cells) != len(header):
            raise ValueError(f'Malformed table: {line}')
        root = cells[0]
        if appendix in ('A', 'B'):
            if header != ['Root', 'Degree formula', 'Notes']:
                raise ValueError(f'Unexpected scale header: {header}')
            yield appendix, section, root, cells[1], cells[2]
        else:
            for family, notes in zip(header[1:], cells[1:]):
                yield appendix, family, root, CHORDS[family], notes


class PitchTables(unittest.TestCase):
    def test_all_scale_and_chord_cells(self):
        entries = list(rows((ROOT/'piano_transposition_manual.md').read_text()))
        # 84 modal rows + 96 scale rows + 108 chord-family cells.
        self.assertEqual(Counter(r[0] for r in entries), {'A': 84, 'B': 96, 'C': 108})
        groups = {}
        for appendix, family, root, formula, notes in entries:
            groups.setdefault((appendix, family), []).append(root)
            with self.subTest(appendix=appendix, family=family, root=root):
                self.assertEqual(discrepancies(root, formula, notes), [])
        for group, roots in groups.items():
            self.assertEqual(roots, ROOTS, group)

    def test_whole_tone_has_explicit_flat_sevenths(self):
        entries = [r for r in rows((ROOT/'piano_transposition_manual.md').read_text())
                   if r[:2] == ('B', 'Whole tone')]
        self.assertEqual([r[4].split()[-1] for r in entries],
                         'Bb Cb C Db D Eb E F Gb G Ab A'.split())
        self.assertTrue(all(r[3] == '1 2 3 #4 #5 b7' for r in entries))

    def test_enharmonic_error_is_distinct_from_pitch_error(self):
        self.assertEqual(discrepancies('C', 'b7', 'A#'),
                         ['b7: A# has wrong letter; expected B'])
        self.assertEqual(discrepancies('C', 'b7', 'B'),
                         ['b7: B has wrong pitch class; expected 10'])
        self.assertEqual(discrepancies('Db', 'b7', 'Cb'), [])
        self.assertEqual(discrepancies('B', '#5 bb7', 'F## Ab'), [])
        self.assertTrue(discrepancies('C', '1 3 5', 'C E'))

    def test_convenience_scale_source_matches_canonical(self):
        text = (ROOT/'piano_transposition_manual.md').read_text()
        appendix = text.split('# Appendix B -', 1)[1].split('# Appendix C -', 1)[0]
        canonical_rows = [line for line in appendix.splitlines() if line.startswith('|')]
        convenience_rows = [line for line in (ROOT/'03_appendix_scales.md').read_text().splitlines()
                            if line.startswith('|')]
        self.assertEqual(canonical_rows, convenience_rows)


if __name__ == '__main__':
    unittest.main()
