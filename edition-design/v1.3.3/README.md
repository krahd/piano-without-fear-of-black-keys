# v1.3.3 — completed audit fixes (28 October 2026)

This is an incremental edition of *Piano Without Fear of Black Keys* and **retains the transposition-first purpose and both reading paths**. The separate concept in `successor-book/CONCEPT.md` has not been imported into this book. The versioned PDF and the root stable PDF are copies of the same file.

## Musical and pedagogical changes

- Corrects Cmaj7/Dbmaj7 wording: the chord formula, not sounding pitches, is invariant.
- Clarifies the degree formula vs Roman-numeral harmonic function distinction, introduces double accidental examples and removes the obvious In-Key typo.
- Adds a complete Am–F–C–G to Bbm–Gb–Db–Ab progression with source and destination octave-specific piano voicings. Each target pitch is exactly one semitone higher and the chord inversion is preserved.
- Explicit Push Chromatic/Fourths/Fixed ON (same pad pitches under different key highlighting) versus Fixed OFF (root-following pitch assignments), and Note Fourths/In Key OFF (manual shape movement required).
- Scales the 20-minute routine to three/six/twelve roots depending on fluency and softens the eight-week beginner milestones without removing the twelve-root benchmark.
- Adds a controlled D Aeolian/D Dorian and E Aeolian/E Dorian comparison over a stable tonic.

## Book and accessibility changes

- 160 × 230 mm book design retained; 10 pt Noto Serif body and mirrored margins unchanged.
- Printed contents now have resolved page numbers and clickable links; a digital HTML edition is published alongside the PDF.
- Reflows the glossary as two-column term/definition rows and splits the crowded seventh-chord appendix into two readable groups without deleting or changing any chord table entries.
- Keeps musical example labels with their formulas and moves the final one-page philosophy to its own single page.
- Adds author and subject metadata, basic PDF tagging (not a claim of PDF/UA compliance) and clickable source URLs; the original sixteen SVG diagrams remain vector based.

## Historical builds and release safety

- The v1.3, v1.3.1 and v1.3.2 builders now read **frozen manuscript snapshots** rather than current `piano_transposition_manual.md`. Their expected source SHA-256s are checked before running.
- Historical diagrams reside in `edition-design/archive-assets-v1.3/` and the v1.3 stylesheet is frozen. Each historic builder writes only to a separate `rebuild/` folder; it cannot silently overwrite an archived published PDF.
- The archived PDF files themselves are not changed by this release. Rebuilding with different versions of WeasyPrint and fonts does not guarantee byte-for-byte PDF equivalence; it does protect the **historical text and assets**.

## Validation and limits

- v1.3, v1.3.1, v1.3.2 archive builders executed successfully from frozen sources in the audit workspace.
- New editorial tests verify historical snapshot hashes, one-semitone voicing transformations, updated instructional wording and text-source synchronisation. Existing source pitch-table tests remain in CI and run as part of the current builder.
- Candidate reader PDF inspected page by page using montages and selected high-resolution pages: **55 pages**, **122 bookmarks**, **82 PDF link annotations**, no out-of-bounds extracted text, no U+FFFD glyphs; `pdfinfo` reports tagged structure and Tomas Laurenzo as author.
- Corrected PDF tagging is **not** independently audited for full accessibility conformance. The accessible HTML source has meaningful headings and figure alt text, but a screen-reader usability audit remains to be performed.
- Physical print proof and an observational reader study with both learner populations remain unperformed. Device instructions are documented against official Ableton manuals, but physical Push/Note behaviour has not been tested on hardware in this release.
- Historical digital sources and edition 1.3.2 remain accessible. No changes to the public download filename or the separate successor-book concept.

## Rebuild

From repository root `./build.sh` (Python 3, Pandoc, Noto Serif, Lato and DejaVu Sans Mono required; build packages listed in `requirements-book.txt`). It uses an isolated `uv` environment if necessary, or honours `BOOK_PYTHON` for a pre-configured interpreter. It regenerates the versioned PDF and synchronises the stable `Piano_Without_Fear_of_Black_Keys.pdf` file. The standalone accessible HTML file is `Piano_Without_Fear_of_Black_Keys_v1.3.3.html`.

**Current edition source hash SHA-256:** `7652ef1e643ede4d63cb5a3882a94cc9433bb82555336f7b39b39627605fc302`.
**Current PDF hash SHA-256:** `1ff914461624a7f7b96ef1c2e2a59e510f0bcec4c4d334ced2a6ef26880776e7`.

**Renderer parity:** WeasyPrint 68.0 and the installed Mac WeasyPrint 70.0 were both tested; both produce 55 pages and 122 bookmarks, but the output bytes differ. The publication PDF is the checked WeasyPrint 68.0 rendering.
