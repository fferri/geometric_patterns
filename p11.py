from common import *
from functools import reduce

def draw(**kwargs):
    s=np.array((4096,4096))
    y,x=meshgrid_euclidean(s)
    pts=[]
    for (r,n,o) in ((0,1,0),(0.2,3,math.pi/6),(0.4,6,0)):
        for a in range(n):
            pts.append([getattr(math,f)(o+a*math.pi*2/n)*r+0.5 for f in ['cos','sin']])
    r=[np.sqrt((x-p[1]*s[1])**2+(y-p[0]*s[0])**2) for p in pts]
    r=reduce(np.minimum, r[1:], r[0])
    im=np.sin(r*math.pi/40)>0
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p11.png')
