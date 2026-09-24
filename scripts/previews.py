"""Generate mathematical sphere previews; offscreen cards need no GPU buffers."""
import base64,colorsys,gzip,hashlib,json,math
from pathlib import Path
import numpy as np
from PIL import Image
from piece_orbits import rot

A=json.loads(Path('assets/atlas.json').read_text());W=A['width'];H=A['height']
dest=Path('assets/previews');dest.mkdir(exist_ok=True)
manifest_path=Path('work/preview-hashes.json')
manifest=json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
width,height=440,360;r=min(width,height)*.423
yy,xx=np.mgrid[:height,:width];x=(xx+.5-width/2)/r;y=(height/2-yy-.5)/r;r2=x*x+y*y
inside=r2<=1;local=np.stack([x,y,np.sqrt(np.maximum(0,1-r2))],axis=-1)
R=rot([1,0,0],-.55)@rot([0,1,0],.68);world=local@R;world[~inside]=[0,0,1]
tx=(np.floor((np.arctan2(world[:,:,1],world[:,:,0])/(2*np.pi)+.5)*W).astype(int))%W
ty=np.minimum(H-1,np.floor(np.arccos(np.clip(world[:,:,2],-1,1))/np.pi*H).astype(int))
light=np.array([-.45,.65,1.1]);light/=np.linalg.norm(light);half=light+[0,0,1];half/=np.linalg.norm(half)
shade=.6+.36*np.maximum(0,local@light);shine=.13*np.maximum(0,local@half)**36
palette=np.array([colorsys.hls_to_rgb(((211+i*137.507764)%360)/360,.58+(((i*3)%5)-2)*.04,.61+(i%4)*.055) for i in range(2048)])
def smooth(x):x=np.clip(x,0,1);return x*x*(3-2*x)
built=0
for f in A['families']:
 for vi,v in enumerate(f['variants']):
  key=f'{f["key"]}-{vi}';filename=dest/(key+'.png')
  digest=hashlib.sha256(json.dumps(['nearest-seed-v2',f['axes'],v['angle'],v['data'],v['orbits']],separators=(',',':')).encode()).hexdigest()
  if filename.exists() and manifest.get(key)==digest:continue
  W=v.get('width',A['width']);H=v.get('height',A['height'])
  tx=(np.floor((np.arctan2(world[:,:,1],world[:,:,0])/(2*np.pi)+.5)*W).astype(int))%W
  ty=np.minimum(H-1,np.floor(np.arccos(np.clip(world[:,:,2],-1,1))/np.pi*H).astype(int))
  pixels=np.frombuffer(gzip.decompress(base64.b64decode(v['data'])),np.uint8 if v.get('labelBytes',1)==1 else '<u2').reshape(H,W)
  masks=np.array([-1]+[p['mask'] for p in v['pieces']]);signature=np.zeros((height,width),np.int32);edge=np.ones((height,width))
  h=math.cos(math.radians(v['angle']))
  for i,u in enumerate(f['axes']):
   d=world@np.array(u)-h;signature|=(d>0).astype(np.int32)<<i
   if v['angle']>0:
    gy,gx=np.gradient(d);edge=np.minimum(edge,smooth(np.abs(d)/np.maximum((np.abs(gx)+np.abs(gy))*1.05,.00006)))
  ids=pixels[ty,tx].copy();bad=(ids==0)|(masks[ids]!=signature)
  seeds=np.array([p['seed'] for p in v['pieces']])
  for m in np.unique(signature[bad]):
   candidates=np.flatnonzero(masks[1:]==m)+1;where=bad&(signature==m)
   if len(candidates):ids[where]=candidates[np.argmax(world[where]@seeds[candidates-1].T,axis=1)]
  classes=np.zeros(v['count']+1,np.int32)
  for i,g in enumerate(v['orbits']):classes[np.array(g)+1]=i
  color=palette[classes[ids]]*shade[:,:,None]+shine[:,:,None]
  color=color*edge[:,:,None]+np.array([.09,.14,.23])*(1-edge[:,:,None])
  rgba=np.empty((height,width,4),np.uint8);rgba[:,:,:3]=np.clip(np.round(color*255),0,255)
  rgba[:,:,3]=np.where(inside,np.round(255*smooth((1-np.sqrt(r2))*r/1.4)),0).astype(np.uint8)
  Image.fromarray(rgba).save(filename,optimize=True);manifest[key]=digest;built+=1
manifest_path.write_text(json.dumps(manifest,indent=2))
print('Generated',built,'sphere previews.')
