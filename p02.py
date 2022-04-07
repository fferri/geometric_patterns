from common import *

def draw(**kwargs):
    imgsz=np.array([2*1024]*2)
    box_tile=boxN(imgsz//8, 8)
    chk_tile=checkerboard(imgsz//8, imgsz//16)
    im=imtile(chk_tile^box_tile,imgsz)
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p02.png')
