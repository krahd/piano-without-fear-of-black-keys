from pathlib import Path
import fitz
from weasyprint import HTML
ROOT=Path(__file__).resolve().parent
images=ROOT/'extracted-art';images.mkdir(exist_ok=True)
source_pdf=ROOT/'Piano_Without_Fear_of_Black_Keys_v1.3.pdf'
if source_pdf.exists():
 pdf=fitz.open(str(source_pdf))
 for name,page,rect in [
  ('guitar',9,(76,189,515,350)),('piano',6,(91,135,506,258)),('circle',13,(115,340,475,709)),
 ]:
  pix=pdf[page].get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=fitz.Rect(*rect),alpha=False)
  pix.save(str(images/(name+'.png')))
else:
 assert all((images/(n+'.png')).exists() for n in ('guitar','circle')), 'Required extracted-art assets missing'
html='''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Piano Without Fear of Black Keys – editorial design specimen</title>
<style>
@page {size:160mm 230mm; margin:20mm 18mm 20mm 19mm; @bottom-left{content:string(section); font:8pt 'Lato',sans-serif;color:#666e6d;} @bottom-right{content:counter(page); font:8pt 'Lato',sans-serif;color:#666e6d;}}
@page:first {margin:0; @bottom-left{content:none} @bottom-right{content:none}}
*{box-sizing:border-box}
html,body{margin:0;color:#232727;background:#fff}
body{font:9.8pt/1.43 'Noto Serif',serif;hyphens:none;font-kerning:normal}
p{margin:0 0 .94em 0;orphans:3;widows:3}
strong{font-weight:700}
h1,h2,h3,h4{font-family:'Lato',sans-serif;font-weight:700;line-height:1.19;color:#192524;break-after:avoid;page-break-after:avoid}
h1{font-size:19pt;margin:.2em 0 .78em;letter-spacing:-.03em}
h2{font-size:14pt;letter-spacing:-.015em;margin:1.7em 0 .56em}
h3{font-size:11.4pt; margin:1.7em 0 .63em;}
h4{font-size:9.8pt;margin:1.5em 0 .5em}
.partlabel{font:700 8pt/1.4 'Lato',sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#8f4b37;margin-bottom:3mm;}
.section{string-set:section content(text);}
.section-break{break-before:page;page-break-before:always;}
.opening{padding-top:7mm}
.smallcaps{font:700 8pt 'Lato',sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#8f4b37;}
.lead{font-size:10pt;line-height:1.47}
.chapter-rule{border:0;border-top:1.1pt solid #bfb9af;margin:0 0 9mm}
.fig{margin:5mm 0 5mm;text-align:center;break-inside:avoid}
.fig img{display:block;width:78%;height:auto;margin:0 auto}
.fig.medium img{width:43%}
.figcaption{font:8pt/1.37 'Lato',sans-serif;color:#626967;margin-top:2mm}
.exercise{border-top:1.2pt solid #9c6349;padding-top:1.8mm;margin-top:2mm;break-inside:auto}
.exercise h3{margin:0 0 2.8mm;font-size:11.4pt}
.exercise ol{margin:0 0 0 5.5mm;padding:0}
.exercise li{padding-left:1mm;margin:0 0 1.6mm}
.manual-note{margin:4mm 0 4mm;padding-left:4mm;border-left:2pt solid #94634e;font-size:9.7pt}
pre,code,.notes{font:9.8pt/1.4 'DejaVu Sans Mono',monospace;color:#1f3733}
code{background:none;white-space:normal}
.notes{margin:2mm 0 3.6mm;}
.break{break-before:page}
.book-cover{width:160mm;height:230mm;position:relative;padding:30mm 20mm 20mm;background:#f8f7f3;color:#1e2827}
.cover-kicker{font:700 8pt 'Lato',sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#9f5939}
.cover-title{font:700 33pt/1.09 'Noto Serif',serif;letter-spacing:-.045em;margin-top:32mm;margin-bottom:10mm;max-width:113mm}
.cover-rule{width:20mm;height:1.4pt;background:#9c613d}
.cover-subtitle{font:12pt/1.42 'Lato',sans-serif;margin-top:13mm;max-width:105mm;color:#48504d}
.cover-author{position:absolute;bottom:25mm;left:20mm;font:700 12pt 'Lato',sans-serif}
.cover-meta{position:absolute;bottom:16mm;left:20mm;font:8pt 'Lato',sans-serif;color:#6d6f69}
.page-intro{padding-top:10mm}
.book-text{font-size:10.55pt}
table{border-collapse:collapse;width:100%;font:8.8pt/1.27 'Lato',sans-serif;margin:4mm 0 6mm}
th,td{padding:1.35mm 1.8mm 1.3mm;border-bottom:.45pt solid #c9c6bd;text-align:left;vertical-align:top}
th{font-weight:700;border-top:1pt solid #59645f;border-bottom:.8pt solid #59645f;color:#253633}
tr{break-inside:avoid}
.table-notes td:nth-child(2){font-family:'DejaVu Sans Mono',monospace;font-size:8.5pt}
.table-notes th:first-child{width:25%}
.table-notes th:nth-child(2){width:46%}
.list-simple{margin:.4em 0 1.2em 5mm;padding-left:2mm}
.list-simple li{margin:0 0 .7mm;padding-left:1mm}
.endline{border-top:.5pt solid #d2c9be;margin-top:10mm;padding-top:3mm;font:8pt 'Lato',sans-serif;color:#777}
</style></head><body>
<section class="book-cover"><div class="cover-kicker">A transposition-first manual</div><div class="cover-title">Piano<br>Without Fear<br>of Black Keys</div><div class="cover-rule"></div><p class="cover-subtitle">A transposition-first manual for piano, Ableton Push/Note, and guitar</p><div class="cover-author">Tomás Laurenzo</div><div class="cover-meta">Version 1.3 &nbsp;&middot;&nbsp; September 2026</div></section>

<section class="section-break page-intro"><div class="partlabel section">Preface</div><h1>Preface</h1><hr class="chapter-rule"><p class="lead">This is not a general piano method. It has a narrower goal: make <strong>scales, chords, arpeggios, voicings, and progressions transposable</strong> on a keyboard whose physical geometry changes from key to key. It starts from first principles so a new musician can use it, but everything points back to that goal.</p><p>You do <strong>not</strong> need to read staff notation, have perfect pitch, memorize every key signature, or already know piano fingering. You need a keyboard or piano, a few minutes of focused practice, and the willingness to say note names and interval formulas before speed becomes important.</p><h3>How to read every musical example</h3><p>The book uses the same four-layer translation throughout:</p><div class="notes">function → pitch spelling → register → instrument geometry</div><p>For example, a minor seventh chord is always:</p><div class="notes">1 b3 5 b7</div><p>On D, that becomes:</p><div class="notes">D F A C</div></section>

<section class="section-break opening"><div class="partlabel section">Part II &nbsp; / &nbsp; Three geometries for the same music</div><h1>Three geometries<br>for the same music</h1><hr class="chapter-rule"><h2>4. Piano: non-isomorphic geometry</h2><p>On piano, the same interval formula produces different visible shapes in different keys. Compare:</p><div class="notes">Cmaj7 &nbsp;&nbsp;&nbsp; Dbmaj7</div><p>Both are <code>1 3 5 7</code>. The musical object is identical; only its keyboard realization changes.</p><h2>7. Guitar: mostly movable geometry</h2><p>In standard tuning, every fret is a semitone. Most interval/chord shapes transpose by sliding, with one important irregularity: the interval between G and B strings is a major third rather than a perfect fourth.</p><figure class="fig"><img src="extracted-art/guitar.png"><figcaption>Guitar C major</figcaption></figure><p>The piano problem is therefore the reverse of a barre chord: the <em>formula</em> transposes, but the <em>shape</em> does not.</p></section>

<section class="section-break opening"><div class="partlabel section">Part II &nbsp; / &nbsp; Three geometries for the same music</div><h1>7.1 Movable shapes hide pitch location</h1><hr class="chapter-rule"><p class="lead">Movable geometry is useful, but it creates a specific blind spot. On guitar, a scale or chord can often be transposed by moving a familiar shape up or down the neck. The fingering relationship survives, but every sounding pitch has moved with it. A player can therefore know <em>how to move the object</em> without knowing which notes are sounding, or where the same pitch classes live in another register. Push and Note can encourage the same habit because their chromatic layouts are largely isomorphic.</p><p>Piano exposes the problem differently. Several keys can be practised in the same register: C major around middle C, Db major beginning a semitone higher, D major another semitone higher. The hand geometry changes, but the keyboard remains a fixed map of absolute pitches. This makes it easier to notice that transposition and relocation are not the same operation.</p><p>The book therefore treats <strong>shape as a consequence, not as the musical object</strong>. A shape is allowed to become automatic only after you can recover what it means: function, note names, register, and exact locations.</p><p class="manual-note"><strong>Fixed-register rule.</strong> When practising transposition on guitar, Push, or Note, do not always slide the same shape. Choose a register window first—for example C3–C5—and realize each scale or chord inside that window. Changing key will then force new strings, pads, inversions, or fingerings while keeping the sounding range comparable.</p></section>

<section class="section-break opening"><div class="partlabel section">Part III &nbsp; / &nbsp; Keys, scales, and modes</div><h1>9. The seven diatonic modes</h1><hr class="chapter-rule"><p>The modes are not seven unrelated scales. They are seven rotations / alterations of a diatonic collection, best understood as degree formulas relative to a new tonic.</p><table class="table-notes"><thead><tr><th>Mode</th><th>Formula</th><th>Characteristic degree</th></tr></thead><tbody>
<tr><td>Ionian</td><td>1 2 3 4 5 6 7</td><td>major 7</td></tr><tr><td>Dorian</td><td>1 2 b3 4 5 6 b7</td><td>natural 6 over minor</td></tr><tr><td>Phrygian</td><td>1 b2 b3 4 5 b6 b7</td><td>b2</td></tr><tr><td>Lydian</td><td>1 2 3 #4 5 6 7</td><td>#4</td></tr><tr><td>Mixolydian</td><td>1 2 3 4 5 6 b7</td><td>b7 over major</td></tr><tr><td>Aeolian</td><td>1 2 b3 4 5 b6 b7</td><td>b6</td></tr><tr><td>Locrian</td><td>1 b2 b3 4 b5 b6 b7</td><td>b5</td></tr></tbody></table><div class="exercise"><h3>Exercise 5 - Break the white-key trap</h3><p>If C major, A minor, and D Dorian are your default universe, they all use the same pitch collection. Deliberately practice modes whose tonic forces black keys:</p><ul class="list-simple"><li>Eb Dorian: <code>Eb F Gb Ab Bb C Db</code></li><li>F# Dorian: <code>F# G# A B C# D# E</code></li><li>Db Lydian: <code>Db Eb F G Ab Bb C</code></li><li>Ab Mixolydian: <code>Ab Bb C Db Eb F Gb</code></li></ul><p>For each, alternate between:</p><div class="notes">scale → triad → seventh chord → arpeggio → 2-bar improvisation</div></div></section>

<section class="section-break opening"><div class="partlabel section">Part IV &nbsp; / &nbsp; Chords, inversions, voicings, and arpeggios</div><h1>Chords, inversions,<br>voicings, and arpeggios</h1><hr class="chapter-rule"><h2>11. Chords are formulas</h2><p>Read a chord symbol from left to right: <strong>root letter → chord quality → extensions or alterations</strong>. For example, <code>Abmaj9</code> means an Ab-root chord with major quality, a major seventh, and a ninth.</p><h3>11.1 The circle of thirds: the geometry inside tertian chords</h3><p>In a diatonic key, reorder the seven scale degrees as:</p><div class="notes">1 → 3 → 5 → 7 → 2 → 4 → 6 → 1</div><p>In C major this is <code>C → E → G → B → D → F → A → C</code>. Three adjacent positions give a triad; four give a seventh chord. Unlike the circle of fifths, this <strong>diatonic circle of thirds depends on the key</strong> because the sequence uses scale notes rather than a fixed chromatic interval.</p><figure class="fig medium"><img src="extracted-art/circle.png"><figcaption>Diatonic circle of thirds in C major</figcaption></figure></section>
</body></html>'''
(ROOT/'design-proof.html').write_text(html,encoding='utf-8')
HTML(string=html,base_url=str(ROOT)).write_pdf(str(ROOT/'Piano_Without_Fear_Existing_Text_Book_Design_Proof.pdf'))
print('PDF created:',ROOT/'Piano_Without_Fear_Existing_Text_Book_Design_Proof.pdf')
