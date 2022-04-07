from common import *

def draw(*args):
    imgsz=np.array([2*1024]*2)
    r,a=meshgrid_polar(imgsz,dist=distance.L1)
    r=np.uint(5*np.log(1+r))%2
    a=np.uint(np.floor(a*16/math.pi/2))%2
    im=r^a
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p16.png')
