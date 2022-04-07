from common import *

def draw(**kwargs):
    imgsz=(2048,)*2
    r,a=meshgrid_polar(imgsz)
    im=np.float32(np.uint8(np.log(1+r)*4%2)^np.uint8(np.sin(a*16)>0))

    # fast box blur:
    for n in (65,):
        for axis in range(2):
            im=sum(np.roll(im,i,axis) for i in range(-n//2,(n+1)//2))

    im=imnormalize(im)>(0.25+r/imgsz[0])*255
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p24.png')
