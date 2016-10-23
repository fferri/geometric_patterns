import math
import numpy as np
from PIL import Image

class norm:
    @staticmethod
    def L1(x1,x2):
        return np.abs(x1)+np.abs(x2)
    @staticmethod
    def L2(x1,x2):
        return np.sqrt(x1**2+x2**2)
    @staticmethod
    def Linf(x1,x2):
        return np.maximum(np.abs(x1),np.abs(x2))

distance = norm

def meshgrid_euclidean(shape):
    return np.meshgrid(*map(range,shape))

def meshgrid_distance(shape,center=None,dist=distance.L2):
    y,x=meshgrid_euclidean(shape)
    if center is None: center=np.array(shape)/2
    y,x=y-center[0],x-center[1]
    return dist(x,y)

def meshgrid_polar(shape,center=None,dist=distance.L2):
    y,x=meshgrid_euclidean(shape)
    if center is None: center=np.array(shape)/2
    y,x=y-center[0],x-center[1]
    return dist(x,y),np.arctan2(x,y)

def meshgrid_hyperbolic(shape):
    y,x=meshgrid_euclidean(shape)
    u=0.5*(np.log(x+1)-np.log(y+1))
    v=np.sqrt(x*y)
    return u,v

def clip(x,xmax):
    return np.minimum(xmax-1,np.maximum(0,x))

def cycle(x,xmax):
    return np.fmod(-np.minimum(0,np.ceil(x/xmax))*xmax+x,xmax)

def imwarp(im,fn,oob=clip):
    warped=np.zeros(im.shape,dtype=np.uint8)
    i,j=meshgrid_euclidean(im.shape)
    h,k=fn(i,j)
    h,k=oob(h,im.shape[0]),oob(k,im.shape[1])
    h,k=np.int32(h),np.int32(k)
    i,j,h,k=map(lambda x: x.reshape(-1), (i,j,h,k))
    warped[i,j]=im[h,k]
    return warped 

def imtile(im,shape):
    im=np.kron(np.ones(tuple(int(0.5+shape[i]/im.shape[i]) for i in range(2)),dtype=np.uint8),im)
    return im[0:shape[0],0:shape[1]]

def checkerboard(shape,sqshape,inv=False):
    if isinstance(shape,(int,float))==1: shape=(int(shape),int(shape))
    if isinstance(sqshape,(int,float))==1: sqshape=(int(sqshape),int(sqshape))
    y,x=np.meshgrid(*map(range,shape))
    return (x//sqshape[1]%2)^(y//sqshape[0]%2)

def box2(shape,delta):
    box=np.zeros(shape,dtype=np.uint8)
    box[delta[0]:shape[0]-delta[0], delta[1]:shape[1]-delta[1]]=1
    return box

def boxN(shape,n):
    box=meshgrid_distance(shape,None,distance.Linf)
    l=max(shape)//(n*2)
    box=box//l%2
    return np.uint8(box)

def imnormalize(im):
    im-=np.min(im)
    M=np.max(im)
    if M>0: im=im*255/M
    return im

def imshow(im,normalize=True):
    if len(im.shape)==2:
        if normalize: im=imnormalize(im)
        im=np.float32(im)
    if len(im.shape)==3 and im.shape[2]==3:
        im=np.uint8(im)
    im=Image.fromarray(im)
    im.show()

def imsave(im,filename,normalize=True):
    if len(im.shape)==2:
        if normalize: im=imnormalize(im)
    im=Image.fromarray(np.uint8(im))
    im.save(filename)

def apply_colormap(im,cmap,prenormalize=True):
    if callable(cmap): cmap=cmap()
    if cmap.shape != (256,3): raise ValueError('colormap must be 256x3 uint8 values')
    if prenormalize: im=imnormalize(im)
    return cmap[np.uint8(im.reshape(-1))].reshape(im.shape+(3,))

def make_colormap(colors,positions=None):
    if positions is None: positions=np.uint8(np.linspace(0,255,len(colors)))
    colors=np.array(colors)
    if colors.shape[1] != 3: raise ValueError('colors must be Nx3 uint8 values')
    if len(positions) != colors.shape[0]: raise ValueError('positions must be an array of %d floating point values' % colors.shape[0])
    if any(pos < 0 or pos > 255 for pos in positions): raise ValueError('positions must be between 0 and 255')
    cmap=np.zeros((256,3), dtype=np.uint8)
    for c1,c2,p1,p2 in zip(colors,colors[1:],positions,positions[1:]):
        for i in range(p1,p2+1):
            x=(i-p1)/(p2-p1)
            cmap[i,:]=c1*(1-x)+c2*x
    return np.uint8(cmap)

class colormap:
    @staticmethod
    def rainbow():
        cc=[[255,0,0],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[255,0,255],[255,0,0]]
        pp=[0,25,76,127,178,229,255]
        return make_colormap(cc,pp)

