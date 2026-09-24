"""Check the two user-suggested polyhedral axis sets directly from coordinates."""
import itertools,json,math
from pathlib import Path
import numpy as np
from configurations import normalize,critical,count_generic
from piece_orbits import rot

def gyrobifastigium(beta=30):
 b=math.radians(beta);s=math.sin(b);c=math.cos(b)
 return np.array([[a/math.sqrt(2),d/math.sqrt(2),0] for a,d in itertools.product([-1,1],repeat=2)]+[[0,-s,c],[0,s,c],[-s,0,-c],[s,0,-c]])

def gyrobicupola():
 a=1+math.sqrt(2)
 vertices=np.array([[a*signs[i] if j==i else signs[j] for j in range(3)] for i in range(3) for signs in itertools.product([-1,1],repeat=3)])
 R=rot([0,0,1],math.pi/4)
 vertices=np.array([R@p if abs(p[2]-a)<1e-8 else p for p in vertices])
 return normalize(vertices)

def rotations(U,i,alpha):
 u=U[i];neighbors=[j for j,v in enumerate(U) if j!=i and -1+1e-8<u@v and u@v>math.cos(2*math.radians(alpha))+1e-8]
 found=[]
 for j,k in itertools.permutations(neighbors,2):
  a=U[j];b=U[k]
  if abs(u@a-u@b)>1e-8:continue
  aa=a-(u@a)*u;bb=b-(u@b)*u
  phi=math.atan2(u@np.cross(aa,bb),aa@bb)
  if abs(phi)<1e-8:continue
  R=rot(u,phi)
  preserved=[m for m in neighbors if any(np.linalg.norm(R@U[n]-U[m])<1e-7 for n in neighbors)]
  blocked=[m for m in neighbors if m not in preserved]
  assert np.linalg.norm(R@U[j]-U[k])<1e-7
  found.append(dict(axis=i+1,source=j+1,target=k+1,angle=math.degrees(phi),opens=[m+1 for m in preserved],blocks=[m+1 for m in blocked],regular=not blocked))
 return sorted(found,key=lambda x:(abs(x['angle']),x['target']))

if __name__=='__main__':
 results=[]
 for key,title,U,alpha in [('gyrobifastigium','Gyrobifastigium',gyrobifastigium(),40),('gyrobicupola','Elongated square gyrobicupola',gyrobicupola(),25)]:
  events=critical(U);witnesses=[];regular=[]
  for i in range(len(U)):
   candidates=rotations(U,i,alpha);assert candidates,(key,i)
   ordinary=[x for x in candidates if x['regular']]
   if ordinary:regular.append(i+1)
   witnesses.append((ordinary or candidates)[0])
  result=dict(key=key,name=title,axes=U.tolist(),angle=alpha,criticalAngles=events,regularAxes=regular,witnesses=witnesses)
  results.append(result)
  print(title,len(U),'axes; regular axes:',regular,'all axes support interacting switches')
  print('witness',next(w for w in witnesses if w['blocks']))
 # The gyrobifastigium's ridge switch survives a continuous change of tilt.
 samples=[]
 for beta in [20,25,30,35,40]:
  U=gyrobifastigium(beta);u=U[5];a=U[3];b=U[1]
  d=u@a;phi=math.acos(-math.sin(math.radians(beta))**2/(2-math.sin(math.radians(beta))**2))
  assert np.linalg.norm(rot(u,phi)@a-b)<1e-7
  samples.append(dict(beta=beta,turn=math.degrees(phi),overlapAbove=math.degrees(math.acos(d))/2))
 results[0]['deformationSamples']=samples
 Path('data/local-examples.json').write_text(json.dumps(results,indent=2)+'\n')
