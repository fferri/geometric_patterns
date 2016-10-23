from common import *
# inspired by a Aldous Huxley's book cover
r,a=meshgrid_polar((2048,)*2)
im=np.fmod(np.float32(3.5*np.log(1+r))+2*np.power(np.abs(np.sin(8*np.float32(a))),0.4),1.4)
cmap=make_colormap([[255,0,0],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[255,0,255]])
im=apply_colormap(im,cmap)
imshow(im)
imsave(im,'p18.png')
