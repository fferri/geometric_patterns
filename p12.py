from common import *

def draw(*args):
    w,h=2048,2048
    x,y=np.meshgrid(range(w),range(h))
    r=np.sqrt((x-w/2)**2+(y-h/2)**2)
    a=np.arctan2(x-w/2,y-h/2)
    im1=np.sin(np.log(1+r)*math.pi*16)>0
    im2=np.sin(4*math.pi*np.cos(a*8+8*np.log(1+r)))>0
    return im1^im2

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p12.png')
