from common import *
from time import time

def spiral(shape,nbands=16,twist=0.1):
    t=time()
    r,a=meshgrid_polar(shape)
    return np.sin(0.2*t+np.log(1+r)*twist+a*nbands)>0

def draw(**kwargs):
    imgsz=(1024,1024)
    s1,s2=(spiral(imgsz,16,16*i) for i in (1,-1))
    return s1^s2

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p03.png')
