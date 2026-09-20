# Plan — Piano Without Fear of Black Keys

## Objective

Maintain *Piano Without Fear of Black Keys* as a standalone book repository while keeping its conceptual relationship to Musifold and Ableton Note Helper explicit.

## Project architecture

- `krahd/piano-without-fear-of-black-keys` — this standalone book and its reproducible PDF source.
- `krahd/musifold` — interactive cross-instrument music-geometry application; not the container for this book.
- `krahd/ableton-note-helper` — narrower predecessor/reference tool from which Musifold grew.
- A future Musifold book, if created, is a distinct future publication rather than this book renamed.

## In scope for repository establishment

1. Publish the corrected v1.3 source as a standalone GitHub repository.
2. Preserve the explicit four-layer model: `function → pitch spelling → register → instrument geometry`.
3. Preserve the register/shape revision and fixed-register exercises.
4. Keep all original SVG teaching diagrams and a reproducible Pandoc build with WeasyPrint or verified Chromium fallback.
5. Verify source/image completeness, PDF preflight, and representative rendered pages.
6. Commit and push through an isolated workspace/checkpoint flow where applicable.
7. Independently verify the GitHub remote ref and repository contents.
8. Reconcile related-project documentation without folding the book into Musifold.

## Out of scope

- Designing or writing a future Musifold book.
- Merging the experimental `ai/musifold-book-home-20260918` branch into Musifold `main`.
- Rewriting Ableton Note Helper into Musifold.

## Acceptance criteria

- The standalone GitHub repository exists and `main` contains the complete book source, 16 SVG diagrams, build files, persistent state, and current PDF.
- `./build.sh` succeeds from the repository source.
- No referenced local teaching diagram is missing.
- The one-page philosophy uses the four-layer model including register.
- The final PDF passes preflight and representative visual QA.
- GitHub `main` is independently verified after push/integration.
- Musifold `main` remains an interactive application and does not contain the piano book as an integrated publication tree.
