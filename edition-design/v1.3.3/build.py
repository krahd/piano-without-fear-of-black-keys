"""Build the current book edition from canonical Markdown without rewriting its prose."""
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
import subprocess, hashlib, sys, re
from weasyprint import HTML
ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent.parent
VERSION = '1.3.3'
assert (SRC/'piano_transposition_manual.md').exists()
subprocess.run([sys.executable,'-m','unittest','discover','-s',str(SRC/'tests'),'-v'],check=True)
old = (SRC/'piano_transposition_manual.md').read_text(encoding='utf-8')
new = old
replacements={
    '<h1 class="cover-title">Piano Without Fear of Black Keys</h1>': '<h1 class="cover-title">Piano<br>Without Fear<br>of Black Keys</h1>',
    '<p class="cover-subtitle">A transposition-first manual for piano, Ableton Push/Note, and guitar</p>': '<p class="cover-subtitle">A transposition-first manual<br>for piano,<br>Ableton Push and Note,<br>and guitar</p>',
    '<p class="cover-author">Tomás Laurenzo</p>': '<p class="cover-author">Tomas Laurenzo</p>',
    '<p class="cover-version">Version 1.3 - September 2026</p>': '<p class="cover-version">Version 1.3.3 · October 2026</p>',
}
for before,after in replacements.items():
    assert new.count(before)==1,(before, new.count(before))
    new=new.replace(before,after)
assert new.split('</section>',1)[1]==old.split('</section>',1)[1], 'Builder must not change non-cover text'
md=ROOT/'piano_transposition_manual_v1.3.3.md'
md.write_text(new, encoding='utf-8')
html_file=ROOT/'Piano_Without_Fear_of_Black_Keys_v1.3.3.html'
subprocess.run(['pandoc',str(md),'-s','-t','html5',
                '--metadata','title=Piano Without Fear of Black Keys',
                '--metadata','author=Tomas Laurenzo',
                '--metadata','lang=en-GB',
                '-o',str(html_file)],check=True)
soup=BeautifulSoup(html_file.read_text(encoding='utf-8'),'html.parser')
for el in list(soup.body.children):
    if getattr(el,'name',None)=='header' and el.get('id')=='title-block-header': el.decompose()
for h in soup.select('h1.title'):
    if h.find_parent('section',class_='cover') is None:h.decompose()
for el in soup.select('section.cover + .pagebreak'):el.decompose()
for img in soup.select('img[src^="assets/"]'):
    name=img['src'].split('/')[-1]
    assert (SRC/'assets'/name).exists(),name
    img['src']='../../assets/'+name
for table in soup.select('table'):
    thead=table.find('thead')
    if thead and len(thead.find_all('th'))>=4:table['class']=table.get('class',[])+['wide']
# Preserve table content; reflow the four-column glossary into legible two-column rows.
gloss=soup.select_one('table.glossary')
assert gloss
# The original glossary has two term/definition pairs per row.
# Replace the four-cell header as well, otherwise PDF engines allocate phantom columns.
head=gloss.find('thead'); assert head
head.clear();row=soup.new_tag('tr')
for name in ['Term','Meaning']:
    th=soup.new_tag('th');th.string=name;row.append(th)
head.append(row)
trs=list(gloss.select('tbody > tr'))
for tr in trs:
    cells=list(tr.find_all('td',recursive=False))
    if len(cells)!=4:raise AssertionError('Glossary structure changed')
    newrow=soup.new_tag('tr')
    for c in cells[2:]:newrow.append(c.extract())
    tr.insert_after(newrow)
# Split the cramped six-column seventh-chord chart into two narrower reference tables,
# keeping every chord spelling and its original order intact.
header=soup.find(id='seventh-chords-in-all-12-roots')
assert header and header.name in {'h2','h3'}
table=header.find_next('table')
assert table and len(table.select('thead tr th'))==6
rows=table.select('tbody tr')
assert len(rows)==12
left=soup.new_tag('table');left['class']=['split-chords']
right=soup.new_tag('table');right['class']=['split-chords']
for src_idx,dst in [(range(0,4),left),([0,4,5],right)]:
    for tag in ['thead','tbody']:
        group=soup.new_tag(tag)
        for tr in table.select(f'{tag} tr'):
            tr_new=soup.new_tag('tr')
            cells=tr.find_all(['td','th'],recursive=False)
            for k in src_idx:tr_new.append(BeautifulSoup(str(cells[k]),'html.parser').find(['td','th']))
            group.append(tr_new)
        dst.append(group)
