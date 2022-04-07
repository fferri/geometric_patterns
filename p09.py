from common import *

# 2-sides checkerboard

def draw(**kwargs):
    imgsz=np.array([2*1024]*2)
    def radial_warp(i,j):
        cx,cy=imgsz/2
        a,r=np.arctan2(i-cy,j-cx),np.sqrt((i-cy)**2+(j-cx)**2)
        r=r*(1+0.1*np.sin(0.008*r))
        a=a*6/4
        return cx+np.cos(a)*r,cy+np.sin(a)*r
    im=checkerboard(imgsz, imgsz//16)^imtile(boxN(imgsz//8,4),imgsz)
    im2=checkerboard(imgsz, imgsz//16)^imtile(boxN(imgsz//16,4),imgsz)
    im[512:1536,512:1536]=im2[512:1536,512:1536]
    im=imwarp(im,radial_warp,cycle)
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p09.png')
