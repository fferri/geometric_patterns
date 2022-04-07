from common import *

def draw(**kwargs):
    imgsz=(2048,)*2
    r,a=meshgrid_polar(imgsz)
    lr=np.log(1+r)
    im=np.sin(a*5+np.sin(lr*4)+lr*2)
    im=np.fmod((1+im+lr),1)
    im=apply_colormap(im,colormap.hot)
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p22.png')