for chart,label in [(left,'Major, dominant and minor seventh chords'),(right,'Half-diminished and diminished seventh chords')]:
    box=soup.new_tag('div');box['class']=['reference-subtable']
    h=soup.new_tag('p');h['class']=['table-subhead'];h.string=label
    box.append(h);box.append(chart)
    table.insert_before(box)
table.decompose()
# Generate printed page numbers and digital anchors from the existing contents list.
toc=soup.find(id='contents'); assert toc
ol=toc.find_next('ol');assert ol and len(ol.find_all('li',recursive=False))==15
ol['class']=ol.get('class',[])+['toc-list']
targets=[soup.find(id='preface')]
targets += [next(x for x in soup.select('h1[id]') if x['id'].startswith('part-'+roman.lower()+'---')) for roman in ['i','ii','iii','iv','v','vi','vii']]
targets += [next(x for x in soup.select('h1[id]') if x['id'].startswith('appendix-'+ch+'---')) for ch in 'abcdefg']
for li,target in zip(ol.find_all('li',recursive=False),targets):
    assert target and target.get('id')
    label=li.get_text(' ',strip=True)
    li.clear();a=soup.new_tag('a',href='#'+target['id']);a.string=label;li.append(a)
# Keep the preface's introductory sentence with its standalone D-minor chord example.
for p in soup.find_all('p'):
    if p.get_text(' ',strip=True)=='On D, that becomes:':
        following=p.find_next_sibling('p')
        assert following and following.get_text(' ',strip=True)=='D F A C'
        box=soup.new_tag('div');box['class']=['keep-example'];p.wrap(box);box.append(following.extract())
        break
else: raise AssertionError('Missing example to keep together')
# One-page conclusion should be a single logical unit, not a section split between pages.
philos=soup.find(id='one-page-philosophy');assert philos
closing=soup.new_tag('section');closing['class']=['finale'];philos.insert_before(closing)
n=philos
while n is not None:
    nxt=n.next_sibling;closing.append(n.extract());n=nxt
# Link plain-text references, but do not duplicate existing anchor tags.
regex=re.compile(r'https?://[^\s<>]+')
for textnode in list(soup.find_all(string=regex)):
    if textnode.parent.name in {'a','script','style','code'}:continue
    val=str(textnode);frags=[];start=0
    for match in regex.finditer(val):
        url=match.group(0).rstrip('.,;)')
        if match.start()>start:frags.append(NavigableString(val[start:match.start()]))
        a=soup.new_tag('a',href=url);a.string=url;frags.append(a)
        start=match.start()+len(url)
    if start<len(val):frags.append(NavigableString(val[start:]))
    for obj in reversed(frags):textnode.insert_after(obj)
    textnode.extract()
# Language and publisher metadata.
soup.html['lang']='en-GB'
for name,content in [('author','Tomas Laurenzo'),('description','A transposition-first manual for piano, Ableton Push and Note, and guitar')]:
    for existing in soup.head.select('meta[name="'+name+'"]'): existing.decompose()
    meta=soup.new_tag('meta');meta['name']=name;meta['content']=content;soup.head.append(meta)
link=soup.new_tag('link',rel='stylesheet',href='book.css');soup.head.append(link)
html_file.write_text(str(soup),encoding='utf-8')
pdf=ROOT/'Piano_Without_Fear_of_Black_Keys_v1.3.3.pdf'
# pdf_tags is an accessibility aid; tagging alone does not establish PDF/UA conformance.
HTML(filename=str(html_file),base_url=str(html_file)).write_pdf(str(pdf),pdf_tags=True,custom_metadata=True)
print('PDF',pdf,pdf.stat().st_size,'bytes')
print('SOURCE_SHA256',hashlib.sha256(old.encode()).hexdigest())
print('BODY_UNCHANGED_IN_BUILD',new.split('</section>',1)[1]==old.split('</section>',1)[1])
