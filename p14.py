from common import *

imgsz=np.array([2*1024]*2)
r,a=meshgrid_polar(imgsz,dist=distance.L2)
r=np.uint(7*np.log(1+r))
im=np.zeros(imgsz,dtype=np.uint8)
for i in range(8,17):
    c,d,k=i*3,(i+1)*3,2**(i-6)
    im|=(np.uint(np.floor(a*k/math.pi/2))%2)*(r>=c)*(r<d)
imshow(im)
imsave(im,'p14.png')
