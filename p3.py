from common import *

def spiral(shape,nbands=16,twist=0.1):
    r,a=meshgrid_polar(shape)
    return np.sin(np.log(1+r)*twist+a*nbands)>0

imgsz=(2048,2048)
s1,s2=(spiral(imgsz,16,16*i) for i in (1,-1))
im=s1^s2
imshow(im)
imsave(im,'p3.png')
