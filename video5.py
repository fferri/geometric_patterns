from common import *

# plasma effect

imgsz=(1280,800)
y,x=meshgrid_euclidean(imgsz)

def draw(t=0, *args):
    cx1,cy1=x-imgsz[1]*0.5*(1+math.cos(t*0.01)),y-imgsz[0]*0.5*(1+math.sin(t*0.01))
    v1=np.sin(np.sqrt(cx1**2+cy1**2)/imgsz[0]*12+t*0.0354837)
    v2=np.sin(9*(1+0.4*math.sin(t*0.04566))*x/imgsz[1]*math.sin(t*0.01)+7*(1+0.6*math.cos(t*0.0463))*y/imgsz[0]*math.cos(t*0.00784)+t*0.0295528)
    v3=np.sin(0.546427+np.sqrt(cx1**2+cy1**2)/imgsz[0]*6+t*0.0156737)
    v4=np.sin(0.4635+3*(1+0.5*math.sin(t*0.06566))*x/imgsz[1]*math.sin(t*0.01)+5*(1+0.6*math.cos(t*0.0463))*y/imgsz[0]*math.cos(t*0.00784)+t*0.0195528)
    im=v1*(0.7+0.6*math.sin(t*0.04526))+v2*(0.8+0.7*math.cos(t*0.05))+v3+v4
    im=apply_colormap(im,colormap.jet)
    return im

if __name__ == '__main__':
    for t in range(8000):
        print('rendering frame %08d...'%t)
        im=draw(t)
        imsave(im,'video5-%08d.png'%t)
