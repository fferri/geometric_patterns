from common import *
imgsz=(2048,)*2
r,a=meshgrid_polar(imgsz)
lr=np.log(1+r)
im=np.sin(a*5+np.sin(lr*4)+lr*2)
im=np.fmod((1+im+lr),1)
im=apply_colormap(im,colormap.hot)
imshow(im)
imsave(im,'p22.png')
