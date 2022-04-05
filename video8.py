from common import *

imgsz=(2048,)*2
r,a=meshgrid_polar(imgsz)
im=np.float32(np.uint8(np.log(1+r)*4%2)^np.uint8(np.sin(a*16)>0))

def draw(t=0, *args):
    im2=im
    # fast box blur:
    for n in (1+2*t,):
        for axis in range(2):
            im2=sum(np.roll(im2,i,axis) for i in range(-n//2,(n+1)//2))
    im2=imnormalize(im2)>(0.25+r/imgsz[0])*255
    return im2

if __name__ == '__main__':
    for t in range(1000):
        print('rendering frame %08d...'%t)
        im2=draw(t)
        imsave(im2,'video8-%08d.png'%t)
