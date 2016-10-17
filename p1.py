from common import *
s=256
im=checkerboard(s,s//2)
for i in range(6):
    im[[0,-1],...]^=1
    im[...,[0,-1]]^=1
    s//=2
    ch=checkerboard((s,im.shape[1]),s//2)
    cv=checkerboard((im.shape[0]+2*s,s),s//2)
    im=np.hstack((cv,np.vstack((ch,im,ch)),cv))
imshow(im)
imsave(im,'p1.png')
