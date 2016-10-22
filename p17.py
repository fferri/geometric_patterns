from common import *
r,a=meshgrid_polar((2048,)*2)
im=np.sin(a*8+5*np.log(1+r))
cmap=make_colormap([[255,0,0],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[255,0,255]])
im=apply_colormap(im,cmap)
imshow(im)
imsave(im,'p17.png')
