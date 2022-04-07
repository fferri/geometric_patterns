from common import *

def radial_warp(t):
    def f(i,j):
        cx,cy=imgsz/2
        a,r=np.arctan2(i-cy,j-cx),norm.L2(i-cy,j-cx)
        r+=(1+np.cos(0.1*t+r*math.pi*8/imgsz[0]))*imgsz[0]/(1+10*np.log(1+r))
        a+=r*t/imgsz[0]/1000
        return cx+np.cos(a)*r,cy+np.sin(a)*r
    return f

imgsz=np.array([2*1024]*2)
im=checkerboard(imgsz, imgsz//16)

def draw(t=0, **kwargs):
    return imwarp(im,radial_warp(t),cycle)

if __name__ == '__main__':
    for t in range(4000):
        print('rendering frame %08d...'%t)
        im1=draw(t)
        imsave(im1,'video3-%08d.png'%t)
