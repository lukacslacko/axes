import json,collections,sys,time
from pathlib import Path
import numpy as np
from piece_orbits import Puzzle,rot,groups

atlas=json.loads(Path('work/bounded_atlas.json').read_text());f=atlas['families'][-1]
for v in f['variants']:
 if v['angle']==0:
  v['orbits']=[[0]];v['moves']=[];continue
 p=Puzzle(f,v,atlas);edges=[];witnesses=[];initial=[np.eye(3) for _ in range(p.N)];reached={(j,j) for j in range(p.N)}
 queue=collections.deque([(initial,[])]);seen=set();start=time.time();target=v['orbitUpperBound'];maxdepth=0;truncated=False
 while queue and len(seen)<10000:
  Rs,path=queue.popleft();key=tuple(np.round(np.array(Rs).flatten(),8))
  if key in seen:continue
  seen.add(key);maxdepth=max(maxdepth,len(path))
  for j,R in enumerate(Rs):
   k=p.locate(R@p.seeds[j])
   if k>=0 and j!=k and abs(v['pieces'][j]['area']-v['pieces'][k]['area'])<.001 and p.fits(j,R,k) and p.fits(k,R.T,j):
    current=groups(p.N,edges)
    if (j,k) not in reached:
     reached.add((j,k))
     perm=list(range(p.N));perm[j],perm[k]=k,j;edges.append({'permutation':perm});witnesses.append(dict(piece=j,target=k,path=path))
     print('WITNESS',v['angle'],j,k,path,flush=True)
  current=groups(p.N,edges)
  if current==target and all((j,k) in reached for g in target for j in g for k in g):break
  if len(path)>=18:truncated=True;continue
  for i,inside in p.legal(Rs):
   for phi in p.candidates(Rs,i,inside):
    R=rot(p.axes[i],phi);nextRs=[R@Q if j in inside else Q for j,Q in enumerate(Rs)]
    queue.append((nextRs,path+[(i+1,round(float(np.degrees(phi)),8))]))
 exhausted=not queue and not truncated
 assert all((j,k) in reached for g in current for j in g for k in g),('An orbit union lacks a direct reachability witness',v['angle'],current,reached)
 print('RESULT',v['angle'],len(seen),len(queue),time.time()-start,current,'target',target,'exhausted',exhausted,'maxdepth',maxdepth,flush=True)
 v['orbits']=current;v['witnesses']=witnesses;v['orbitComplete']=current==target or exhausted;v['switchStates']=len(seen);v['maxSearchDepth']=maxdepth;v['orbitMethod']='Numerically certified legal-turn classes (analytic arc bounds; geometric upper bound or exhaustive switching graph)';v['moves']=[]
 Path('work/jumble_atlas.json').write_text(json.dumps(atlas,separators=(',',':')))

Path('work/jumble_atlas.json').write_text(json.dumps(atlas,separators=(',',':')))
