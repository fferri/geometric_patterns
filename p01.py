from common import *

def draw(*args):
    s=2**9
    k=2 # try 1, 2, 3...

    im=checkerboard(s,s//k)
    for i in range(6):
        im[[0,-1],...]^=1
        im[...,[0,-1]]^=1
        s//=2
        ch=checkerboard((s,im.shape[1]),s//k)
        cv=checkerboard((im.shape[0]+2*s,s),s//k)
        im=np.vstack((cv,np.hstack((ch,im,ch)),cv))
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p01.png')
