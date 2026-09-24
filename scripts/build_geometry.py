import base64, gzip, json, math, time
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

def set_grid(width):
    global W,H,phi,theta,st,ct,X,Y,Z,index,ch,cv
    W,H=width,width//2
    phi=(np.arange(W)+.5)*(2*np.pi/W)-np.pi
    theta=(np.arange(H)+.5)*(np.pi/H)
    st=np.sin(theta)[:,None];ct=np.cos(theta)[:,None]
    X=np.broadcast_to(st*np.cos(phi)[None,:],(H,W)).copy()
    Y=np.broadcast_to(st*np.sin(phi)[None,:],(H,W)).copy()
    Z=np.broadcast_to(ct,(H,W)).copy()
    index=np.arange(W*H,dtype=np.int32).reshape(H,W)
    ch=ct*ct+st*st*np.cos(2*np.pi/W)
    cv=math.cos(np.pi/H)

set_grid(2048)

def unique_circles(U,alpha):
    if alpha==0:return []
    out=[]
    for u in U:
        if any(np.linalg.norm(u-v)<1e-7 or (alpha==90 and np.linalg.norm(u+v)<1e-7) for v in out):continue
        out.append(u)
    return out

def exact_regions(U,alpha):
    U=np.asarray(U,dtype=float);U=U/np.linalg.norm(U,axis=1)[:,None]
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

def boundary_seeds(U,alpha):
    """Probe both sides of every open circle arc, including subpixel cells."""
    h=math.cos(math.radians(alpha));s=math.sin(math.radians(alpha));circles=unique_circles(U,alpha);points=[]
    for u in circles:
        e=np.cross(u,[0,0,1] if abs(u[2])<.9 else [0,1,0]);e/=np.linalg.norm(e);b=np.cross(u,e);angles=[]
        for w in circles:
            if np.linalg.norm(w-u)<1e-7:continue
            A=w@e;B=w@b;t=h*(1-w@u)/s;length=math.hypot(A,B)
            if length<1e-10 or abs(t)>length+1e-8:continue
            ratio=t/length
            if abs(abs(ratio)-1)<1e-8:ratio=math.copysign(1,ratio)
            phi=math.atan2(B,A);delta=math.acos(np.clip(ratio,-1,1))
            for a in [(phi-delta)%(2*np.pi),(phi+delta)%(2*np.pi)]:
                if not any(abs((a-c+np.pi)%(2*np.pi)-np.pi)<1e-7 for c in angles):angles.append(a)
        angles.sort()
        if not angles:angles=[0.]
        for a,z in zip(angles,angles[1:]+[angles[0]+2*np.pi]):
            if z-a<1e-7:continue
            mid=(a+z)/2;p=h*u+s*(math.cos(mid)*e+math.sin(mid)*b);inside=u-h*p;inside/=np.linalg.norm(inside)
            clearance=min([abs(w@p-h) for w in circles if np.linalg.norm(w-u)>1e-7]+[1.])
            epsilon=min(.003,clearance/4)
            for direction in [-1,1]:
                q=p+direction*epsilon*inside;q/=np.linalg.norm(q);points.append(q)
    return points

