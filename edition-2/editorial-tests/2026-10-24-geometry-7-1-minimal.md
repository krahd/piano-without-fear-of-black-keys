# Editorial test: section 7.1, instrument geometry

**Status:** voice-unverified, awaiting the author's direct assessment.  
**Source:** `piano_transposition_manual.md`, v1.3, `main` at `145cbe1d2c30d7c0eaa3a1f810a951d140dcd494`.  
**Scope:** exactly one inserted paragraph within section 7.1. No original source, design, reference tables or release files are altered.  
**Previous failed prototype:** PR #3 was explicitly rejected for its prose; its text is not used as a source for this revision.

## Change in one sentence

Explain how a familiar open D-minor chord maps to actual pitches and chord tones; then contrast a simple piano triad with the movable-guitar transposition. Retain the original manual's section and exercise architecture.

## Original section (verbatim)

### 7.1 Movable shapes hide pitch location

Movable geometry is useful, but it creates a specific blind spot. On guitar, a scale or chord can often be transposed by moving a familiar shape up or down the neck. The fingering relationship survives, but every sounding pitch has moved with it. A player can therefore know *how to move the object* without knowing which notes are sounding, or where the same pitch classes live in another register. Push and Note can encourage the same habit because their chromatic layouts are largely isomorphic.

Piano exposes the problem differently. Several keys can be practised in the same register: C major around middle C, Db major beginning a semitone higher, D major another semitone higher. The hand geometry changes, but the keyboard remains a fixed map of absolute pitches. This makes it easier to notice that transposition and relocation are not the same operation.

The book therefore treats **shape as a consequence, not as the musical object**. A shape is allowed to become automatic only after you can recover what it means: function, note names, register, and exact locations.

<div class="practice-note"><strong>Fixed-register rule.</strong> When practising transposition on guitar, Push, or Note, do not always slide the same shape. Choose a register window first—for example C3–C5—and realize each scale or chord inside that window. Changing key will then force new strings, pads, inversions, or fingerings while keeping the sounding range comparable.</div>

### Exercise 3A - One register, many geometries

Choose the register from C3 through C5. Play these major scales without leaving it:

1. C major
2. Db major
3. D major
4. Eb major
5. E major

On piano, name every note as you play it. On guitar or Push/Note, resist the urge to preserve one movable shape: choose positions that keep the pitches inside the same register window. Then reverse the exercise: keep a familiar shape and state explicitly how far the entire sounding register moved.

**Success criterion:** you can distinguish *transposing the musical relationship* from *moving a physical shape*, and you can name the exact pitches produced by either operation.

## Proposed section (one insertion; remaining text identical)

### 7.1 Movable shapes hide pitch location

Movable geometry is useful, but it creates a specific blind spot. On guitar, a scale or chord can often be transposed by moving a familiar shape up or down the neck. The fingering relationship survives, but every sounding pitch has moved with it. A player can therefore know *how to move the object* without knowing which notes are sounding, or where the same pitch classes live in another register. Push and Note can encourage the same habit because their chromatic layouts are largely isomorphic.

A familiar open D minor chord (`xx0231`) sounds `D3 A3 D4 F4` from the fourth string upwards: four pitches, but only three chord tones, `D F A` (`1 b3 5`). On piano, `D F A` can be played as a root-position triad without reproducing the guitar's doubled D or its register. Transpose that triad one semitone to Eb minor and the notes become `Eb Gb Bb`: three black keys rather than three white keys. A movable minor barre shape on guitar can make the same transposition by shifting one fret.

Piano exposes the problem differently. Several keys can be practised in the same register: C major around middle C, Db major beginning a semitone higher, D major another semitone higher. The hand geometry changes, but the keyboard remains a fixed map of absolute pitches. This makes it easier to notice that transposition and relocation are not the same operation.

The book therefore treats **shape as a consequence, not as the musical object**. A shape is allowed to become automatic only after you can recover what it means: function, note names, register, and exact locations.

<div class="practice-note"><strong>Fixed-register rule.</strong> When practising transposition on guitar, Push, or Note, do not always slide the same shape. Choose a register window first—for example C3–C5—and realize each scale or chord inside that window. Changing key will then force new strings, pads, inversions, or fingerings while keeping the sounding range comparable.</div>

### Exercise 3A - One register, many geometries

Choose the register from C3 through C5. Play these major scales without leaving it:

1. C major
2. Db major
3. D major
4. Eb major
5. E major

On piano, name every note as you play it. On guitar or Push/Note, resist the urge to preserve one movable shape: choose positions that keep the pitches inside the same register window. Then reverse the exercise: keep a familiar shape and state explicitly how far the entire sounding register moved.

**Success criterion:** you can distinguish *transposing the musical relationship* from *moving a physical shape*, and you can name the exact pitches produced by either operation.

## Editorial review notes

- Original's opening, guitar/Push/Note comparison, fixed-register discussion, and Exercise 3A are all unchanged.
- The addition names exact sounding pitches `D3 A3 D4 F4` for open `xx0231`, versus the chord-tone set `D F A`. It distinguishes these pitches from a root-position piano triad.
- Dm/Ebm root-position piano triads demonstrate a change from three white keys to three black keys under the same `1 b3 5` relation; the movable-guitar example explicitly specifies a *barre* shape so that an open chord is not wrongly presented as sliding unchanged.
- No reader-addressed assurances, success-criterion box, new headings, catchy slogan, or pedagogical preamble were added.
- **Known editorial issue left for later:** the original occasionally conflates 'function' with interval structure, and the section gives Push/Note more early space than the newly agreed primary readership probably warrants. Do not use this local experiment to silently rewrite them.
- Approval gate: only adopt the insertion after the author accepts its voice and usefulness; if rejected, keep the original and log the reason.
