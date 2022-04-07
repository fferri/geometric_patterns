from common import *

# inspired by a Aldous Huxley's book cover

def draw(**kwargs):
    imgsz=(2048,)*2
    r,a=meshgrid_polar(imgsz)
    im=np.fmod(np.float32(3.5*np.log(1+r))+2*np.power(np.abs(np.sin(8*np.float32(a))),0.4),1.4)
    im=apply_colormap(im,colormap.rainbow)
    def warp(o):
        def f(i,j):
            cy,cx=imgsz[0]//2,imgsz[1]//2
            y,x=i-cy,j-cx
            r,a=np.sqrt(x**2+y**2),np.arctan2(y,x)
            return cy+r*np.sin(a+o),cx+r*np.cos(a+o)
        return f
    im[:,:,0]=imwarp(im[:,:,0],warp(-0.02),cycle)
    im[:,:,2]=imwarp(im[:,:,2],warp(0.03),cycle)
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p18.png')
