from common import *
r,a=meshgrid_polar((2048,)*2)
im=np.sin(a*8+5*np.log(1+r))
im=apply_colormap(im,colormap.rainbow)
imshow(im)
imsave(im,'p17.png')