def joined_components(U,h,probes,lab,labels,mask,margin,expected):
    """Join raster fragments by certified paths and supply unseen thin cells.

    Every true cell has a boundary-arc seed. Geodesic connections only join
    points of one cell. Equality with Euler's count certifies the partition.
    """
    points=list(probes);raster=[]
    for label in labels:
        rows,cols=np.where(lab==label);pick=np.argmax(margin[rows,cols]);r,c=rows[pick],cols[pick]
        raster.append((int(label),len(points)));points.append(np.array([X[r,c],Y[r,c],Z[r,c]]))
    points=np.array(points);masks=[sum(1<<i for i,d in enumerate(U@p) if d>h) for p in points]
    parent=list(range(len(points)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    bymask={}
    for i,m in enumerate(masks):bymask.setdefault(m,[]).append(i)
    for m,ids in bymask.items():
        for ii,j in enumerate(ids):
            for k in ids[:ii]:
                if find(j)==find(k):continue
                p,q=points[j],points[k];c=np.clip(p@q,-1,1);theta=math.acos(c)
                if theta<1e-9:parent[find(j)]=find(k);continue
                if abs(math.sin(theta))<1e-10:continue
                tangent=(q-c*p)/math.sin(theta);aa=U@p;bb=U@tangent;end=U@q
                lo=np.minimum(aa,end);hi=np.maximum(aa,end);phase=np.arctan2(bb,aa)%(2*np.pi);magnitude=np.hypot(aa,bb)
                hi=np.where(phase<=theta,np.maximum(hi,magnitude),hi);phase=(phase+np.pi)%(2*np.pi)
                lo=np.where(phase<=theta,np.minimum(lo,-magnitude),lo)
                # Touching a boundary is insufficient: two different open
                # pieces can meet at a tangent point without being joined.
                if all(lo[i]>h+1e-12 if m&(1<<i) else hi[i]<h-1e-12 for i in range(len(U))):parent[find(j)]=find(k)
    groups={}
    for i in range(len(points)):groups.setdefault(find(i),[]).append(i)
    if len(groups)!=expected:
        print('  Boundary-seed path components:',len(groups),'expected',expected,flush=True);return None
    fullaxes=list(U)
    if abs(h)<1e-12:
        for u in U:
            if not any(np.linalg.norm(-u-v)<1e-7 for v in fullaxes):fullaxes.append(-u)
    out=np.zeros((H,W),np.uint8 if expected<256 else '<u2');records=[];rastermap={node:label for label,node in raster}
    for j,ids in enumerate(groups.values()):
        seed=max((points[i] for i in ids),key=lambda p:np.min(np.abs(U@p-h)));area=0.
        for i in ids:
            if i in rastermap:
                where=lab==rastermap[i];rows,cols=np.where(where);area+=float(np.sum(st[rows,0]))/(W*float(np.sum(st)));out[where]=j+1
        records.append(dict(mask=masks[ids[0]],seed=seed.round(10).tolist(),area=round(area,9),members=[i+1 for i,u in enumerate(fullaxes) if u@seed>h+1e-10]))
    print('  Certified',expected,'components using boundary seeds and uncut paths',flush=True)
    return out,records,len(fullaxes)

def atlas(U,alpha,expected):
    h=math.cos(math.radians(alpha));dots=[];mask=np.zeros((H,W),np.uint32);boundary=np.zeros((H,W),bool)
    margin=np.full((H,W),10.)
    if alpha==0:
        out=np.ones((H,W),np.uint8)
        return out,[dict(mask=0,seed=[0,0,1],area=1,members=[])],len(U)
    horizontal=np.ones((H,W),bool);vertical=np.ones((H-1,W),bool)
    for i,u in enumerate(U):
        d=u[0]*X+u[1]*Y+u[2]*Z
        mask|=((d>h).astype(np.uint32)<<i)
        boundary|=np.abs(d-h)<1e-11
        margin=np.minimum(margin,np.abs(np.arccos(np.clip(d,-1,1))-math.radians(alpha)))
        horizontal&=~connectivity_block(d,np.roll(d,-1,axis=1),ch,h)
        vertical&=~connectivity_block(d[:-1],d[1:],cv,h)
    probes=boundary_seeds(U,alpha);analytic={}
    for p in probes:
        m=sum(1<<i for i,d in enumerate(U@p) if d>h)
        clearance=float(np.min(np.abs(U@p-h)))
        if m not in analytic or clearance>analytic[m][1]:analytic[m]=(p,clearance)
    # Every region meets an open cut arc. If its signature count equals the
    # analytic region count, each signature is exactly one connected piece.
    if len(analytic)==expected:
        fullaxes=list(U)
        if alpha==90:
            for u in U:
                if not any(np.linalg.norm(-u-v)<1e-7 for v in fullaxes):fullaxes.append(-u)
        out=np.zeros((H,W),np.uint8 if expected<256 else '<u2');records=[]
        for j,(m,(seed,_)) in enumerate(sorted(analytic.items())):
            where=mask==m;rows,cols=np.where(where)
            if len(rows):
                pick=np.argmax(margin[rows,cols]);r,c=rows[pick],cols[pick]
                sampled=np.array([X[r,c],Y[r,c],Z[r,c]])
                if np.min(np.abs(U@sampled-h))>np.min(np.abs(U@seed-h)):seed=sampled
            area=float(np.sum(st[rows,0]))/(W*float(np.sum(st)))
            records.append(dict(mask=int(m),seed=seed.round(10).tolist(),area=round(area,9),members=[i+1 for i,u in enumerate(fullaxes) if u@seed>h+1e-10]))
            out[where]=j+1
        return out,records,len(fullaxes)
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
        joined=joined_components(U,h,probes,lab,labels,mask,margin,expected)
        if joined is not None:return joined
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
    records=[];out=np.zeros((H,W),np.uint8 if expected<256 else '<u2')
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

def main():
    names={'one':'Single ray','opposite':'Antipodal pair','ring3':'Triangular ring','ring4':'Square ring','tetra':'Tetrahedral axes','ring5':'Pentagonal ring','bipyramid3':'Triangle + poles','ring6':'Hexagonal ring','bipyramid4':'Octahedral axes','ring7':'Heptagonal ring','bipyramid5':'Pentagon + poles','jumble':'Jumbling example (60° apart)'}
    raw={x['name']:x for x in json.load(open('data/configurations.json'))}
    raw['jumble']=dict(axes=[[1,0,0],[.5,math.sqrt(3)/2,0],[.5,1/(2*math.sqrt(3)),math.sqrt(2/3)]],angles=[30,math.degrees(math.acos(math.sqrt(2/3)))],spherical_regions=[4,8,8])
    result=dict(width=W,height=H,families=[])
    cache={}
    for cache_path in [Path('assets/atlas.json'),Path('work/sphere_atlas.json'),Path('work/sphere_atlas.partial.json')]:
        if cache_path.exists():
            for f in json.loads(cache_path.read_text())['families']:
                for v in f['variants']:cache[(f['key'],v['kind'],round(v['angle'],7))]=(f['axes'],v)
    start=time.time();total=0
    for key,f in raw.items():
        name=f.get('title',names.get(key,key))
        f=raw[key];U=np.array(f['axes']);thresholds=[0]+f['angles']+[90]
        family=dict(key=key,name=name,axes=U.round(10).tolist(),variants=[],symmetry=f.get('symmetry'),construction=f.get('construction'),scope=f.get('scope','local' if key=='jumble' else 'global'))
        definitions=[]
        for i,(lo,hi) in enumerate(zip(thresholds,thresholds[1:])):
            definitions.append(dict(kind='regime',angle=(lo+hi)/2,low=lo,high=hi,expected=f['spherical_regions'][i],regime=i+1))
        for a in f['angles']:definitions.append(dict(kind='transition',angle=a,expected=exact_regions(U,a)))
        definitions += [dict(kind='central',angle=90,expected=exact_regions(U,90)),dict(kind='zero',angle=0,expected=1)]
        for info in definitions:
            a=info['angle'];expected=info.pop('expected')
            assert exact_regions(U,a)==expected,(key,a,expected,exact_regions(U,a))
            cached=cache.get((key,info['kind'],round(a,7)))
            if cached and np.max(np.abs(np.array(cached[0])-U))<1e-8 and cached[1]['count']==expected:
                info.update({k:cached[1][k] for k in ['count','pieces','rays','data','width','height','labelBytes'] if k in cached[1]});size=len(base64.b64decode(info['data']))
            else:
                if W!=2048:set_grid(2048)
                try:pixels,pieces,rays=atlas(U,a,expected)
                except RuntimeError as first:
                    print('  Refining the sphere grid:',first,flush=True);set_grid(4096)
                    pixels,pieces,rays=atlas(U,a,expected)
                info.update(width=W,height=H,labelBytes=pixels.dtype.itemsize)
                compressed=gzip.compress(pixels.tobytes(),compresslevel=9,mtime=0);size=len(compressed)
                info.update(count=len(pieces),pieces=pieces,rays=rays,data=base64.b64encode(compressed).decode())
            family['variants'].append(info);total+=1
            Path('work/sphere_atlas.partial.json').write_text(json.dumps(dict(width=2048,height=1024,families=result['families']+[family]),separators=(',',':')))
            print(f'{total:02d} {key:12s} {info["kind"]:10s} {a:9.5f}° {info["count"]:2d} pieces {size:6d} bytes {time.time()-start:.1f}s',flush=True)
        result['families'].append(family)
        Path('work/sphere_atlas.partial.json').write_text(json.dumps(result,separators=(',',':')))
    Path('work/sphere_atlas.json').write_text(json.dumps(result,separators=(',',':')))
    print('TOTAL',total,'SIZE',Path('work/sphere_atlas.json').stat().st_size,flush=True)

if __name__=='__main__':main()
