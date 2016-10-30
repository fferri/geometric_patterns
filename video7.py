from common import *

imgsz=(1280,800)
r,a=meshgrid_polar(imgsz)
single=0
for t in range(1 if single else 100):
    print('rendering frame %08d...'%t)
    h=t*math.pi*2/100
    im=3*(3*np.log(1+r))+5*np.sin(a*8+16*np.log(1+r))
    im=apply_colormap(im,colormap.rainbow2(h))
    if single: imshow(im)
    else: imsave(im,'video7-%08d.png'%t)
