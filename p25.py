from common import *

# floor tiles

def draw(*args):
    imgsz=(2048,)*2
    x,y=meshgrid_euclidean(imgsz)
    s=lambda x: np.sin(math.pi*x)
    b=0.5
    h=s(y*8/imgsz[0])+b*s(x*8/imgsz[1])
    v=s(1+x*8/imgsz[0])+b*s(y*8/imgsz[1])
    im=(h>0)^(v>0)
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p25.png')
