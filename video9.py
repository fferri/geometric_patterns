from common import *

# floor tiles metamorphosis

imgsz=(2048,)*2
x,y=meshgrid_euclidean(imgsz)
c=lambda x: np.cos(math.pi*x)
f=8./imgsz[0]

def draw(t=0, nf=250, **kwargs):
    b=min(1.,max(0.,1.3*abs(math.fmod(2*t/125.,2)-1)))
    q=int(t>=nf*0.25 and t<=nf*0.75)
    im=(c(y*f)+b*c(x*f)>0)^(c(q+x*f)+b*c(y*f)>0)^q
    return im

if __name__ == '__main__':
    for t in range(nf):
        print('rendering frame %08d...'%t)
        im=draw(t)
        imsave(im,'video9-%08d.png'%t)
