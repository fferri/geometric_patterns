from common import *

def square_spiral(shape,num_cycles):
    w,b=np.ones(shape,dtype=np.uint8),np.zeros(shape,dtype=np.uint8)
    im=np.hstack((b,w))
    z=[[w,b],[w,b],[b,w],[b,w]]
    for i in range(2,3+num_cycles):
        j=(i-2)%4
        if i<2+num_cycles:
            im=np.vstack((np.kron([1]*i,z[j][0]),im,np.kron([1]*i,z[j][1])))
        else:
            im=np.vstack((np.kron([1]*i,z[j][0]),im))
        im=im.T
    return im

def draw(**kwargs):
    s=square_spiral((4,4),10)
    s1=1-s.T[...,::-1]
    s2=s1[::-1,::-1]
    s2=s2[...,5:]
    q=np.hstack((s1,s2))
    q[-4:,...]=1
    q=np.vstack((q,q[...,::-1]))
    im=imtile(q,np.array(q.shape)*10)
    return im

if __name__ == '__main__':
    im=draw()
    imshow(im)
    imsave(im,'p04.png')
