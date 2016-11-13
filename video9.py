from common import *
# floor tiles metamorphosis
imgsz=(2048,)*2
x,y=meshgrid_euclidean(imgsz)
c=lambda x: np.cos(math.pi*x)
f=8./imgsz[0]
nf=250
for frame in range(nf):
    print('rendering frame %08d...'%frame)
    b=min(1.,max(0.,1.3*abs(math.fmod(2*frame/125.,2)-1)))
    q=int(frame>=nf*0.25 and frame<=nf*0.75)
    im=(c(y*f)+b*c(x*f)>0)^(c(q+x*f)+b*c(y*f)>0)^q
    #imshow(im)
    imsave(im,'video9-%08d.png'%frame)
