from common import *

imgsz=np.array((512,512))
c=[imgsz*(0.5,d) for d in (0.25,0.75)]
(r1,a1),(r2,a2)=(meshgrid_polar(imgsz,c[i]) for i in range(2))
cmap=colormap.rainbow()

def draw(t=0, **kwargs):
    k=0.03*t/250
    im=np.minimum(r1*np.sin(k*r2),r2*np.sin(k*r1))
    cmap=np.roll(cmap,-1,axis=0)
    im=apply_colormap(im,cmap)
    return im

if __name__ == '__main__':
    for t in range(2153):
        print('rendering frame %08d...'%t)
        im=draw(t)
        imsave(im,'video6-%08d.png'%t)
