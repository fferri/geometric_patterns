from common import *

def spiral(shape,nbands=16,twist=0.1):
    im=np.zeros(shape,dtype=np.uint8)
    for i,j in all_coords(shape):
        y,x=(i-0.5*shape[0],j-0.5*shape[1])
        r=math.log(1+math.hypot(y,x))
        a=math.atan2(y,x)
        im[i,j]=1 if math.sin(a*nbands+r*twist)>0 else 0
    return im

imgsz=(2048,2048)
s1,s2=(spiral(imgsz,16,16*i) for i in (1,-1))
im=s1^s2
imshow(im)
imsave(im,'p3.png')
