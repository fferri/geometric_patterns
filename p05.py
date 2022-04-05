from common import *

# 8-sides checkerboard

def draw(*args):
    imgsz=np.array([2*1024]*2)
    def radial_warp(i,j):
        cx,cy=imgsz/2
        a,r=np.arctan2(i-cy,j-cx),np.sqrt((i-cy)**2+(j-cx)**2)
        a=np.fmod(2*a,math.pi*2)
        return cx+np.cos(a)*r,cy+np.sin(a)*r
    im=checkerboard(imgsz, imgsz//16)
    im=imwarp(im,radial_warp,cycle)
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p05.png')
