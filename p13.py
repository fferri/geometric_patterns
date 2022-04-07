from common import *

# hyperbolic coords checkerboard

def draw(**kwargs):
    w,h=2048,2048
    u,v=meshgrid_hyperbolic((w,h))
    u=np.uint(u*10)%2
    v=np.uint(v//300)%2
    im=u^v
    im=np.hstack((im[...,::-1],im))
    im=np.vstack((im[::-1,...],im))
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p13.png')
