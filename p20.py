from common import *
sq=np.array((256,)*2)
imgsz=sq*6
k=8 # try 128
h,v=map(lambda im: im//k%2, meshgrid_euclidean(imgsz))
c=checkerboard(imgsz,sq)
im=c*h+(1-c)*(1-v)
imshow(im)
imsave(im,'p20.png')
