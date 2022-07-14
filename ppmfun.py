from math import sin, cos

WIDTH = 256
HEIGHT = 256

cx = int(WIDTH/2)
cy = int(HEIGHT/2)

sqrt2over2 = 0.7071


def frag(u,v):
    u = u/WIDTH
    v = v/HEIGHT

    return (u * 2, v *2 , 255)

def grid(u,v): #interesting: I made a mistake and let the values of rgb be <0, but instead of giving me a bug, a cool grid was formed
    return (sin(u), cos(v), 0)


def color_oscillation(u,v):
    return ( (cos(u) + 1)/2 , (sin(v) +1)/2, 100 )

def crazy(u,v):
    u = u/WIDTH
    v = v/HEIGHT

    return (u+v, u-v, 255)

def xadrez(u,v):

    if (u % 20 < 10):
        u = 1
    
    else:
        u = 0

    if (v % 20 < 10):
        v = 1
    
    else:
        v = 0

    return (u, v , 1 )



def circle(u,v, radius): 
    if (u - cx)**2 + (v - cy)**2 <= radius:
        return (1,0,0)
    else:
        return (1,1,1)   

def france(u):

    if(u < WIDTH/3):
        return (0,0,1) #blue
    elif (u < 2* WIDTH/3):
        return (1,1,1) #white
    else:
        return (255,0,0) #red

def brazil(u,v,a,b, radius, ribbon_width):


    # checking if the coordinates are inside the diamond 
    #change of basis 
    uu = (u - cx +v - cy)*sqrt2over2
    vv = (v - cy -u + cx) * sqrt2over2
     
    if uu > -a/2  and uu < a/2  and vv > - b/2 and vv < b/2 :       

        #checking if we are inside the circle

        if ((u - cx)**2 + (v - cy)**2 <= radius):

            if (uu < ribbon_width/2 and uu > -ribbon_width/2):
                return (0.9,0.9,0.9)
            else:
                return (0, 0 , 0.8) #circle color
        else:
            return (0.7,0.7, 0) #diamond color
    else:
        return (0,0.2,0) #flag background


def centerd_square(u,v):

    if u - cx < 100 and u - cx > -100 and v - cy < 100 and v - cy > -100:
        return (1,0,0)
    else:
        return (0,0,1)   


f = open("img.ppm", "w")

f.write(f"P3 \n {WIDTH} {HEIGHT} 255 \n")

for y in range(HEIGHT):
    for x in range(WIDTH):

        r , g, b = brazil(x,y, 150, 150, 1500, 10)
        # r , g, b = centerd_square(x,y)c

        f.write(f"{int(r*255)} {int(g*255)} {int(b*255)} ")


