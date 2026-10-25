from pathlib import Path
from html import escape
from weasyprint import HTML
from PIL import Image, ImageOps, ImageDraw
import fitz

OUT=Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True)

ROOT='#AA573E'; TEAL='#247B78'; INK='#222828'; MUTED='#606A68'; PAPER='#F7F5F0'; LINE='#D4D1C9'

PCH={'C':0,'C#':1,'Db':1,'D':2,'D#':3,'Eb':3,'E':4,'F':5,'F#':6,'Gb':6,'G':7,'G#':8,'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}
WHITE=[('C',0),('D',2),('E',4),('F',5),('G',7),('A',9),('B',11)]
BLACK=[('C#',1,0),('D#',3,1),('F#',6,3),('G#',8,4),('A#',10,5)]

def keyboard(notes,labels=None):
    labels=labels or {}
    active={PCH[n]:i for i,n in enumerate(notes)}
    W=72; base=15; h=184; rows=[]
    rows.append(f'<svg role="img" aria-label="Keyboard with notes {escape(", ".join(notes))} highlighted" viewBox="0 0 534 213" xmlns="http://www.w3.org/2000/svg">')
    rows.append('<rect x="0" y="0" width="534" height="213" fill="#F9F8F3"/>')
    for k,(note,pc) in enumerate(WHITE):
        x=base+k*W
        fill=ROOT if pc in active and active[pc]==0 else TEAL if pc in active else '#FFFFFF'
        rows.append(f'<rect x="{x}" y="9" width="{W}" height="{h}" fill="{fill}" stroke="#303735" stroke-width="1.4"/>')
        fg='white' if pc in active else INK
        rows.append(f'<text x="{x+W/2}" y="180" text-anchor="middle" font-family="Lato, sans-serif" font-weight="700" font-size="17" fill="{fg}">{note}</text>')
        if pc in active and labels.get(pc):
            rows.append(f'<text x="{x+W/2}" y="147" text-anchor="middle" font-family="Lato" font-size="12" fill="white">{escape(labels[pc])}</text>')
    for note,pc,left in BLACK:
        x=base+(left+1)*W-23
        fill=ROOT if pc in active and active[pc]==0 else TEAL if pc in active else '#293133'
        rows.append(f'<rect x="{x}" y="9" width="46" height="111" rx="1" fill="{fill}" stroke="#1E2525" stroke-width="1.5"/>')
        if pc in active:
            display=next((n for n in notes if PCH[n]==pc),note)
            rows.append(f'<text x="{x+23}" y="73" text-anchor="middle" font-family="Lato" font-weight="700" font-size="15" fill="white">{escape(display)}</text>')
            if labels.get(pc):rows.append(f'<text x="{x+23}" y="99" text-anchor="middle" font-family="Lato" font-size="12" fill="white">{escape(labels[pc])}</text>')
    rows.append('</svg>')
    return ''.join(rows)

def fretboard():
    # Dm A-minor-shaped barre chord at fifth fret: x57765, strings lowest to highest.
    out=['<svg viewBox="0 0 540 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Movable D minor guitar chord x57765; sounding strings D3 A3 D4 F4 A4">']
    out+=['<rect width="540" height="230" fill="#F7F5F0"/>']
    xs=[58,143,228,313,398,483]
    for x,s in zip(xs,['E','A','D','G','B','e']):
        out.append(f'<text x="{x}" y="21" text-anchor="middle" font-family="Lato" font-size="15" fill="{MUTED}">{s}</text>')
        out.append(f'<line x1="{x}" y1="38" x2="{x}" y2="188" stroke="#777B79" stroke-width="{2 if s in ["E","A"] else 1.1}"/>')
    for f in range(5):
        y=38+f*38
        out.append(f'<line x1="58" y1="{y}" x2="483" y2="{y}" stroke="{INK}" stroke-width="{3 if f==0 else 1.2}"/>')
        if f<4:out.append(f'<text x="22" y="{y+25}" font-family="Lato" font-size="13" fill="{MUTED}">{5+f}</text>')
    fing=[None,5,7,7,6,5]; pitch=['×','D3','A3','D4','F4','A4']
    out.append(f'<text x="58" y="74" text-anchor="middle" font-family="Lato" font-size="26" fill="{MUTED}">×</text>')
    for i in range(1,6):
        y=57+(fing[i]-5)*38
        fill=ROOT if i==1 else TEAL
        out.append(f'<circle cx="{xs[i]}" cy="{y}" r="20" fill="{fill}"/>')
        out.append(f'<text x="{xs[i]}" y="{y+5}" text-anchor="middle" font-family="Lato" font-weight="700" font-size="15" fill="white">{pitch[i]}</text>')
    out.append('</svg>')
    return ''.join(out)

def modal_strip(name,notes,degrees,alter_index=5):
    out=['<div class="modal-strip"><div class="modal-name">'+name+'</div><div class="modal-notes">']
    for i,(n,d) in enumerate(zip(notes,degrees)):
        klass='root' if i==0 else ('alter' if i==alter_index else '')
        out.append(f'<div class="pitch {klass}"><strong>{escape(n)}</strong><span>{escape(d)}</span></div>')
    out.append('</div></div>')
    return ''.join(out)

HEADER='<div class="header"><span>PIANO WITHOUT FEAR OF BLACK KEYS</span><span>WORKING CHAPTER / 01</span></div>'

def foot(n,topic):
    return f'<div class="footer"><span>{topic}</span><span>{n:02d}</span></div>'

def page(n,tag,body):
    return f'<section class="page">{HEADER}<div class="content"><div class="section-tag">{tag}</div>{body}</div>{foot(n,"GEOMETRY / HARMONY / TRANSFER")}</section>'

pages=[]
pages.append('''<section class="page cover">
<div class="cover-header">A SECOND-EDITION STUDY<br/>TOMÁS LAURENZO</div>
<div class="cover-rule"></div>
<div class="cover-centre"><div class="cover-number">01 — EXPERIMENTAL CHAPTER</div><h1>The shape<br/>is not <em>the chord.</em></h1><p>What a guitarist’s fingers know, what the notes reveal, and why the piano makes the same music feel different.</p></div>
<div class="cover-geometry"><div class="cover-box copper">1<span>ROOT</span></div><div class="cover-box teal">♭3<span>QUALITY</span></div><div class="cover-box ivory">5<span>INTERVAL</span></div><div class="cover-arrow">→</div><div class="cover-keyboard">D · F · A<br/><small>NOTES, NOT A FINGERING</small></div></div>
<div class="cover-bottom"><span>PIANO WITHOUT FEAR OF BLACK KEYS</span><span>24 OCTOBER 2026 · PROTOTYPE, NOT AN EDITION</span></div>
</section>''')

pages.append(page(2,'01 / RECOVERING A FAMILIAR CHORD',f'''
<h2>Start with something<br/>you can already play.</h2>
<p class="lead">Play an open D minor chord on guitar: <b>xx0231</b>. You may know this gesture so well that you no longer think about it. But which pitches actually sound?</p>
<div class="wide-rule"></div>
<div class="two-col"><div><div class="mini-label">OPEN D MINOR · GUITAR</div><div class="grip"><span>×</span><span>×</span><span>0</span><span>2</span><span>3</span><span>1</span></div><div class="grip-notes">LOW E · A · D · G · B · HIGH E</div></div>
<div><div class="mini-label">SOUNDING PITCHES</div><div class="note-stack"><b>D3</b><b>A3</b><b>D4</b><b>F4</b></div><p class="small">The chord contains four sounding notes, including two Ds at different octaves.</p></div></div>
<div class="takeaway"><div class="mini-label">CHORD TONES</div><div class="formula"><span class="root-ink">D</span> <span>F</span> <span>A</span><i>→</i><span class="root-ink">1</span><span>♭3</span><span>5</span></div><p>These three note names constitute a D minor triad. Its minor third, F, distinguishes it from D major, where the third is F♯.</p></div>
<h3>Three related, different descriptions</h3><div class="divided-row"><b>Chord identity</b><span>D minor</span></div><div class="divided-row"><b>Chord tones</b><span>D – F – A</span></div><div class="divided-row"><b>Actual guitar voicing</b><span>D3 – A3 – D4 – F4</span></div>
<p class="small bottom-note">The first tells you what chord it is; the second names its constituent pitches without octaves; the third specifies which pitches this guitar fingering produces.</p>
'''))

pages.append(page(3,'02 / ONE FORMULA, DIFFERENT INTERFACES',f'''
<h2>Move the chord.<br/>Watch the shape change.</h2>
<p class="lead">A movable A-minor-shaped barre chord at fret five sounds D minor. Move it up one fret and it sounds E♭ minor. On guitar the grip survives; on piano the same chord quality takes a very different shape.</p>
<div class="fret-figure"><div class="mini-label">GUITAR · MOVABLE BARRE / x57765</div>{fretboard()}<div class="figure-caption">D minor: D3–A3–D4–F4–A4. One fret higher: E♭3–B♭3–E♭4–G♭4–B♭4.</div></div>
<div class="keyboard-grid"><div class="kbd-figure"><div class="mini-label">PIANO / D MINOR</div>{keyboard(['D','F','A'],{2:'1',5:'♭3',9:'5'})}<div class="caption-bold">D – F – A <span>three white keys</span></div></div><div class="kbd-figure"><div class="mini-label">PIANO / E♭ MINOR</div>{keyboard(['Eb','Gb','Bb'],{3:'1',6:'♭3',10:'5'})}<div class="caption-bold">E♭ – G♭ – B♭ <span>three black keys</span></div></div></div>
<div class="takeaway compact"><b>What stayed the same?</b> The interval formula: <strong>1–♭3–5</strong>. <b>What changed?</b> Every pitch, its location on the keyboard, and the most convenient movement of the hand.</div>
'''))

pages.append(page(4,'03 / MODES AS AUDIBLE ALTERATIONS',f'''
<h2>One changed note.<br/>A different modal sound.</h2>
<p class="lead">Keep D as the tonal centre. Hold a D minor chord or play a slow Dm7 accompaniment, and compare the following two scales. Six of their seven notes are the same.</p>
{modal_strip('D NATURAL MINOR / AEOLIAN',['D','E','F','G','A','B♭','C'],['1','2','♭3','4','5','♭6','♭7'])}
{modal_strip('D DORIAN',['D','E','F','G','A','B','C'],['1','2','♭3','4','5','6','♭7'])}
<div class="difference"><span>THE DIFFERENCE</span><strong>B♭</strong><i>→</i><strong>B</strong><small>lowered sixth → natural sixth</small></div>
<h3>Hear the alteration, not just the scale</h3>
<p>While D minor continues in the background, alternate <b>A–B♭–A</b> and <b>A–B–A</b>. Then play the paired two-bar cells. The tonic, the accompaniment and the surrounding notes stay unchanged.</p>
<div class="melody-row"><span>AEOLIAN</span><strong>A – C – <mark>B♭</mark> – A&nbsp; | &nbsp;F – G – F – D</strong></div>
<div class="melody-row"><span>DORIAN</span><strong>A – C – <mark>B</mark> – A&nbsp;&nbsp; | &nbsp;F – G – F – D</strong></div>
<p class="small bottom-note">Try it without a metronome first. Listen to the quality of the sixth degree against the sustained minor harmony. The exercise does not depend on assigning emotional adjectives to the modes.</p>
'''))

pages.append(page(5,'04 / WHY TONAL CENTRE MATTERS',f'''
<h2>Starting on D does not<br/>make the music Dorian.</h2>
<p class="lead">C major and D Dorian contain the same pitch classes: C, D, E, F, G, A and B. But a pitch collection does not determine which note a listener experiences as the tonal centre.</p>
<div class="compare-box"><div class="case"><div class="mini-label">SAME PITCH COLLECTION</div><div class="case-title">C major <i>↔</i> D Dorian</div><p>All seven pitches coincide. What changes is the tonic and the musical context supporting it.</p><div class="pills"><span class="root-pill">C</span><span>D</span><span>E</span><span>F</span><span>G</span><span>A</span><span>B</span></div></div>
<div class="case"><div class="mini-label">SAME TONIC</div><div class="case-title">D Aeolian <i>↔</i> D Dorian</div><p>D remains the centre. Only the sixth degree changes; this gives us a controlled aural comparison.</p><div class="pills"><span class="root-pill">D</span><span>E</span><span>F</span><span>G</span><span>A</span><span class="alter-pill">B♭ / B</span><span>C</span></div></div></div>
<h3>Which comparison answers your question?</h3>
<div class="divided-row"><b>Where do the notes come from?</b><span>Compare shared pitch collections.</span></div><div class="divided-row"><b>What makes Dorian sound Dorian?</b><span>Keep D as the tonic; hear its natural sixth.</span></div>
<div class="takeaway compact">Playing a C major scale beginning on D, over a C major accompaniment, does not by itself establish D Dorian. Harmony, emphasis, phrasing and the experience of a tonal centre matter.</div>
'''))

pages.append(page(6,'05 / TRANSFER TO AN UNFAMILIAR KEY',f'''
<h2>Move the relationship,<br/>not the fingering.</h2>
<p class="lead">The D-minor comparison was familiar. Now transpose it to F♯ minor. First construct the tonic chord, then choose the sixth degree from the formula, before consulting a keyboard diagram.</p>
<div class="accent-formula"><b>F♯ minor chord</b><strong>F♯ – A – C♯</strong><span>1 – ♭3 – 5</span></div>
{modal_strip('F♯ AEOLIAN',['F♯','G♯','A','B','C♯','D','E'],['1','2','♭3','4','5','♭6','♭7'])}
{modal_strip('F♯ DORIAN',['F♯','G♯','A','B','C♯','D♯','E'],['1','2','♭3','4','5','6','♭7'])}
<div class="mini-label" style="margin-top:9mm">TONIC CHORD ON PIANO</div>
<div class="wide-keyboard">{keyboard(['F#','A','C#'],{6:'1',9:'♭3',1:'5'})}</div>
<div class="takeaway compact">The significant alteration is <b>D → D♯</b>. The musical relationship is the same one you heard in D minor; its pitch spelling and physical keyboard locations have changed.</div>
'''))

pages.append(page(7,'06 / LEARNING CHECK',f'''
<h2>Can you recover<br/>the relationship?</h2>
<p class="lead">Try these tasks without referring to the previous pages. The point is not speed or perfect technique, but whether you can find your way from a musical gesture to the relationships it embodies.</p>
<ol class="tasks">
<li><b>Identify.</b> From open D minor on guitar, name its three chord tones and then its four actual sounding pitches.</li>
<li><b>Change.</b> Turn D minor into D major by moving only one chord tone. Which one moved, and by how many semitones?</li>
<li><b>Listen.</b> Play D Aeolian and D Dorian against the same Dm7 accompaniment. Identify the degree that changes and improvise a phrase that makes it perceptible.</li>
<li><b>Transpose.</b> Without consulting the table, play F♯ Aeolian and F♯ Dorian. Identify their different sixth degrees.</li>
<li><b>Compare.</b> What is preserved when a guitarist moves a barre chord up one fret? What is preserved when a pianist rebuilds the same chord formula a semitone higher?</li>
</ol>
<div class="answer-box"><div class="mini-label">CHECK YOUR ANSWERS AFTER PLAYING</div><p><b>1.</b> D–F–A; D3–A3–D4–F4. <b>2.</b> F becomes F♯, a semitone higher. <b>3.</b> B♭/B: ♭6/6 against D. <b>4.</b> D/D♯ against F♯. <b>5.</b> The interval relationships and chord quality; the notes and register change by a semitone, while the instrument geometry presents the new pitches differently.</p></div>
<p class="small bottom-note">Next: inversions and voice leading. Once we can identify a chord independently of the way we play it, we can choose voicings according to how their individual notes move.</p>
'''))

css=r'''<style>
@page { size: A4; margin:0 }
*{box-sizing:border-box} html,body{margin:0;background:#eee}body{font-family:Lato, 'Noto Sans',sans-serif;color:#222828}
.page{height:297mm;width:210mm;background:#F7F5F0;position:relative;page-break-after:always;overflow:hidden;padding:18mm 19mm 18mm}
.header,.footer{display:flex;justify-content:space-between;align-items:center;text-transform:uppercase;letter-spacing:.13em;font-size:8.1pt;font-weight:700;color:#606A68}
.header{border-bottom:1px solid #CFCBC2;padding-bottom:5mm}.footer{position:absolute;bottom:13mm;left:19mm;right:19mm;border-top:1px solid #CFCBC2;padding-top:3mm;font-size:7.5pt}
.content{padding-top:14mm}.section-tag,.mini-label{font-weight:800;text-transform:uppercase;letter-spacing:.135em;color:#A9563C;font-size:9pt;margin-bottom:4mm}
h2,h3{font-family:'Noto Serif',Georgia,serif;font-weight:500;line-height:1.19;color:#222828}h2{font-size:27pt;margin:0 0 8mm;letter-spacing:-.023em}h3{font-size:15pt;margin:8mm 0 4mm}
p{font-size:11pt;line-height:1.52;margin:0 0 4mm}p.lead{font-size:12.7pt;line-height:1.52;max-width:165mm;margin-bottom:9mm;color:#3C4644}p.small{font-size:9.6pt;line-height:1.48;color:#56625F}b,strong{font-weight:800}.wide-rule{border-top:1px solid #D0CCC3;margin:0 0 8mm}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:10mm;margin:0 0 10mm}.grip{display:flex;gap:1.5mm;margin:5mm 0 2mm}.grip span{display:inline-flex;align-items:center;justify-content:center;width:10.3mm;height:12mm;background:#EEE9DF;border-bottom:2px solid #D2CBC0;font-family:Lato;font-size:18pt;font-weight:800}.grip span:first-child,.grip span:nth-child(2){color:#909793}.grip-notes{font-size:7.5pt;color:#687270;letter-spacing:.06em}.note-stack{display:flex;gap:2mm;margin-top:6mm}.note-stack b{display:flex;align-items:center;justify-content:center;width:16mm;height:13mm;background:#247B78;color:white;font-size:15pt}.note-stack b:first-child{background:#AA573E}
.takeaway{border-left:3.5pt solid #AA573E;padding:6mm 7mm;background:#EEEAE2;margin:6mm 0 8mm}.takeaway p{margin:0}.takeaway.compact{font-size:10.6pt;line-height:1.47;margin-top:8mm;padding:5mm 6mm}.formula{display:flex;gap:4mm;align-items:center;font-size:20pt;font-weight:900;margin:2mm 0 3mm}.formula span{color:#247B78}.formula .root-ink{color:#AA573E}.formula i{font-size:17pt;color:#A8A49C;font-weight:400}.divided-row{display:flex;justify-content:space-between;gap:5mm;padding:3.3mm 0;border-top:1px solid #D4D1C9;font-size:10.6pt}.divided-row span{max-width:95mm;text-align:right}.bottom-note{margin-top:7mm}
.fret-figure{background:#F4F1EA;border:1px solid #D3CEC4;padding:4mm 5mm 3mm;margin-bottom:7mm}.fret-figure svg{display:block;width:100%;height:45mm}.figure-caption{font-size:8.9pt;color:#56625F;margin-top:1mm}
.keyboard-grid{display:grid;grid-template-columns:1fr 1fr;gap:5mm}.kbd-figure{background:#F4F1EA;padding:4mm 3mm 3mm;border:1px solid #D3CEC4}.kbd-figure svg{display:block;width:100%;height:auto}.caption-bold{font-weight:800;font-size:10.3pt;margin-top:2mm}.caption-bold span{display:block;font-weight:400;color:#66716D;font-size:9pt;margin-top:1mm}
.modal-strip{margin:0 0 9mm}.modal-name{font-size:9pt;font-weight:800;letter-spacing:.12em;color:#394341;margin-bottom:3mm}.modal-notes{display:grid;grid-template-columns:repeat(7,1fr);gap:2mm}.pitch{height:17mm;border:1px solid #D4D1C9;background:#ECEAE3;display:flex;flex-direction:column;align-items:center;justify-content:center}.pitch strong{font-size:15pt}.pitch span{font-size:9pt;margin-top:1mm;color:#687471}.pitch.root{background:#AA573E;border-color:#AA573E;color:white}.pitch.root span{color:white}.pitch.alter{background:#CDE3DE;border-color:#247B78;color:#165F5C}.pitch.alter span{color:#165F5C}
.difference{display:flex;gap:5mm;align-items:center;justify-content:center;border-top:1px solid #D4D1C9;border-bottom:1px solid #D4D1C9;padding:5mm 0;margin:2mm 0 8mm}.difference span{font-size:8pt;color:#626B67;letter-spacing:.1em}.difference strong{font-family:'Noto Serif';font-size:24pt;color:#247B78}.difference i{font-style:normal;color:#A1A5A0}.difference small{font-size:9pt;color:#65706D}
.melody-row{display:flex;align-items:center;gap:8mm;background:#EEEBE3;padding:4mm 5mm;border-bottom:2mm solid #F7F5F0}.melody-row>span{font-size:8.3pt;color:#68726F;letter-spacing:.07em;width:22mm}.melody-row strong{font-size:11.4pt}.melody-row mark{color:#A9563C;background:#F2DED1;padding:1mm;border-radius:1mm}
.compare-box{border:1px solid #D4D1C9;margin:5mm 0 5mm}.case{padding:4mm 6mm 4mm}.case+.case{border-top:1px solid #D4D1C9}.case-title{font-family:'Noto Serif';font-size:18pt;margin:0 0 3mm}.case-title i{font-style:normal;color:#AA573E}.case p{color:#58615E;margin:0 0 3mm}.pills{display:flex;gap:2mm}.pills span{display:inline-flex;align-items:center;justify-content:center;min-width:11mm;height:11mm;padding:0 3mm;background:#E7E3D9;color:#3C4844;font-weight:800}.pills .root-pill{background:#AA573E;color:white}.pills .alter-pill{background:#CDE3DE;color:#1A6A65}
.accent-formula{display:flex;align-items:center;gap:6mm;background:#EDE8DC;padding:5mm;margin:6mm 0 8mm}.accent-formula b{font-size:10.5pt}.accent-formula strong{font-size:18pt;color:#AA573E}.accent-formula span{font-size:10pt;color:#5C6662}.wide-keyboard{width:110mm;margin:2mm auto 2mm}.wide-keyboard svg{display:block;width:100%}
.tasks{padding-left:7mm;margin-top:4mm}.tasks li{font-size:11.1pt;line-height:1.5;margin-bottom:5.5mm;padding-left:3mm}.tasks li::marker{color:#AA573E;font-weight:800}.answer-box{padding:6mm 7mm;background:#EDEAE2;border-top:2.5pt solid #247B78;margin-top:7mm}.answer-box p{font-size:9.8pt;line-height:1.58;margin:0}
.cover{background:#F7F5F0;padding:22mm 19mm 20mm}.cover-header,.cover-bottom{display:flex;justify-content:space-between;color:#51615B;font-size:10pt;letter-spacing:.12em;font-weight:800}.cover-rule{border-top:4px solid #AA573E;margin-top:8mm}.cover-centre{margin-top:40mm}.cover-number{font-size:10pt;color:#A9563C;letter-spacing:.14em;font-weight:800;margin-bottom:8mm}.cover h1{font-family:'Noto Serif',Georgia,serif;font-size:44pt;font-weight:500;line-height:1.14;letter-spacing:-.04em;margin:0 0 10mm}.cover h1 em{font-weight:500;color:#AA573E}.cover-centre>p{font-size:14.5pt;line-height:1.47;max-width:148mm;color:#49524F}.cover-geometry{display:flex;gap:3mm;align-items:center;position:absolute;left:19mm;right:19mm;bottom:43mm}.cover-box{display:flex;flex-direction:column;justify-content:center;align-items:center;width:22mm;height:25mm;font-size:20pt;font-weight:800}.cover-box span{font-size:7pt;letter-spacing:.07em;font-weight:700;margin-top:2mm}.cover-box.copper{background:#AA573E;color:white}.cover-box.teal{background:#247B78;color:white}.cover-box.ivory{background:#E3DDD0;color:#303B37}.cover-arrow{color:#6C7671;font-size:18pt;margin:0 2mm}.cover-keyboard{font-family:'Noto Serif';font-size:21pt;line-height:1.3;padding-left:4mm}.cover-keyboard small{font:800 8pt Lato;letter-spacing:.1em;color:#606A68}.cover-bottom{position:absolute;bottom:14mm;left:19mm;right:19mm;border-top:1px solid #CFCBC2;padding-top:4mm;font-size:7.5pt}
</style>'''

html='''<!doctype html><html lang="en"><head><meta charset="utf-8"/><title>Piano Without Fear of Black Keys — prototype 01</title>'''+css+'''</head><body>'''+''.join(pages)+'''</body></html>'''
(OUT/'prototype-01-design-proof.html').write_text(html,encoding='utf-8')
HTML(string=html,base_url=str(OUT)).write_pdf(str(OUT/'Piano_Without_Fear_v2_Chapter_Prototype.pdf'))
doc=fitz.open(str(OUT/'Piano_Without_Fear_v2_Chapter_Prototype.pdf'))
print('PDF',len(doc),'pages')
for i,p in enumerate(doc):
    text=p.get_text()
    print(i+1,'chars',len(text),'images',len(p.get_images()),'page',tuple(round(x) for x in p.rect),'text_tail',repr(text[-70:]))
    pix=p.get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False)
    pix.save(str(OUT/f'page-{i+1:02d}.png'))
# contact sheet for QA
files=sorted(OUT.glob('page-??.png'))
thumb_w=420; thumb_h=594;gap=20
sheet=Image.new('RGB',(4*thumb_w+5*gap,2*thumb_h+3*gap),'#d7d5ce')
for i,f in enumerate(files):
    im=Image.open(f).convert('RGB'); im.thumbnail((thumb_w,thumb_h))
    x=gap+(i%4)*(thumb_w+gap);y=gap+(i//4)*(thumb_h+gap)
    sheet.paste(im,(x,y))
sheet.save(OUT/'contact-sheet.png')
