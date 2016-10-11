from common import *

# 2-sides checkerboard

def radial_warp(i,j):
    cx,cy=imgsz/2
    a,r=math.atan2(i-cy,j-cx),math.hypot(i-cy,j-cx)
    r=r*(1+0.1*math.sin(0.008*r))
    a=a*6/4
    return cx+math.cos(a)*r,cy+math.sin(a)*r

imgsz=np.array([2*1024]*2)
im=checkerboard(imgsz, imgsz//16)^imtile(boxN(imgsz//16,4),imgsz)
im=imwarp(im,radial_warp,cycle)
imshow(im)
imsave(im,'p9.png')
