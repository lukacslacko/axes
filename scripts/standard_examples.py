"""A symbolic-angle witness for partial turns of dodecahedral vertex rays."""
import json,math
from pathlib import Path
import numpy as np
from configurations import enumerate_configs
from local_examples import rotations
from piece_orbits import rot

f=next(f for f in enumerate_configs(20) if f['name']=='dodeca')
U=np.array(f['axes']);angle=math.degrees(math.acos((3*math.sqrt(5)-1)/8));witnesses=[]
for i,u in enumerate(U):
    move=next(m for m in rotations(U,i,60) if not m['regular'] and abs(abs(m['angle'])-angle)<1e-7)
    if u@U[move['source']-1]<0:
        for key in ['source','target']:move[key]=int(np.argmin(np.linalg.norm(U+U[move[key]-1],axis=1)))+1
    a=U[move['source']-1];b=U[move['target']-1]
    assert np.linalg.norm(rot(u,math.radians(move['angle']))@a-b)<1e-8
    assert abs(u@a-1/3)<1e-8 and abs(u@b-1/3)<1e-8
    assert abs(a@b-math.sqrt(5)/3)<1e-8
    assert len(move['opens'])==6 and len(move['blocks'])==9
    witnesses.append(move)
result=dict(key='dodeca',axes=U.tolist(),cutAngle=60,turnAngle=angle,
    cosine='(3*sqrt(5)-1)/8',overlapAbove=math.degrees(math.acos(1/3))/2,witnesses=witnesses)
Path('data/standard-examples.json').write_text(json.dumps(result,indent=2)+'\n')
print('Verified dodecahedral partial-turn witnesses on all 20 rays:',angle,'degrees')
