# Piano Without Fear of Black Keys

Canonical source: `piano_transposition_manual.md`.

Convenience source files:
- `01_foundations_and_instruments.md` (cover, preface, Parts I-VII)
- `02_appendix_modes.md`
- `03_appendix_scales.md`
- `04_appendix_chords_progressions_drills.md`
- `05_appendix_negative_harmony.md`
- `06_sources_and_notes.md`

`assets/` contains original vector teaching diagrams. `style.css` controls the PDF export.

**Current public PDF (v1.3.3):** [`Piano_Without_Fear_of_Black_Keys.pdf`](Piano_Without_Fear_of_Black_Keys.pdf). This stable filename is linked from laurenzo.net.

Version 1.3 changes: register is now an explicit layer between pitch spelling and instrument geometry; movable-shape pedagogy is counterbalanced by fixed-register drills for guitar/Push/Note; ASCII transformation arrows are replaced by typographic arrows; typography and table spacing are refined.

Version 1.2 changes: author/contact on the cover; compact preface with reading paths, first-ten-minutes exercise, symbol guide, and beginner glossary; local decoding of chord symbols and Roman-numeral progressions; small language simplifications for first-time musicians. The theoretical scope and practice architecture are otherwise unchanged.


## Maintenance editions: v1.3.2 and v1.3.3

v1.3.2 corrected the twelve whole-tone flat-seventh spellings without changing pitches. v1.3.3 repairs the remaining documented pedagogy, controller, reference-layout, accessibility and historical-build issues. The public download filename remains stable. See [v1.3.3 release notes](edition-design/v1.3.3/README.md).

Run `python3 -m unittest discover -s tests -v` to check all 180 scale rows and 108 chord-family cells in Appendices A-C. The maintenance build runs these checks before rendering. See [review and release notes](edition-design/v1.3.2/README.md).

## Editions

- **v1.3.3 (current, 55 pages, 160 × 230 mm):** [versioned PDF](edition-design/v1.3.3/Piano_Without_Fear_of_Black_Keys_v1.3.3.pdf), with the same public filename, a corrected typesetting and a [structured HTML edition](edition-design/v1.3.3/Piano_Without_Fear_of_Black_Keys_v1.3.3.html).
- **v1.3.2 (archived, 53 pages, 160 × 230 mm):** [versioned PDF](edition-design/v1.3.2/Piano_Without_Fear_of_Black_Keys_v1.3.2.pdf), using the unchanged v1.3.1 CSS and original SVGs.
- **v1.3.1 (archived, 53 pages, 160 × 230 mm):** [historical versioned PDF](edition-design/v1.3.1/Piano_Without_Fear_of_Black_Keys_v1.3.1.pdf). The original instructional content and SVG teaching diagrams are retained; the book is retypeset with 10 pt Noto Serif and mirrored binding margins. See [edition notes](edition-design/v1.3.1/README.md).
- **v1.3 (archived A4 original):** [historical PDF](edition-design/v1.3/Piano_Without_Fear_of_Black_Keys_v1.3.pdf). The historical stylesheet `style.css` remains unchanged; the canonical manuscript now includes the maintenance errata. The [v1.3 build script](edition-design/v1.3/build.sh) remains available.

The transposition-first premise and both intended reading routes remain unchanged. A [separate successor book](successor-book/CONCEPT.md) explores instrumental geometry and musical knowledge; it is not version 1.4 of this manual.

## Build

To reproduce **the v1.3.3 book PDF** at the stable root filename, run from the repository root:

```sh
./build.sh
```

This invokes `edition-design/v1.3.3/build.py` and copies the resulting versioned PDF to `Piano_Without_Fear_of_Black_Keys.pdf`. Requirements: Pandoc, Noto Serif/Lato fonts and a Python interpreter with packages from `requirements-book.txt`. `./build.sh` uses an existing compatible interpreter or an isolated `uv` environment; `BOOK_PYTHON` explicitly selects an already configured interpreter. No global Python installation is required. Historical v1.3/v1.3.1/v1.3.2 builders read frozen sources and figures and output only to their `rebuild/` directories, never overwriting archived release PDFs.

## Editorial work

- [v1.3.2 critical audit](audits/v1.3.2-2026-10-28.md) and [v1.3.3 applied corrections](edition-design/v1.3.3/README.md). The transposition-first purpose and both reading paths remain intact.
- [Separate successor-book concept](successor-book/CONCEPT.md), descended from this manual but concerned with instrumental geometry and what musicians know through playing. It is **not** version 1.4, not the absolute-beginner preparatory companion, and not yet a finished book or separately named repository.

## Pitch notation

The book uses scientific pitch notation with middle C = C4. Some software and hardware use different octave-number labels for the same MIDI pitches; the octave numbers here follow the book's stated convention rather than a product-specific display convention.

## Related projects

This book is a standalone publication within the same broader line of work as [Musifold](https://github.com/krahd/musifold), the interactive cross-instrument music-geometry application. Musifold grew out of [Ableton Note Helper](https://github.com/krahd/ableton-note-helper), which remains the narrower Ableton Note/Push reference tool.

The book is not the Musifold application and is not intended to serve as the future Musifold book.

