# Piano Without Fear of Black Keys — v1.3.1

**Edition:** complete book-design/typesetting revision of v1.3, 25 October 2026.

**PDF:** `Piano_Without_Fear_of_Black_Keys_v1.3.1.pdf` (53 pages, 160 × 230 mm).

The book is derived directly from `../../piano_transposition_manual.md` and the original SVGs in `../../assets/`. The entire manuscript after the original cover closing `</section>` is unchanged. This is a **visual publication update**, not the rejected v2 prose rewrite. The `main`-branch original v1.3 book and its build system are retained separately.

## Changes in v1.3.1

- A more book-like, 160 × 230 mm trim with mirrored margins: inside 24 mm, outside 20 mm; top 22 mm, bottom 24 mm.
- Noto Serif body text at 10 pt, 1.43 line spacing; Lato heads and tables. Minor copper/teal accents and unobtrusive folios.
- Cover author spelled **Tomas Laurenzo**, without an accent.
- Cover subtitle exactly four lines:

  ```text
  A transposition-first manual
  for piano,
  Ableton Push and Note,
  and guitar
  ```

- Cover version number `1.3.1 · October 2026`.
- The original vector diagrams and all reference appendices are retained. Tables are reset in a quieter typographic style.
- Removes the extra title inserted by Pandoc's standalone HTML template (not a manuscript title).

## Rebuild

Requirements: Python 3, Pandoc, WeasyPrint, BeautifulSoup4, locally available Noto Serif, Lato and DejaVu Sans Mono fonts.

From this directory:

```sh
python3 build.py
```

`build.py` reads the original manuscript from the root and writes the derived v1.3.1 Markdown, HTML and PDF beside itself. It asserts that the manuscript body is unchanged. The original root build (`./build.sh`) still reproduces v1.3; do **not** overwrite it.

## Verification and limitations

- PDF: 53 pages, each exactly 160 × 230 mm.
- Original Markdown SHA-256: `0fd2c4030b21c7ce3b7454ac983a6821aec8acfe980f8ab978c301dc455a33b6`.
- PDF SHA-256: `f8726d53fad0757bac8a65de91f0f58d56619cb31cfc3cdc4eeca6d204d26359`.
- Text objects checked against the page bounds; no overflow detected. All original diagram files resolved; SVGs are included as vectors. Text extraction contained no replacement-character glyphs. All pages reviewed via contact sheets.
- This is a reader/print-layout PDF, **not** a commercial print-on-demand production package with bleed, ISBN or printer-specific imposition.
- The existing discussion about the book's audience and the phrase *transposition-first* is reserved for v1.4 ([issue #5](https://github.com/krahd/piano-without-fear-of-black-keys/issues/5)), not silently applied to v1.3.1.

The source and design remain independently editable; typography can be adjusted without touching the body prose.
