## Version 1.3.1 cover corrections (25 October 2026)

The approved design direction now has a [v1.3.1 six-page proof](Piano_Without_Fear_of_Black_Keys_v1.3.1_design_proof.pdf), alongside the original design test below. The corresponding [HTML](design-proof.html) and [source generator](build_proof.py) have been updated.

- Author credit on cover: **Tomas Laurenzo**, without accent.
- Version on cover: **1.3.1**, October 2026.
- Cover subtitle (five fixed lines): `A transposition-first manual` / `for piano,` / `Ableton Push,` / `Ableton Note,` / `and guitar`.
- Redundant kicker removed.
- Body specimen uses original v1.3 text without rewriting, with a 160 × 230 mm book layout.
- **This is not a complete v1.3.1 publication.** Whole-book typesetting, native SVG integration, complete text integrity, appendix pagination and production preflight remain outstanding. Original v1.3 text/PDF on main remain untouched.
- The conceptual question of **“transposition-first”** is reserved for **v1.4**.

---

# Book-design track: original-text specimen

**Status:** typesetting trial for review; NOT a new edition of the manuscript.

This folder contains a six-page typographic specimen using selected, unchanged passages from *Piano Without Fear of Black Keys* v1.3, with two diagrams cropped from an earlier v1.3 PDF export. It is deliberately **not** a continuous six-page excerpt of the manuscript: some intervening passages, tables and diagrams are omitted in order to test representative page types. The passage content that is reproduced was not rewritten. The cover rearranges existing title, author, subtitle and version data.

A saved PDF labelled v1.3 in the user's file Library was used for visual inspection and for temporary raster copies of selected existing artwork. That saved export is 39 pages, whereas the canonical repository's most recent completion status reports a 37-page build; **do not** treat the Library export as a current canonical checksum or base for subsequent book production. The GitHub Markdown and SVG source on `main` remain authoritative.

## Direction tested

- 160 x 230 mm book trim (not A4).
- Single title page, serif book typography for prose, sober sans-serif headings and small running heads.
- Existing copper/teal accents used sparingly rather than coloured boxes as the organising device.
- Less boxed, less dashboard-like pedagogy; no rewritten lead-ins or explanatory slogans.
- Diagrams treated as illustrations and placed in a typographic grid. Current specimen embeds raster crops only for the proof; use the original SVGs in production.
- Open tables with horizontal rules, not dense cell borders.

## Review files

- `Piano_Without_Fear_Existing_Text_Book_Design_Proof.pdf` — six-page PDF specimen.
- `design-proof.html` — self-contained page markup referring to images in `extracted-art/`.
- `build_proof.py` — rebuild script (requires Python, PyMuPDF and WeasyPrint; uses installed Lato and Noto Serif fonts).
- `extracted-art/` — illustrative raster crops from the previously generated PDF; these are not replacements for the repository's original vector artwork.

## Scope limitations

This proof **does not** establish a final editorial architecture, page count, table overflow behaviour across the appendices, final SVG integrity, accessibility tagging, print bleed or press/POD-ready margins. There is no new audio or new pedagogy. There is no layout approval implied by rendering successfully. Do not merge into the original v1.3 build pipeline without human review and full-book QA.

The separate content-revision track remains independent, including the rejected early chapter prototype (PR #3) and the approved ideas about scale geometry without any prose approval.
