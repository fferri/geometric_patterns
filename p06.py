from common import *

# 6-sides checkerboard

def draw(**kwargs):
    imgsz=np.array([2*1024]*2)
    def radial_warp(i,j):
        cx,cy=imgsz/2
        a,r=np.arctan2(i-cy,j-cx),np.sqrt((i-cy)**2+(j-cx)**2)
        a=a*6/4
        return cx+np.cos(a)*r,cy+np.sin(a)*r
    im=checkerboard(imgsz, imgsz//16)
    im=imwarp(im,radial_warp,cycle)
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p06.png')
