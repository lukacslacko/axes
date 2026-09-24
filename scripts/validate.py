import json,math
from pathlib import Path
import numpy as np
from piece_orbits import Puzzle,rot
A=json.loads(Path('assets/atlas.json').read_text());count=0
for f in A['families']:
 for v in f['variants']:
  assert sorted(j for g in v['orbits'] for j in g)==list(range(v['count']))
  if v['angle']==0:continue
  p=Puzzle(f,v,A)
  for m in v['moves']:
   R=rot(p.axes[m['axis']-1],math.radians(m['angle']))
   for j,k in enumerate(m['permutation']):
    if m['axis'] in v['pieces'][j]['members']:
     assert p.fits(j,R,k) and p.fits(k,R.T,j),(f['key'],v['angle'],m['axis'],j,k)
     count+=1
  for w in v.get('witnesses',[]):
   Rs=[np.eye(3) for _ in range(p.N)]
   for axis,angle in w['path']:
    legal=dict(p.legal(Rs));i=axis-1;assert i in legal,(f['key'],v['angle'],w)
    R=rot(p.axes[i],math.radians(angle));Rs=[R@Q if j in legal[i] else Q for j,Q in enumerate(Rs)]
   j=w['piece'];k=w['target'];R=Rs[j]
   assert p.locate(R@p.seeds[j])==k and p.fits(j,R,k) and p.fits(k,R.T,j),(f['key'],v['angle'],w)
   count+=1
cases=sum(len(f['variants']) for f in A['families'])
print('Validated',count,'whole-sector move images and jumbling witnesses, and all',cases,'orbit partitions.')

# Switching angles on the standard families cannot introduce a new cut normal.
alignments=0
for f in A['families'][:-1]:
 for deep in [False,True]:
  U=[np.array(u) for u in f['axes']]
  if deep:
   for u in U.copy():
    if not any(np.linalg.norm(-u-v)<1e-7 for v in U):U.append(-u)
  for u in U:
   for a in U:
    for b in U:
     if abs(u@a-u@b)>1e-7:continue
     aa=a-(u@a)*u;bb=b-(u@b)*u
     if np.linalg.norm(aa)<1e-7:continue
     phi=math.atan2(u@np.cross(aa,bb),aa@bb);R=rot(u,phi)
     assert all(min(np.linalg.norm(R@x-y) for y in U)<1e-7 for x in U),(f['key'],deep,phi)
     alignments+=1
print('Validated',alignments,'cut-normal alignments on standard configurations.')

from html.parser import HTMLParser
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.cards=[];self.canvases=0
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.append(d['id'])
  if tag=='a':self.links.append(d.get('href',''))
  if tag=='canvas':self.canvases+=1
  if tag=='article' and d.get('class')=='puzzle':self.cards.append(d)
page=Page();page.feed(Path('index.html').read_text())
assert len(page.ids)==len(set(page.ids))
assert len(page.cards)==page.canvases==cases
for link in page.links:
 if link.startswith('#'):assert link[1:] in page.ids,link
 elif '://' not in link:assert Path(link).exists(),link
for card in page.cards:
 f=A['families'][int(card['data-family'])];v=f['variants'][int(card['data-variant'])]
 assert card['id']==f['key']+'-'+card['data-variant']
print('Validated',cases,'unique gallery cards, their data references, and navigation targets.')
