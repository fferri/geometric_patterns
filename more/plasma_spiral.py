import math
import numpy as np
from PIL import Image
def ramp(values,positions,n):
    r=np.zeros((n,),dtype=np.uint8)
    for (vi,vj,pi,pj) in zip(values,values[1:],positions,positions[1:]):
        for h in range(pi,1+pj):
            a=(h-pi)/(pj-pi)
            r[h]=(1-a)*vi+a*vj
    return r
im=np.zeros((1024,1024,3),dtype=np.uint8)
cmap=np.zeros((1024,3),dtype=np.uint8)
cmap[...,0]=ramp([20,0,100,50],[0,700,900,1023],1024)
cmap[...,1]=ramp([100,0,100,0],[0,255,700,1023],1024)
cmap[...,2]=ramp([255,0,100,0,255],[0,500,950,1000,1023],1024)
print('im.shape:',im.shape)
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        y,x=i-im.shape[0]*0.5,j-im.shape[1]*0.5
        r,a=math.hypot(x,y),math.atan2(y,x)
        v=1023*0.5*(1.+math.sin((0.003*r)**2+4*a))+(8*a*1024/2/math.pi)
        while v<0: v+=1024
        while v>=1024: v-=1024
        for h in range(3):
            im[i,j,h]=cmap[int(v),h]

im=Image.fromarray(im)
#im.save('my.png')
im.show()
