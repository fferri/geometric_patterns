import math
import numpy as np
from PIL import Image

def meshgrid_euclidean(shape):
    return np.meshgrid(*map(range,shape))

def meshgrid_polar(shape,center=None,dist='L2'):
    y,x=meshgrid_euclidean(shape)
    if center is None: center=np.array(shape)/2
    y,x=y-center[0],x-center[1]
    if dist == 'L1': r=np.abs(x)+np.abs(y)
    elif dist == 'L2': r=np.sqrt(x**2+y**2)
    elif dist == 'Linf': r=np.maximum(np.abs(x),np.abs(y))
    a=np.arctan2(x,y)
    return r,a

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
    box=np.zeros(shape,dtype=np.uint8)
    for delta in zip(range(0,shape[0]//2,shape[0]//2//n),range(0,shape[1]//2,shape[1]//2//n)):
        box=box^box2(shape,delta)
    return box

def imnormalize(im):
    im-=np.min(im)
    M=np.max(im)
    if M>0: im=im*255/M
    return im

def imshow(im,normalize=True):
    if normalize: im=imnormalize(im)
    im=Image.fromarray(np.float32(im))
    im.show()

def imsave(im,filename,normalize=True):
    if normalize: im=imnormalize(im)
    im=Image.fromarray(np.uint8(im))
    im.save(filename)

