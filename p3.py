from common import *

def spiral(shape,nbands=16,twist=0.1):
    h,w=shape
    x,y=np.meshgrid(range(w),range(h))
    r=np.sqrt((x-w/2)**2+(y-h/2)**2)
    a=np.arctan2(x-w/2,y-h/2)
    return np.sin(np.log(1+r)*twist+a*nbands)>0

imgsz=(2048,2048)
s1,s2=(spiral(imgsz,16,16*i) for i in (1,-1))
im=s1^s2
imshow(im)
imsave(im,'p3.png')
