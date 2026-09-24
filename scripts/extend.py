"""Extend geometry and verified ordinary orbits; retain prior partial-turn proofs.

New partial-turn cases deliberately stop at verified groups instead of running
an exhaustive state search. Run from the repository root.
"""
import argparse,json,math,subprocess,sys,time
from pathlib import Path
import numpy as np
from configurations import enumerate_configs,critical,count_generic
from local_examples import gyrobifastigium,gyrobicupola,rotations
from piece_orbits import Puzzle,groups

parser=argparse.ArgumentParser()
parser.add_argument('--max-axes',type=int,default=24)
parser.add_argument('--skip-geometry',action='store_true')
args=parser.parse_args()
configs=enumerate_configs(args.max_axes)
U=gyrobifastigium();events=critical(U);ends=[0]+events+[90]
configs.append(dict(name='gyrobifastigium',title='Gyrobifastigium vertices',axes=U.tolist(),angles=events,
 spherical_regions=[count_generic(U,(a+b)/2) for a,b in zip(ends,ends[1:])],scope='local',
 construction='Vertex rays of two triangular prisms joined along a square, with perpendicular ridges.'))
if args.max_axes>=24:
 U=gyrobicupola();events=critical(U);ends=[0]+events+[90]
 configs.append(dict(name='gyrobicupola',title='Elongated square gyrobicupola vertices',axes=U.tolist(),angles=events,
  spherical_regions=[count_generic(U,(a+b)/2) for a,b in zip(ends,ends[1:])],scope='local',
  construction='Vertex rays of a rhombicuboctahedron with one square cupola turned by 45 degrees.'))
Path('data/configurations.json').write_text(json.dumps(configs,indent=2)+'\n')
Path('work').mkdir(exist_ok=True)
if not args.skip_geometry:
 subprocess.run([sys.executable,'scripts/build_geometry.py'],check=True)
A=json.loads(Path('work/sphere_atlas.json').read_text())
cache={}
for path in [Path('assets/atlas.json'),Path('work/expansion.partial.json')]:
 if path.exists():
  for f in json.loads(path.read_text())['families']:
   for v in f['variants']:
    if 'orbits' in v:cache[(f['key'],v['kind'],round(v['angle'],7))]=(f['axes'],v)
start=time.time()
for f in A['families']:
 for index,v in enumerate(f['variants']):
  old=cache.get((f['key'],v['kind'],round(v['angle'],7)))
  if old and np.max(np.abs(np.array(old[0])-np.array(f['axes'])))<1e-8 and old[1]['data']==v['data'] and old[1]['pieces']==v['pieces']:
   v.update(old[1]);continue
  if f['key']=='jumble':raise RuntimeError('Rebuild the original jumbling example before extending.')
  p=Puzzle(f,v,A);v['moves']=p.standard_moves();v['orbits']=groups(p.N,v['moves'])
  v['extraSwitches']=[]
  if v['angle']:
   for i in range(len(p.axes)):
    v['extraSwitches'].extend(m for m in rotations(p.axes,i,v['angle']) if not m['regular'])
  v['orbitStatus']='regular-only' if v['extraSwitches'] else 'complete'
  v['orbitMethod']='Verified diagram-preserving legal turns; further partial-turn mergers not searched' if v['extraSwitches'] else 'Orbits of diagram-preserving legal turns; no extra interacting switch angles'
  v['searchPolicy']='ordinary-generators'
  print(f['key'],index,round(v['angle'],6),p.N,'pieces',len(v['orbits']),'verified groups',v['orbitStatus'],round(time.time()-start,1),'s',flush=True)
  Path('work/expansion.partial.json').write_text(json.dumps(A,separators=(',',':')))
Path('work/jumble_atlas.json').write_text(json.dumps(A,separators=(',',':')))
print('Ready:',sum(len(f['variants']) for f in A['families']),'views',flush=True)
