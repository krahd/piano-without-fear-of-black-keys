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

**Current public PDF (v1.3.1):** [`Piano_Without_Fear_of_Black_Keys.pdf`](Piano_Without_Fear_of_Black_Keys.pdf). This stable filename is linked from laurenzo.net.

Version 1.3 changes: register is now an explicit layer between pitch spelling and instrument geometry; movable-shape pedagogy is counterbalanced by fixed-register drills for guitar/Push/Note; ASCII transformation arrows are replaced by typographic arrows; typography and table spacing are refined.

Version 1.2 changes: author/contact on the cover; compact preface with reading paths, first-ten-minutes exercise, symbol guide, and beginner glossary; local decoding of chord symbols and Roman-numeral progressions; small language simplifications for first-time musicians. The theoretical scope and practice architecture are otherwise unchanged.


## Editions

- **v1.3.1 (current, 53 pages, 160 × 230 mm):** [stable public PDF](Piano_Without_Fear_of_Black_Keys.pdf), with an [identical explicitly versioned PDF](edition-design/v1.3.1/Piano_Without_Fear_of_Black_Keys_v1.3.1.pdf). The original instructional content and SVG teaching diagrams are retained; the book is retypeset with 10 pt Noto Serif and mirrored binding margins. See [edition notes](edition-design/v1.3.1/README.md).
- **v1.3 (archived A4 original):** [historical PDF](edition-design/v1.3/Piano_Without_Fear_of_Black_Keys_v1.3.pdf). Its canonical manuscript `piano_transposition_manual.md` and historical stylesheet `style.css` remain unchanged. The [v1.3 build script](edition-design/v1.3/build.sh) remains available.

The term *transposition-first* and the book's overall pedagogical framing are reserved for reconsideration in [v1.4](https://github.com/krahd/piano-without-fear-of-black-keys/issues/5).

## Build

To reproduce **the current public v1.3.1 PDF** at the stable root filename, run from the repository root:

```sh
./build.sh
```

This invokes `edition-design/v1.3.1/build.py` and copies the resulting versioned PDF to `Piano_Without_Fear_of_Black_Keys.pdf`. Requirements: Python 3 with BeautifulSoup4 and WeasyPrint, Pandoc, and the documented book fonts. The old v1.3 build is separate: `sh edition-design/v1.3/build.sh`; it writes only to the archived versioned PDF, not the public filename.

## Pitch notation

The book uses scientific pitch notation with middle C = C4. Some software and hardware use different octave-number labels for the same MIDI pitches; the octave numbers here follow the book's stated convention rather than a product-specific display convention.

## Related projects

This book is a standalone publication within the same broader line of work as [Musifold](https://github.com/krahd/musifold), the interactive cross-instrument music-geometry application. Musifold grew out of [Ableton Note Helper](https://github.com/krahd/ableton-note-helper), which remains the narrower Ableton Note/Push reference tool.

The book is not the Musifold application and is not intended to serve as the future Musifold book.

