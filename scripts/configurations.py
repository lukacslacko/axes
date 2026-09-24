"""Enumerate rotation-pole unions, without using a catalogue of puzzles."""
import argparse,itertools,json,math
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull

def normalize(points):
 a=np.array(points,dtype=float);a/=np.linalg.norm(a,axis=1)[:,None];return a

def unique(points):
 result=[]
 for p in normalize(points):
  if not any(np.linalg.norm(p-q)<1e-8 for q in result):result.append(p)
 return np.array(result)

def ring(n):return np.array([[math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n),0] for j in range(n)])

def critical(U):
 values=[]
 for k in [2,3]:
  for ids in itertools.combinations(range(len(U)),k):
   a=U[list(ids)];x,*_=np.linalg.lstsq(a,np.ones(k),rcond=None)
   if np.linalg.norm(a@x-1)>1e-8:continue
   h=1/np.linalg.norm(x)
   if 1e-8<h<1-1e-8:values.append(h)
 values.sort(reverse=True);out=[]
 for h in values:
  if not out or abs(h-out[-1])>1e-8:out.append(h)
 return [math.degrees(math.acos(h)) for h in out]

def count_generic(U,alpha):
 parent=list(range(len(U)));pairs=0;h=math.cos(2*math.radians(alpha))
 def find(i):
  while parent[i]!=i:i=parent[i]
  return i
 for i,u in enumerate(U):
  for j in range(i):
   if u@U[j]>h+1e-10:parent[find(i)]=find(j);pairs+=1
 return 2*pairs+len({find(i) for i in parent})+1

def enumerate_configs(limit):
 if limit<7:raise ValueError('The original catalogue is retained; use a limit of at least 7.')
 old=json.loads(Path('data/configurations.json').read_text())
 result=[f for f in old if len(f['axes'])<=7]
 seen={f['name'] for f in result}
 def add(key,title,axes,group,description):
  if len(axes)>limit or key in seen:return
  axes=normalize(axes);angles=critical(axes);ends=[0]+angles+[90]
  result.append(dict(name=key,title=title,axes=axes.tolist(),angles=angles,
   spherical_regions=[count_generic(axes,(a+b)/2) for a,b in zip(ends,ends[1:])],symmetry=group,construction=description))
  seen.add(key)
 for n in range(8,limit+1):
  add(f'ring{n}',f'{n}-gon ring',ring(n),f'D{n}','A regular polygon on a great circle.')
  m=n-2
  add(f'bipyramid{m}',f'{m}-gon + poles',np.vstack([ring(m),[0,0,1],[0,0,-1]]),f'D{m}','A regular equatorial polygon and its two poles.')
 octa=normalize([[s if j==i else 0 for j in range(3)] for i in range(3) for s in [-1,1]])
 cube=normalize(list(itertools.product([-1,1],repeat=3)))
 tetra=normalize([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])
 edges=normalize([[0 if j==i else signs[[k for k in range(3) if k!=i].index(j)] for j in range(3)] for i in range(3) for signs in itertools.product([-1,1],repeat=2)])
 add('tetra_octa','Tetrahedron + octahedron',np.vstack([tetra,octa]),'T','The four-ray and six-ray pole orbits of the tetrahedral rotation group.')
 for key,title,points in [
  ('cube','Cube vertices',cube),('cubocta','Cube edge axes',edges),
  ('octa_cube','Cube vertices + face axes',np.vstack([octa,cube])),
  ('octa_edges','Cube face + edge axes',np.vstack([octa,edges])),
  ('cube_edges','Cube vertices + edge axes',np.vstack([cube,edges])),
  ('octa_all','All octahedral pole orbits',np.vstack([octa,cube,edges]))]:
  add(key,title,points,'O','A union of the 6-, 8-, and 12-ray pole orbits of the octahedral rotation group.')
 phi=(1+math.sqrt(5))/2
 ico=normalize([np.roll([0,a,b*phi],k) for k in range(3) for a,b in itertools.product([-1,1],repeat=2)])
 hull=ConvexHull(ico);dodeca=unique([ico[face].sum(axis=0) for face in hull.simplices])
 distance=min(np.linalg.norm(a-b) for i,a in enumerate(ico) for b in ico[:i])
 iedges=unique([a+b for i,a in enumerate(ico) for b in ico[:i] if abs(np.linalg.norm(a-b)-distance)<1e-7])
 assert [len(ico),len(dodeca),len(iedges)]==[12,20,30]
 orbits=[('ico','Icosahedral vertices',ico),('dodeca','Dodecahedral vertices',dodeca),('iedges','Icosahedral edge axes',iedges)]
 for bits in range(1,8):
  selected=[o for i,o in enumerate(orbits) if bits&(1<<i)];key='_'.join(o[0] for o in selected)
  title=selected[0][1] if len(selected)==1 else {3:'Icosahedral vertices + face axes',5:'Icosahedral vertices + edge axes',6:'Icosahedral face + edge axes',7:'All icosahedral pole orbits'}[bits]
  add(key,title,np.vstack([o[2] for o in selected]),'I','A union of the 12-, 20-, and 30-ray pole orbits of the icosahedral rotation group.')
 result.sort(key=lambda f:(len(f['axes']),0 if f['name'].startswith('ring') else 1 if f['name'].startswith('bipyramid') else 2,f['name']))
 return result

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--max-axes',type=int,default=12);args=parser.parse_args()
 configs=enumerate_configs(args.max_axes)
 Path('data/configurations.json').write_text(json.dumps(configs,indent=2)+'\n')
 for f in configs:print(len(f['axes']),f['name'],len(f['angles'])+1,'regimes',max(f['spherical_regions']),'pieces')
 print('TOTAL',len(configs),'configurations',sum(len(f['angles'])+1 for f in configs),'open regimes')
