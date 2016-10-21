from common import *

imgsz=np.array([2*1024]*2)
r,a=meshgrid_polar(imgsz,dist=distance.L2)
a2=a
a+=0.001*r
a2+=0.001*r
r=np.uint(5*np.log(1+r))%2
a=np.uint(np.floor(a*16/math.pi/2))%2
a2=np.uint(np.floor(a2*3*16/math.pi/2))%2
im=r*a|(1-r)*a2
imshow(im)
imsave(im,'p15.png')
