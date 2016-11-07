from common import *
# "the flower of life"
imgsz=(2048,)*2
r0=imgsz[0]*0.124
xy=set([(0,0,0)])
for (a1,a2) in [np.array((i,(i+1)%6))*math.pi/3+math.pi/6 for i in range(6)]:
    for j in range(1,5):
        (x1,y1),(x2,y2)=((math.cos(a)*r0*j,math.sin(a)*r0*j) for a in (a1,a2))
        xy.add((x1,y1,j))
        xy.add((x2,y2,j))
        for h in np.linspace(0,1,j+1)[1:-1]:
            xy.add((h*x1+(1-h)*x2,h*y1+(1-h)*y2,j))
circles=[1.*j*(meshgrid_distance(imgsz,(imgsz[0]*0.5+x,imgsz[1]*0.5+y))<=r0) for x,y,j in xy]
from functools import reduce
im=reduce(lambda a,b: a+b, circles)
im=apply_colormap(im,colormap.rainbow2)
imshow(im)
imsave(im,'p23.png')
