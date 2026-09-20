# Worklog — Piano Without Fear of Black Keys

## 2026-09-18 — v1.3 revision

- Added register as an explicit representational layer between pitch spelling and instrument geometry.
- Added the movable-shape/pitch-location discussion and fixed-register practice.
- Added cross-instrument exercises that distinguish transposition from physical relocation.
- Replaced ASCII transformation arrows with typographic arrows.
- Refined handbook typography and pagination.

## 2026-09-20 — architecture correction and repository preparation

- Recovered the project-family distinction: Ableton Note Helper is the narrower predecessor; Musifold is the interactive cross-instrument application; *Piano Without Fear of Black Keys* is a standalone book.
- Confirmed Musifold `main` was clean and aligned with GitHub and that the earlier book integration remains only on experimental branch `ai/musifold-book-home-20260918`.
- Reconstructed a standalone repository candidate from the revised book source and complete SVG set.
- Corrected the stale one-page philosophy to the four-layer model including register.
- Added explicit related-project documentation preventing future conflation with a possible Musifold book.

## 2026-09-20 — standalone repository build recovered

- Created and cloned `krahd/piano-without-fear-of-black-keys` as the independent home of the book; Musifold remains the interactive application and Ableton Note Helper its predecessor/reference project.
- Imported the complete v1.3 source into workspace job `piano-book-v13-20260920-a1`.
- Static validation passed: 16 referenced SVG teaching diagrams, 16 assets, four-layer model present, project architecture wording correct, and `git diff --check` clean.
- Initial Mac build failed because WeasyPrint was absent. Chromium was tested but produced 28 pages rather than the canonical 37-page layout, so it was rejected as the canonical renderer.
- Installed Homebrew `weasyprint` 70.0 (plus required image dependencies) without changing the repository build architecture.
- Re-ran `./build.sh` successfully; `pdfinfo` reports 37 pages. Workspace checkpoint after the successful build: `15540bdf2d00d3b6957fec9a27eb180ca24aa5bb`.
- Next: final integration validation, remote verification, project-link reconciliation, work-admin registration, and retirement of the obsolete unmerged Musifold book branch.

## 2026-09-20 — build-system correction and integration recovery

- Reconciled the standalone workspace against GitHub before resuming; no piano-book content had reached `main`.
- Confirmed the previous integration attempt failed validation and did not mutate `main`.
- Determined that Homebrew provides the GLib stack but the available Python WeasyPrint runner could not resolve `libgobject-2.0`; avoided changing the Mac globally.
- Verified installed Chromium as a working renderer and updated `build.sh` to prefer WeasyPrint when available, otherwise use Chromium.
- Ran `./build.sh` successfully on the Mac; `pdfinfo` reports A4, 38 pages, PDF 1.7.
- Updated README build documentation and live persistent state to match the verified renderer behaviour.
- Next: update plan acceptance wording, mark the workspace ready, integrate through the v5 gate, and independently verify GitHub `main` before related-repository cleanup.

## 2026-09-20 — canonical renderer reconciliation

- Confirmed the installed canonical renderer is WeasyPrint 70.0 with Pandoc 3.11; `build.sh` correctly prefers it and retains Chromium only as a fallback.
- Rebuilt the standalone book on the Mac with WeasyPrint 70.0; `pdfinfo` reports 37 pages, A4, PDF 1.7. The earlier 38-page result was produced by the Chromium fallback and is superseded as the canonical PDF.
- Diagnosed two safe integration-gate failures: one validation argument was expanded by the outer shell before reaching the temporary integration worktree; a later literal validation proved the temporary worktree contained all expected staged files.
- Measured integration predicates individually: build succeeds, 16 referenced SVGs equal 16 assets, the four-layer model is present, `git diff --check` passes, and the only mismatch was the obsolete 38-page expectation.
- Next: mark the updated workspace ready, integrate with the corrected 37-page acceptance gate, independently verify GitHub `main`, reconcile related-project/work-admin documentation, retire the obsolete unmerged Musifold book branch, and mark persistent state COMPLETE.
