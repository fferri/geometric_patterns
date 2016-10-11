from common import *

imgsz=np.array([2*1024]*2)
box_tile=boxN(imgsz//8, 8)
chk_tile=checkerboard(imgsz//8, imgsz//16)
im=imtile(chk_tile^box_tile,imgsz)
imshow(im)
imsave(im,'p2.png')
