"""Find checked partial-turn loops which restore the original piece diagram."""
import json,math,time
from pathlib import Path
import numpy as np
from piece_orbits import Puzzle,rot,groups

A=json.loads(Path('work/extended_atlas.json').read_text())
for f in A['families']:
 for v in f['variants']:
  if v.get('orbitStatus')!='regular-only':continue
  p=Puzzle(f,v,A);initial=np.tile(np.eye(3),(p.N,1,1));moves=list(v['moves']);loops=[];start=time.time();checks=0
  def turn(Rs,axis,angle,legal=None):
   legal=dict(p.legal(Rs)) if legal is None else legal
   if axis not in legal:return None
   result=Rs.copy();result[legal[axis]]=rot(p.axes[axis],math.radians(angle))@Rs[legal[axis]]
   return result
  def check(Rs,path):
   global checks
   checks+=1;seeds=np.einsum('nij,nj->ni',Rs,p.seeds);perm=[p.locate(s) for s in seeds]
   if sorted(perm)!=list(range(p.N)):return
   if all(any(j in g and k in g for g in groups(p.N,moves)) for j,k in enumerate(perm)):return
   for j,k in enumerate(perm):
    if not p.fits(j,Rs[j],k) or not p.fits(k,Rs[j].T,j):return
   moves.append(dict(permutation=perm));loops.append(dict(path=path,permutation=perm));print('LOOP',f['key'],v['angle'],path,flush=True)
  normals={m['axis']-1:m['angle'] for m in v['moves']}
  for first in v['extraSwitches']:
   i=first['axis']-1;a=first['angle'];R1=turn(initial,i,a);legal1=dict(p.legal(R1))
   for j in legal1:
    if j==i or j not in normals:continue
    if p.axes[i]@p.axes[j]<=math.cos(2*p.alpha)+1e-7:continue
    for b in sorted({normals[j],-normals[j]}):
     R2=turn(R1,j,b,legal1);legal2=dict(p.legal(R2))
     R3=turn(R2,i,-a,legal2)
     if R3 is None:continue
     path=[[i+1,a],[j+1,b],[i+1,-a]];check(R3,path)
     R4=turn(R3,j,-b)
     if R4 is not None:check(R4,path+[[j+1,-b]])
   if groups(p.N,moves)==v['geometricUpperBound']:break
  v['orbits']=groups(p.N,moves);v['restoringLoops']=loops
  if v['orbits']==v['geometricUpperBound']:v['orbitStatus']='complete'
  print('RESULT',f['key'],round(v['angle'],6),v['orbitStatus'],[len(g) for g in v['orbits']],len(loops),'loops',checks,'checked',round(time.time()-start,2),'sec',flush=True)
  Path('work/restored_atlas.json').write_text(json.dumps(A,separators=(',',':')))
Path('work/restored_atlas.json').write_text(json.dumps(A,separators=(',',':')))
