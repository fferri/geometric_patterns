from common import *

def radial_warp(t):
    def f(i,j):
        cx,cy=imgsz/2
        a,r=np.arctan2(i-cy,j-cx),np.sqrt((i-cy)**2+(j-cx)**2)
        r=r*(1+(0.1*math.sin(t*0.01)+0.1)*np.sin((0.008+math.sin(0.0007*t)*0.01)*r+t*0.005637))
        a=a*6/4
        return cx+np.cos(a)*r,cy+np.sin(a)*r
    return f

imgsz=np.array([2*1024]*2)
im=checkerboard(imgsz, imgsz//16)^imtile(boxN(imgsz//8,4),imgsz)
im2=checkerboard(imgsz, imgsz//16)^imtile(boxN(imgsz//16,4),imgsz)
im[512:1536,512:1536]=im2[512:1536,512:1536]
for t in range(10000):
    print('rendering frame %08d...'%t)
    imw=imwarp(im,radial_warp(t),cycle)
    imsave(imw,'video%08d.png'%t)

