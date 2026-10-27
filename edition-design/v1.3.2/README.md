# v1.3.2 maintenance candidate

Prepared 27 October 2026 for authorial review under issue #10. Not a published release until the author approves and merges the review PR.

## Scope

Only the last note of each of the twelve Appendix B whole-tone rows changes, from raised sixth spelling to the stated flat seventh. Sounding pitches and formula `1 2 3 #4 #5 b7` are preserved. `03_appendix_scales.md` is synchronised. No other manuscript prose, examples, pedagogy, SVG assets or successor-book files change.

The build is derived from v1.3.1/build.py, with edition/output names advanced to v1.3.2 and regression checks run before rendering. `book.css` is byte-identical to v1.3.1. The original v1.3 and v1.3.1 PDFs and build files are untouched. The root build now produces this maintenance candidate at the unchanged public filename `Piano_Without_Fear_of_Black_Keys.pdf`; the review branch does not change the public main-branch file until merge.

## Build and checks

From the repository root:

```sh
python3 -m unittest discover -s tests -v
./build.sh
```

Requirements: Python 3, BeautifulSoup4, WeasyPrint (review build: 70.0), Pandoc, Noto Serif, Lato, DejaVu Sans Mono. See v1.3.1 for design history. Generated Markdown/HTML are build intermediates, not tracked sources.

The four regression tests cover 204 physical table rows in Appendices A-C: 180 scale rows and 24 chord rows (108 chord-family cells), totalling 288 separately validated sequences. Both diatonic letter and semitone pitch class are checked, including double accidentals; missing rows, roots and note counts are checked. The explicit whole-tone regression fixes the intended formula and twelve final spellings. Negative controls distinguish an enharmonic letter error from a pitch error. CI runs the same dependency-free checks.

Running the checker against the parent manuscript reproduces exactly twelve letter discrepancies and no pitch discrepancies. Comparing all 288 old/new sequences confirms unchanged pitch classes. This is table validation, not a claim to validate every musical statement in the manual.

## PDF review

- 53 pages, 160 × 230 mm; 122 outline entries, same as the historical PDF.
- All 16 original SVG references resolve. All four contact sheets visually reviewed; corrected whole-tone pages 43-44 inspected at higher resolution.
- Text extraction differs from the historical v1.3.1 PDF only on pages 1 (edition number), 43 and 44 (corrected notes).
- No extracted text outside page bounds; no U+FFFD replacement glyphs. All original fonts are available for the review build.
- No new layout defect observed in the changed tables. Existing split examples, glossary, compressed chord table and split finale from the 25 October audit remain outside this notation-only correction. No physical print proof claimed.

## Verification hashes (SHA-256)

- Canonical manuscript: `e9c35a32d6280aae6efcdc6d19c208d3549e336304007874a2e097f8eb22dd49`
- Candidate PDF and identical root PDF: `829f929df2f4909dbd8db8af88d2c95904b291824158148ff6ee3b11d49bb043`
- Unchanged stylesheet: `06a2f25fd7a2f51948e890f55d1eff3b1d4393eb8b11b33efd4a520b91870596`
- Historical v1.3.1 PDF: `f8726d53fad0757bac8a65de91f0f58d56619cb31cfc3cdc4eeca6d204d26359`

## Author-review and release handoff

1. Review the twelve-line canonical diff, mirrored convenience-source changes, passing checks, and candidate PDF, particularly pp. 43-44.
2. Author approval is required before merge, as stated in issue #10: “Publish improvements incrementally after authorial review; old release stays archived.”
3. Merge the review PR only after approval. Its root PDF is byte-identical to the reviewed versioned v1.3.2 PDF, preserving the existing public URL.
4. Verify the main-branch root/versioned PDF hashes above after merge, retain all historical PDFs, and mark v1.3.2 current in the release documentation. Any release tag should point to the approved merge commit.
5. Leave issue #10 open: this completes its notation/regression priority only; the other editorial and exercise priorities remain outstanding.
