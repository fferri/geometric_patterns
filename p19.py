from common import *

def spiral(shape,nbands=16,twist=0.1):
    r,a=meshgrid_polar(shape)
    return np.sin(np.log(1+10*(1+np.sin(r*0.002)))*twist+a*nbands)+1/(1.2+0.0007*r)
imgsz=(2048,2048)
s1,s2=(spiral(imgsz,3,16*i) for i in (-1,1))
im=s1*s2
cmap=np.zeros((256,3), dtype=np.uint8)
cmap[0:49,:]=[185,0,0]
cmap[155:185,:]=[255,205,0]
cmap|=colormap.contours(4,3)
im=apply_colormap(im,cmap)
imshow(im)
imsave(im,'p19.png')
