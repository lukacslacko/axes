"""Explore piece-diagram states, retaining executable loops for new slot orbits."""
import collections,hashlib,json,math,sys,time
from pathlib import Path
import numpy as np
from piece_orbits import Puzzle,rot,groups

def explore(f,v,A,maxstates=50000):
 p=Puzzle(f,v,A);initial=np.tile(np.eye(3),(p.N,1,1));edges=list(v['moves'])+[dict(permutation=m['permutation']) for m in v.get('restoringLoops',[])];loops=list(v.get('restoringLoops',[]));start=time.time()
 arc_features=[]
 for j,arcs in enumerate(p.boundaries()):
  features=[]
  for u,e,b,a,z in arcs:
   i=int(np.argmin(np.linalg.norm(p.U-u,axis=1)));side=1 if v['pieces'][j]['mask']&(1<<i) else -1
   points=[p.h*u+math.sin(p.alpha)*(math.cos(t)*e+math.sin(t)*b) for t in [a,z,(a+z)/2]]
   features.append((u,side,np.array(points),z-a))
  arc_features.append(features)
 cache={}
 def geometry(Rs):
  keys=[]
  for j,R in enumerate(Rs):
   ck=(j,*np.round(R.flatten(),8))
   if ck in cache:keys.append(cache[ck]);continue
   features=[]
   for u,side,points,span in arc_features[j]:
    n=R@u
    if v['angle']==90:n*=side;side=1
    base=tuple(np.rint(n*1e6).astype(np.int64))+(side,)
    if span>2*np.pi-1e-7:features.append(base+(6283185,));continue
    a,b,mid=np.rint((points@R.T)*1e6).astype(np.int64);ends=sorted([tuple(a),tuple(b)])
    features.append(base+ends[0]+ends[1]+tuple(mid)+(int(round(span*1e6)),))
   key=hashlib.sha256(repr(sorted(features)).encode()).digest();cache[ck]=key;keys.append(key)
  return tuple(sorted(keys)),keys
 def turn(Rs,i,a,legal):
  out=Rs.copy();out[legal[i]]=rot(p.axes[i],a)@Rs[legal[i]];return out
 def verify_loop(path,perm):
  Rs=initial.copy()
  for axis,degrees in path:
   i=axis-1;legal=dict(p.legal(Rs))
   if i not in legal:return False
   Rs=turn(Rs,i,math.radians(degrees),legal)
  return all(p.locate(R@p.seeds[j])==perm[j] and p.fits(j,R,perm[j]) and p.fits(perm[j],R.T,j) for j,R in enumerate(Rs))
 key,keys=geometry(initial);nodes={key:(keys,[])};queue=collections.deque([(initial,[])]);done=False;processed=0
 while queue and len(nodes)<maxstates:
  Rs,path=queue.popleft();processed+=1
  for i,inside in p.legal(Rs):
   if path and path[-1][0]==i+1:continue
   for angle in p.candidates(Rs,i,inside):
    newRs=turn(Rs,i,angle,{i:inside});newpath=path+[[i+1,math.degrees(angle)]];key,newkeys=geometry(newRs)
    if key not in nodes:
     nodes[key]=(newkeys,newpath);queue.append((newRs,newpath));continue
    oldkeys,oldpath=nodes[key];lookup={k:j for j,k in enumerate(oldkeys)};perm=[lookup[k] for k in newkeys]
    current=groups(p.N,edges)
    if all(any(j in g and k in g for g in current) for j,k in enumerate(perm)):continue
    looppath=newpath+[[axis,-a] for axis,a in reversed(oldpath)]
    assert verify_loop(looppath,perm),(f['key'],v['angle'],'geometric collision failed',looppath)
    edges.append(dict(permutation=perm));loops.append(dict(path=looppath,permutation=perm))
    print('LOOP',f['key'],round(v['angle'],6),'length',len(looppath),'states',len(nodes),'classes',[len(g) for g in groups(p.N,edges)],flush=True)
    if groups(p.N,edges)==v['geometricUpperBound']:done=True;break
   if done:break
  if done:break
  if processed%100==0:print('PROGRESS',f['key'],round(v['angle'],6),processed,'processed',len(nodes),'states',len(queue),'queued',flush=True)
 transient=[]
 if not queue and not done:
  current=groups(p.N,edges)
  for _,path in nodes.values():
   Rs=initial.copy()
   for axis,degrees in path:Rs=turn(Rs,axis-1,math.radians(degrees),dict(p.legal(Rs)))
   for j,R in enumerate(Rs):
    k=p.locate(R@p.seeds[j])
    if k<0 or any(j in g and k in g for g in current):continue
    if p.fits(j,R,k) and p.fits(k,R.T,j):transient.append(dict(piece=j,target=k,path=path))
  if transient:print('TRANSIENT',f['key'],v['angle'],len(transient),flush=True)
 complete=done or (not queue and not transient)
 v['orbits']=groups(p.N,edges);v['restoringLoops']=loops;v['switchDiagramStates']=len(nodes);v['switchGraphExhausted']=not queue and not done;v['transientWitnesses']=transient
 if complete:v['orbitStatus']='complete'
 print('RESULT',f['key'],round(v['angle'],6),v['orbitStatus'],len(nodes),'states',processed,'processed',round(time.time()-start,2),'sec',flush=True)

if __name__=='__main__':
 A=json.loads(Path('work/searched_atlas.json' if '--resume' in sys.argv else 'work/restored_atlas.json').read_text())
 for f in A['families']:
  for v in f['variants']:
   if v.get('orbitStatus')!='regular-only':continue
   selected=[arg for arg in sys.argv[1:] if not arg.startswith('--')]
   if selected and f['key']!=selected[0]:continue
   explore(f,v,A)
   Path('work/searched_atlas.json').write_text(json.dumps(A,separators=(',',':')))
 Path('work/searched_atlas.json').write_text(json.dumps(A,separators=(',',':')))
