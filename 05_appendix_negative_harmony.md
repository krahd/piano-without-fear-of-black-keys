# Appendix F - Negative harmony

Negative harmony is best treated as a **pitch-class reflection technique for composition and reharmonization**, not as a claim that every mirrored chord will function identically in every musical context. The practical form used here is associated with Ernst Levy's theory of harmonic polarity and with later popularizations of the term "negative harmony."

## F.1 The common tonic-dominant axis

For a tonic with pitch class `T` (where C=0, C#=1, ... B=11), take the dominant at `T+7`. Reflect every pitch `p` around the midpoint of tonic and dominant:

`N(p) = 2T + 7 - p  (mod 12)`

For C, `T=0`, so:

`N(p) = 7 - p  (mod 12)`

![Negative-harmony pitch-class mirror in C](assets/negative_harmony_axis.svg)

The resulting pitch-class pairs are:

| Positive | Negative | Positive | Negative |
| --- | --- | --- | --- |
| C | G | G | C |
| C#/Db | F#/Gb | F#/Gb | C#/Db |
| D | F | F | D |
| Eb | E | E | Eb |
| Ab | B | B | Ab |
| A | Bb | Bb | A |

Because reflection reverses interval direction, note order is usually normalized after the mapping so the result can be read as an ordinary chord or scale.

## F.2 Major becomes minor around the same tonal center

Reflect C major:

`C E G → G Eb C → C Eb G = Cm`

![C major before reflection](assets/negative_c_major.svg)

![C minor after reflection](assets/negative_c_minor.svg)

Reflecting the C-major scale gives the pitch collection of C natural minor:

`C D E F G A B → G F Eb D C Bb Ab`

Reordered from C:

`C D Eb F G Ab Bb`

This does **not** mean that major and natural minor are interchangeable; it means the reflection maps one collection to the other under this chosen axis.

## F.3 Chord examples in C

| Positive harmony | Pitches | Negative image | Equivalent spelling |
| --- | --- | --- | --- |
| C major (I) | C E G | G Eb C | C minor (i) |
| D minor (ii) | D F A | F D Bb | Bb major (bVII) |
| E minor (iii) | E G B | Eb C Ab | Ab major (bVI) |
| F major (IV) | F A C | D Bb G | G minor (v) |
| G major (V) | G B D | C Ab F | F minor (iv) |
| A minor (vi) | A C E | Bb G Eb | Eb major (bIII) |
| B diminished (vii dim) | B D F | Ab F D | D diminished (ii dim) |

A particularly useful dominant example is:

`G7 = G B D F → C Ab F D = D F Ab C = Dm7b5`

The same pitch set can be heard or voiced as `Fm6 = F Ab C D`. This is one reason the minor-subdominant family appears naturally in negative-harmony demonstrations.

## F.4 A practical reharmonization workflow

1. Choose a tonal center and keep the axis fixed for the passage.
2. Reduce the source chord or melody to actual pitch classes; do not transform only the chord symbol.
3. Reflect each pitch using the mapping table or formula.
4. Reorder the resulting pitch set into a readable chord.
5. Choose an inversion/voicing that preserves useful voice leading.
6. Listen for function. Keep, alter, or reject the result according to the music rather than the transformation alone.

### Exercise F1 - Mirror a cadence

In C major, transform:

`Dm7 → G7 → Cmaj7`

Map every chord tone. Then voice the negative sequence on piano with the smallest possible motion. Compare the original and transformed bass motion, tendency tones, and final sense of arrival.

### Exercise F2 - Mirror a melody, then reharmonize

Write a four-bar melody in C major. Reflect every pitch through the C/G axis. Keep the rhythm unchanged. First play the mirrored melody over a C pedal; then harmonize it by ear. Only after that, compare the result with mechanically reflected chords.

### Exercise F3 - Transpose the method

Repeat the operation in Db, E, F#, and Ab. Do **not** memorize a C-only table. Use the general formula or construct the tonic/dominant axis in the new key.

## F.5 Limits and variants

- The tonic/dominant midpoint is a common practical convention, but inversion axes can be chosen differently for other compositional purposes.
- Enharmonic spelling after reflection is analytical rather than purely mechanical. Choose spellings that make the resulting harmony readable in context.
- Negative harmony preserves a mathematical symmetry, not every psychoacoustic, stylistic, or historical property of tonal function.
- It is most useful as a generator of alternatives: mirrored melodies, modal mixture, minor-subdominant colors, contrary motion, and voice-leading experiments.
