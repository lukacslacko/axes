import base64, gzip, json, math, time
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

W,H=2048,1024
phi=(np.arange(W)+.5)*(2*np.pi/W)-np.pi
theta=(np.arange(H)+.5)*(np.pi/H)
st=np.sin(theta)[:,None];ct=np.cos(theta)[:,None]
X=np.broadcast_to(st*np.cos(phi)[None,:],(H,W)).copy()
Y=np.broadcast_to(st*np.sin(phi)[None,:],(H,W)).copy()
Z=np.broadcast_to(ct,(H,W)).copy()
index=np.arange(W*H,dtype=np.int32).reshape(H,W)
ch=ct*ct+st*st*np.cos(2*np.pi/W)
cv=math.cos(np.pi/H)

def unique_circles(U,alpha):
    if alpha==0:return []
    out=[]
    for u in U:
        if any(np.linalg.norm(u-v)<1e-7 or (alpha==90 and np.linalg.norm(u+v)<1e-7) for v in out):continue
        out.append(u)
    return out

def exact_regions(U,alpha):
    A=unique_circles(U,alpha);h=math.cos(math.radians(alpha))
    if not A:return 1
    vertices=[];inc=[set() for _ in A];parent=list(range(len(A)))
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    for i,u in enumerate(A):
        for j,v in enumerate(A[:i]):
            d=float(u@v)
            if d<-1+1e-10:continue
            mid=h/(1+d)*(u+v);s=1-float(mid@mid)
            if s<-1e-9:continue
            parent[find(i)]=find(j)
            normal=np.cross(u,v);normal/=np.linalg.norm(normal)
            ps=[mid] if abs(s)<1e-9 else [mid+math.sqrt(s)*normal,mid-math.sqrt(s)*normal]
            for p in ps:
                found=next((k for k,q in enumerate(vertices) if np.linalg.norm(p-q)<1e-6),None)
                if found is None:found=len(vertices);vertices.append(p)
                inc[i].add(found);inc[j].add(found)
    isolated=sum(not s for s in inc)
    V=len(vertices)+isolated;E=sum(max(len(s),1) for s in inc)
    C=len({find(i) for i in range(len(A))})
    return E-V+C+1

def connectivity_block(ga,gb,c,h):
    # Exact maximum along the short great-circle arc between two samples.
    derivative=gb-c*ga
    inside=(derivative>1e-13)&(c*gb-ga<-1e-13)&(ga<h)&(gb<h)
    peak=np.sqrt(np.maximum(0,ga*ga+derivative*derivative/np.maximum(1-c*c,1e-20)))
    return inside&(peak>=h-1e-12)

def atlas(U,alpha,expected):
    h=math.cos(math.radians(alpha));dots=[];mask=np.zeros((H,W),np.uint8);boundary=np.zeros((H,W),bool)
    margin=np.full((H,W),10.)
    if alpha==0:
        out=np.ones((H,W),np.uint8)
        return out,[dict(mask=0,seed=[0,0,1],area=1,members=[])],len(U)
    horizontal=np.ones((H,W),bool);vertical=np.ones((H-1,W),bool)
    for i,u in enumerate(U):
        d=u[0]*X+u[1]*Y+u[2]*Z
        mask|=((d>h).astype(np.uint8)<<i)
        boundary|=np.abs(d-h)<1e-11
        margin=np.minimum(margin,np.abs(np.arccos(np.clip(d,-1,1))-math.radians(alpha)))
        horizontal&=~connectivity_block(d,np.roll(d,-1,axis=1),ch,h)
        vertical&=~connectivity_block(d[:-1],d[1:],cv,h)
    horizontal&=(mask==np.roll(mask,-1,axis=1))&~boundary&~np.roll(boundary,-1,axis=1)
    vertical&=(mask[:-1]==mask[1:])&~boundary[:-1]&~boundary[1:]
    starts=np.concatenate([index[horizontal],index[:-1][vertical]])
    ends=np.concatenate([np.roll(index,-1,axis=1)[horizontal],index[1:][vertical]])
    graph=coo_matrix((np.ones(len(starts),np.uint8),(starts,ends)),shape=(W*H,W*H)).tocsr()
    _,lab=connected_components(graph,directed=False,return_labels=True)
    del graph,starts,ends
    lab=lab.reshape(H,W)
    labels,counts=np.unique(lab[~boundary],return_counts=True)
    if len(labels)!=expected:
        # A circle-crossing tip narrower than a texel can be sampled as an
        # isolated pixel of an otherwise large piece. Such pixels are drawn
        # by the exact-mask fallback in the renderer, not counted as pieces.
        substantial=counts>8
        if int(np.sum(substantial))==expected:
            print('  quantized boundary fragments:',counts[~substantial].tolist(),flush=True)
            labels=labels[substantial]
        else:
            raise RuntimeError(f'alpha={alpha}: sampled {len(labels)} != exact {expected}; smallest sizes {sorted(counts)[:20]}')
    fullaxes=list(U)
    if alpha==90:
        for u in U:
            if not any(np.linalg.norm(-u-v)<1e-7 for v in fullaxes):fullaxes.append(-u)
    records=[];out=np.zeros((H,W),np.uint8)
    for j,label in enumerate(labels):
        where=lab==label
        where&=~boundary
        rows,cols=np.where(where)
        pick=np.argmax(margin[rows,cols]);r,c=rows[pick],cols[pick]
        seed=np.array([X[r,c],Y[r,c],Z[r,c]])
        area=float(np.sum(st[rows,0]))/(W*float(np.sum(st)))
        records.append(dict(mask=int(mask[r,c]),seed=seed.round(7).tolist(),area=round(area,7),members=[i+1 for i,u in enumerate(fullaxes) if u@seed>h+1e-8]))
        out[where]=j+1
    return out,records,len(fullaxes)

