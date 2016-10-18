from common import *

x,y=np.meshgrid(range(512),range(512))
r1=np.sqrt((x-384)**2+(y-384)**2)
r2=np.sqrt((x-128)**2+(y-128)**2)
im=np.sin(np.minimum(r1,r2)*math.pi/10)>0
imshow(im)
imsave(im,'p11.png')
