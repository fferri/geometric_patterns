from common import *
s=256
im=checkerboard(s,s//2)
for i in range(6):
    im[0,...]^=1
    im[-1,...]^=1
    im[...,0]^=1
    im[...,-1]^=1
    s//=2
    c=checkerboard(s,s//2)
    ch=imtile(c,(c.shape[0],im.shape[1]))
    cv=imtile(c,(im.shape[0]+2*c.shape[0],c.shape[1]))
    im=np.hstack((cv,np.vstack((ch,im,ch)),cv))
imshow(im)
imsave(im,'p1.png')
