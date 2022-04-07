from common import *

def kaleidoscope(x,y):
    def f(i,j):
        cy,cx=imgsz[0]*y,imgsz[1]*x
        r,a=np.sqrt((i-cy)**2+(j-cx)**2),np.arctan2(i-cy,j-cx)
        l=math.pi*2/4
        a=np.abs(np.fmod(1.5*(2*math.pi+a),l)-l/2)*2+math.sin(x+y+math.sin(x+4*y))
        return cy+r*np.sin(a),cx+r*np.cos(a)
    return f

def spiral(shape,nbands=16,twist=0.1):
    r,a=meshgrid_polar(shape)
    return np.sin(np.log(1+10*(1+np.sin(r*0.002)))*twist+a*nbands)+1/(1.2+0.0007*r)

imgsz=(1024,1024)
s1,s2=(spiral(imgsz,6,32*i) for i in (-1,1))
im=s1*s2

def draw(t=0, **kwargs):
    a=t*0.008
    r=0.2+0.15*math.sin(a*3)
    im2=imwarp(im,kaleidoscope(0.5+r*math.sin(a),0.5+r*math.cos(a)))
    im2=apply_colormap(im2,colormap.jet)
    return im2

if __name__ == '__main__':
    for t in range(4000):
        print('rendering frame %08d...'%t)
        im2=draw(t)
        imsave(im2,'video4-%08d.png'%t)

