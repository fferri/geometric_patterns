from common import *

imgsz=(1280,800)
r,a=meshgrid_polar(imgsz)

def draw(t=0, *args):
    h=t*math.pi*2/100
    im=3*(3*np.log(1+r))+5*np.sin(a*8+16*np.log(1+r))
    im=apply_colormap(im,colormap.rainbow2(h))
    return im

if __name__ == '__main__':
    for t in range(100):
        print('rendering frame %08d...'%t)
        im=draw(t)
        imsave(im,'video7-%08d.png'%t)
