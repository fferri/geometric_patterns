from common import *
from functools import reduce

for t in range(10000):
    print('rendering frame %08d...'%t)
    s=np.array((2048,2048))
    y,x=meshgrid_euclidean(s)
    pts=[]
    for (r,n,o) in ((0,1,0),(0.2+0.12*math.sin(t*0.03),3,0.001*t+math.pi/6),(0.4+0.3*math.sin(0.34+0.0174*t),6,math.sin(0.4+0.0042*t)*math.pi)):
        for a in range(n):
            pts.append([getattr(math,f)(o+a*math.pi*2/n)*r+0.5 for f in ['cos','sin']])
    r=[np.sqrt((x-p[1]*s[1])**2+(y-p[0]*s[0])**2) for p in pts]
    r=reduce(np.minimum, r[1:], r[0])
    im=np.sin(r*math.pi/(40+10*math.sin(0.43586+0.006342*t)))>0
    imsave(im,'video2-%08d.png'%t)
