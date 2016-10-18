from common import *

def radial_warp(i,j):
    cx,cy=imgsz/2
    a,r=np.arctan2(i-cy,j-cx),np.sqrt((i-cy)**2+(j-cx)**2)
    a=a*6/4
    r=r*np.sin(1000/(1+r))
    return cx+np.cos(a)*r,cy+np.sin(a)*r

s=256
im=checkerboard(s,s//2)
for i in range(6):
    s//=2
    c=checkerboard(s,s//2)
    ch=imtile(c,(c.shape[0],im.shape[1]))
    cv=imtile(c,(im.shape[0]+2*c.shape[0],c.shape[1]))
    im=np.hstack((cv,np.vstack((ch,im,ch)),cv))
imgsz=np.uint(im.shape)
im=imwarp(im,radial_warp,cycle)
imshow(im)
imsave(im,'p10.png')
