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

Exported reference: `Piano_Without_Fear_of_Black_Keys.pdf`.

Version 1.3 changes: register is now an explicit layer between pitch spelling and instrument geometry; movable-shape pedagogy is counterbalanced by fixed-register drills for guitar/Push/Note; ASCII transformation arrows are replaced by typographic arrows; typography and table spacing are refined.

Version 1.2 changes: author/contact on the cover; compact preface with reading paths, first-ten-minutes exercise, symbol guide, and beginner glossary; local decoding of chord symbols and Roman-numeral progressions; small language simplifications for first-time musicians. The theoretical scope and practice architecture are otherwise unchanged.


## Editions

- **[v1.3.1 — complete book-typeset PDF](edition-design/v1.3.1/Piano_Without_Fear_of_Black_Keys_v1.3.1.pdf)** (53 pages; 160 × 230 mm; October 2026). This edition retains the existing v1.3 instructional text and original SVG teaching diagrams while applying conventional book typography, 10 pt Noto Serif, mirrored binding margins, and the approved cover. Rebuild instructions and verification are in [the v1.3.1 edition directory](edition-design/v1.3.1/README.md).
- **v1.3 — original A4 manual:** `Piano_Without_Fear_of_Black_Keys.pdf` and `piano_transposition_manual.md`, preserved without changes. The root `./build.sh` continues to build this original edition.

The broader question of whether *transposition-first* is the right organising premise is reserved for [v1.4](https://github.com/krahd/piano-without-fear-of-black-keys/issues/5).

## Build

The PDF is reproducible from the canonical Markdown and `style.css` with Pandoc plus either WeasyPrint or Chromium:

```sh
./build.sh
```

`build.sh` prefers an installed `weasyprint`; on macOS it falls back to `/Applications/Chromium.app/Contents/MacOS/Chromium`, and on other systems it can use a `chromium` executable on `PATH`. The build regenerates `book.html` and `Piano_Without_Fear_of_Black_Keys.pdf`.

## Pitch notation

The book uses scientific pitch notation with middle C = C4. Some software and hardware use different octave-number labels for the same MIDI pitches; the octave numbers here follow the book's stated convention rather than a product-specific display convention.

## Related projects

This book is a standalone publication within the same broader line of work as [Musifold](https://github.com/krahd/musifold), the interactive cross-instrument music-geometry application. Musifold grew out of [Ableton Note Helper](https://github.com/krahd/ableton-note-helper), which remains the narrower Ableton Note/Push reference tool.

The book is not the Musifold application and is not intended to serve as the future Musifold book.

