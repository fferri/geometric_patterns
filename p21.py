from common import *

def draw(**kwargs):
    sq=np.array((64,)*2)
    imgsz=sq*32
    h,v=map(lambda im: im//sq[0]%2, meshgrid_euclidean(imgsz))
    im=apply_colormap((h+v)/2,make_colormap([[255,0,0],[255,255,255]],[0,255]))
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p21.png')
