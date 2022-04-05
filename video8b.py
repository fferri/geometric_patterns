from common import *

imgsz=(2048,)*2
r,a=meshgrid_polar(imgsz)

def draw(t=0, *args):
    discs=np.uint8(np.log(1+r)*4%2)
    bands=np.uint8(np.sin(a*16+0.1*t-np.log(1+r)*t)>0)
    im2=np.float32(discs^bands)
    # fast box blur:
    n=1+2*int(t*5)
    for axis in range(2):
        im2=sum(np.roll(im2,i,axis) for i in range(-n//2,(n+1)//2))
    im2/=n*n
    im3=imnormalize(im2)-(0.25+r/imgsz[0])*255
    im3=apply_colormap(im3,colormap.hot)
    return im3

if __name__ == '__main__':
    for t in range(1000):
        print('rendering frame %08d...'%t)
        im3=draw(0.05*t)
        imsave(im3,'video8b-%08d.png'%frame)
