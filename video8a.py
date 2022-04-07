from common import *

imgsz=(2048,)*2
r,a=meshgrid_polar(imgsz)
im=np.float32(np.uint8(np.log(1+r)*4%2)^np.uint8(np.sin(a*16)>0))

im2=im

def draw(t=0, **kwargs):
    # fast box blur:
    for n in (19,):
        for axis in range(2):
            im2=sum(np.roll(im2,i,axis) for i in range(-n//2,(n+1)//2))
        im2/=n*n
    im3=imnormalize(im2)>(0.25+r/imgsz[0])*255
    return im3

if __name__ == '__main__':
    for t in range(1000):
        print('rendering frame %08d...'%frame)
        im3=draw(t)
        imsave(im3,'video8a-%08d.png'%frame)