names={'one':'1 · Single ray','opposite':'2 · Antipodal pair','ring3':'3 · Triangular ring','ring4':'4 · Square ring','tetra':'4 · Tetrahedral axes','ring5':'5 · Pentagonal ring','bipyramid3':'5 · Triangle + poles','ring6':'6 · Hexagonal ring','bipyramid4':'6 · Octahedral axes','ring7':'7 · Heptagonal ring','bipyramid5':'7 · Pentagon + poles','jumble':'3 · Jumbling example (60° apart)'}
raw={x['name']:x for x in json.load(open('data/configurations.json'))}
raw['jumble']=dict(axes=[[1,0,0],[.5,math.sqrt(3)/2,0],[.5,1/(2*math.sqrt(3)),math.sqrt(2/3)]],angles=[30,math.degrees(math.acos(math.sqrt(2/3)))],spherical_regions=[4,8,8])
result=dict(width=W,height=H,families=[])
start=time.time();total=0
for key,name in names.items():
    f=raw[key];U=np.array(f['axes']);thresholds=[0]+f['angles']+[90]
    family=dict(key=key,name=name,axes=U.round(10).tolist(),variants=[])
    definitions=[]
    for i,(lo,hi) in enumerate(zip(thresholds,thresholds[1:])):
        definitions.append(dict(kind='regime',angle=(lo+hi)/2,low=lo,high=hi,expected=f['spherical_regions'][i],regime=i+1))
    for a in f['angles']:definitions.append(dict(kind='transition',angle=a,expected=exact_regions(U,a)))
    definitions += [dict(kind='central',angle=90,expected=exact_regions(U,90)),dict(kind='zero',angle=0,expected=1)]
    for info in definitions:
        a=info['angle'];expected=info.pop('expected')
        assert exact_regions(U,a)==expected,(key,a,expected,exact_regions(U,a))
        pixels,pieces,rays=atlas(U,a,expected)
        compressed=gzip.compress(pixels.tobytes(),compresslevel=9,mtime=0)
        info.update(count=len(pieces),pieces=pieces,rays=rays,data=base64.b64encode(compressed).decode())
        family['variants'].append(info);total+=1
        print(f'{total:02d} {key:12s} {info["kind"]:10s} {a:9.5f}° {len(pieces):2d} pieces {len(compressed):6d} bytes {time.time()-start:.1f}s',flush=True)
    result['families'].append(family)
    Path('work/sphere_atlas.partial.json').write_text(json.dumps(result,separators=(',',':')))
Path('work/sphere_atlas.json').write_text(json.dumps(result,separators=(',',':')))
print('TOTAL',total,'SIZE',Path('work/sphere_atlas.json').stat().st_size,flush=True)
