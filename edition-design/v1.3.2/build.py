from pathlib import Path
from bs4 import BeautifulSoup
import subprocess, re, hashlib, sys
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
SRC= ROOT.parent.parent
OUT=ROOT
OUT.mkdir(exist_ok=True)
subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', str(SRC/'tests'), '-v'], check=True)
old=(SRC/'piano_transposition_manual.md').read_text(encoding='utf-8')
new=old
replacements={
'<h1 class="cover-title">Piano Without Fear of Black Keys</h1>':'<h1 class="cover-title">Piano<br>Without Fear<br>of Black Keys</h1>',
'<p class="cover-subtitle">A transposition-first manual for piano, Ableton Push/Note, and guitar</p>':'<p class="cover-subtitle">A transposition-first manual<br>for piano,<br>Ableton Push and Note,<br>and guitar</p>',
'<p class="cover-author">Tomás Laurenzo</p>':'<p class="cover-author">Tomas Laurenzo</p>',
'<p class="cover-version">Version 1.3 - September 2026</p>':'<p class="cover-version">Version 1.3.2 · October 2026</p>',
}
for k,v in replacements.items():
    assert new.count(k)==1,(k,new.count(k))
    new=new.replace(k,v)
assert new.split('</section>',1)[1] == old.split('</section>',1)[1], 'Body content changed'
(OUT/'piano_transposition_manual_v1.3.2.md').write_text(new,encoding='utf-8')
css=(ROOT/'book.css')
html_file=OUT/'Piano_Without_Fear_of_Black_Keys_v1.3.2.html'
subprocess.run(['pandoc', str(OUT/'piano_transposition_manual_v1.3.2.md'), '-s','-t','html5','--metadata','title=Piano Without Fear of Black Keys', '-o',str(html_file)],check=True)
soup=BeautifulSoup(html_file.read_text(encoding='utf-8'),'html.parser')
# The pandoc-generated title duplicates the actual designed book cover.
for el in list(soup.body.children):
    if getattr(el,'name',None)=='header' and 'title-block-header' in el.get('id',''):
        el.decompose()
# Some pandoc versions emit a standalone h1.title.
for h in soup.select('h1.title'):
    if h.find_parent('section',class_='cover') is None: h.decompose()
for el in soup.select('section.cover + .pagebreak'):
    el.decompose()
for img in soup.select('img[src^="assets/"]'):
    name=img['src'].split('/')[-1]
    assert (SRC/'assets'/name).exists(), name
    img['src']='../../assets/'+name
for table in soup.find_all('table'):
    thead=table.find('thead')
    count=len(thead.find_all('th')) if thead else 0
    if count>=4: table['class']=table.get('class',[])+['wide']
# Insert CSS link in head, using file URL resolution.
link=soup.new_tag('link', rel='stylesheet', href='book.css')
soup.head.append(link)
html_file.write_text(str(soup),encoding='utf-8')
PDF=OUT/'Piano_Without_Fear_of_Black_Keys_v1.3.2.pdf'
HTML(filename=str(html_file),base_url=str(html_file)).write_pdf(str(PDF))
print('PDF',PDF,PDF.stat().st_size,'bytes')
print('SOURCE_SHA256',hashlib.sha256(old.encode()).hexdigest())
print('COVER_CHANGE_ONLY',new.split('</section>',1)[1]==old.split('</section>',1)[1])
