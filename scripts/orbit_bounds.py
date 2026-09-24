import sys,itertools,json,math
from pathlib import Path
import numpy as np
from piece_orbits import Puzzle,groups,rot

def congruences(p,j,k):
 if abs(p.v['pieces'][j]['area']-p.v['pieces'][k]['area'])>3e-4:return []
 def normals(i):
  out=[]
  for u,*_ in p.boundaries()[i]:
   if not any(np.linalg.norm(u-v)<1e-6 for v in out):out.append(u)
  return out
 A=normals(j);B=normals(k)
 if len(A)!=len(B):return []
 if p.v['angle']==90:B=B+[-u for u in B]
 if len(A)==1:
  a=A[0];b=B[0];c=np.cross(a,b)
  R=rot(c/np.linalg.norm(c),math.acos(np.clip(a@b,-1,1))) if np.linalg.norm(c)>1e-8 else (np.eye(3) if a@b>0 else rot(np.cross(a,[1,0,0] if abs(a[0])<.9 else [0,1,0]),np.pi))
  return [R] if p.fits(j,R,k) and p.locate(R@p.seeds[j])==k else []
 a=A[0];b=next((x for x in A[1:] if abs(a@x)<1-1e-7),None)
 if b is None:return []
 def frame(a,b):
  t=b-(a@b)*a;t/=np.linalg.norm(t);return np.column_stack((a,t,np.cross(a,t)))
 F=frame(a,b);out=[]
 for u,v in itertools.permutations(B,2):
  if abs(u@v-a@b)>1e-6:continue
  R=frame(u,v)@F.T
  if p.locate(R@p.seeds[j])==k and p.fits(j,R,k) and p.fits(k,R.T,j):out.append(R)
 return out

def bounds(p):
 anchored=set()
 for u in p.axes:
  ds=p.axes@u
  if all(d<p.h-1e-7 for d in ds if d<1-1e-7):
   j=p.locate(u)
   if j>=0:anchored.add(j)
 for j,x in enumerate(p.v['pieces']):
  if not x['members']:anchored.add(j)
 pairs=[]
 for j in range(p.N):
  for k in range(j):
   if j in anchored or k in anchored:continue
   if congruences(p,j,k):pairs.append((j,k))
 perms=[]
 for j,k in pairs:
  perm=list(range(p.N));perm[j]=k;perm[k]=j;perms.append({'permutation':perm})
 return groups(p.N,perms),anchored

if __name__=='__main__':
 atlas=json.loads(Path('work/searched_atlas.json').read_text())
 for f in atlas['families']:
  if f['key']!='jumble':continue
  for v in f['variants']:
   if v['angle']==0:continue
   p=Puzzle(f,v,atlas)
   try:upper,anchors=bounds(p)
   except Exception as e:print('ERROR',f['key'],v['angle'],repr(e),flush=True);raise
   v['orbitUpperBound']=upper;v['anchoredPieces']=sorted(anchors)
   if upper!=v.get('orbits'):print('GAP',f['key'],v['angle'],'lower',v.get('orbits'),'upper',upper,'anchors',anchors,flush=True)
 Path('work/bounded_atlas.json').write_text(json.dumps(atlas,separators=(',',':')))
