from math import sin, cos
\
WIDTH = 256
HEIGHT = 256

cx = int(WIDTH/2)
cy = int(HEIGHT/2)

def frag(u,v):
    u = u/WIDTH
    v = v/HEIGHT

    return (u, v, 255)

def grid(u,v): #interesting: I made a mistake and let the values of rgb be <0, but instead of giving me a bug, a cool grid was formed
    return (sin(u), cos(v), 0)


def color_oscillation(u,v):
    return ( (sin(u) + 1)/2 , (cos(v) +1)/2, 0 )

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
    

f = open("img.ppm", "w")

f.write(f"P3 \n {WIDTH} {HEIGHT} 255 \n")

for y in range(HEIGHT):
    for x in range(WIDTH):

        r , g, b = circle(x,y, 2000)

        f.write(f"{int(r*255)} {int(g*255)} {int(b*255)} ")


