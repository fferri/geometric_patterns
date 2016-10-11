from common import *

# 2-sides checkerboard

def radial_warp(i,j):
    cx,cy=imgsz/2
    a,r=math.atan2(i-cy,j-cx),math.hypot(i-cy,j-cx)
    a=a*2/4
    return cx+math.cos(a)*r,cy+math.sin(a)*r

imgsz=np.array([2*1024]*2)
im=checkerboard(imgsz, imgsz//16)
im=imwarp(im,radial_warp,cycle)
imshow(im)
imsave(im,'p7.png')
