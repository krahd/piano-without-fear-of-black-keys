import unittest
from pathlib import Path
from hashlib import sha256
ROOT=Path(__file__).resolve().parents[1]
class EditorialRegression(unittest.TestCase):
 def test_historical_snapshots_pinned(self):
  hashes={'v1.3':'0fd2c4030b21c7ce3b7454ac983a6821aec8acfe980f8ab978c301dc455a33b6','v1.3.1':'0fd2c4030b21c7ce3b7454ac983a6821aec8acfe980f8ab978c301dc455a33b6','v1.3.2':'e9c35a32d6280aae6efcdc6d19c208d3549e336304007874a2e097f8eb22dd49'}
  for ver,h in hashes.items():
   with self.subTest(ver=ver):self.assertEqual(sha256((ROOT/'edition-design'/ver/'frozen_manuscript.md').read_bytes()).hexdigest(),h)
 def test_progression_transposition_spelling(self):
  original=[['A3','C4','E4'],['A3','C4','F4'],['G3','C4','E4'],['G3','B3','D4']]
  target=[['Bb3','Db4','F4'],['Bb3','Db4','Gb4'],['Ab3','Db4','F4'],['Ab3','C4','Eb4']]
  pcs={'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
  import re
  def midi(x):
   m=re.fullmatch('([A-G])([#b]*)([0-9]+)',x);self.assertIsNotNone(m)
   return (int(m[3])+1)*12+pcs[m[1]]+m[2].count('#')-m[2].count('b')
  for a,b in zip(original,target):
   self.assertEqual([midi(y)-midi(x) for x,y in zip(a,b)],[1,1,1])
 def test_instructional_fixes_present(self):
  s=(ROOT/'piano_transposition_manual.md').read_text()
  for phrase in ['Fixed OFF','Fixed ON','Choose the workload by accuracy','The chord formula is unchanged','On Note, changing the key with In Key OFF']:
   self.assertIn(phrase,s)
  self.assertNotIn('The musical object is identical',s)
  self.assertNotIn('in a In-Key',s)
 def test_convenience_text_synced(self):
  s=(ROOT/'piano_transposition_manual.md').read_text().split('# Appendix A - ',1)[0].rstrip()+'\n'
  self.assertEqual((ROOT/'01_foundations_and_instruments.md').read_text(),s)
