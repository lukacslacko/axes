"""Audit where extra alignment angles can affect the ordinary move classes."""
import json,math,itertools,time
from pathlib import Path
import numpy as np
from piece_orbits import Puzzle,groups,rot
from orbit_bounds import congruences,bounds
from local_examples import rotations

A=json.loads(Path('work/orbit_atlas.json').read_text())
for f in A['families']:
 if f['key']=='jumble':continue
 for v in f['variants']:
  v['orbitStatus']='complete';v['extraSwitches']=[]
  if v['angle']==0:continue
  p=Puzzle(f,v,A)
  extra=[];seen=set()
  for i in range(len(p.axes)):
   for move in rotations(p.axes,i,v['angle']):
    key=(i,round(move['angle'],6))
    if not move['regular'] and key not in seen:seen.add(key);extra.append(move)
  if not extra:continue
  v['extraSwitches']=extra
  # Geometry provides an upper bound on any possible slot transfers.
  # Compare orbit representatives; all members of an ordinary orbit are
  # already linked by validated whole-sector permutations.
  base=v['orbits'];edges=list(v['moves']);anchored=set()
  for u in p.axes:
   ds=p.axes@u
   if all(d<p.h-1e-7 for d in ds if d<1-1e-7):
    j=p.locate(u)
    if j>=0:anchored.add(j)
  for j,x in enumerate(v['pieces']):
   if not x['members']:anchored.add(j)
  for g,h in itertools.combinations(base,2):
   if any(j in anchored for j in g+h):continue
   j=g[0];k=h[0]
   if congruences(p,j,k):
    perm=list(range(p.N));perm[j],perm[k]=k,j;edges.append(dict(permutation=perm))
  upper=groups(p.N,edges);v['geometricUpperBound']=upper
  if upper!=base:v['orbitStatus']='regular-only'
  print(f['key'],round(v['angle'],6),'extra',len(extra),'normal',[len(g) for g in base],'upper',[len(g) for g in upper],v['orbitStatus'],flush=True)
 Path('work/extended_atlas.json').write_text(json.dumps(A,separators=(',',':')))
