
from vpython import *
from math import *
from random import *

## Vectores unitarios ##
x_i = arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.red, shaftwidth=0.05)
txt_x = text(text='x', pos=x_i.pos+x_i.axis, axis=x_i.axis, align='center', height=0.4,
          color=color.red, billboard=True, emissive=True)

y_j = arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.blue, shaftwidth=0.05)
txt_y = text(text='y', pos=y_j.pos+y_j.axis, axis=y_j.axis, align='center', height=0.4,
          color=color.blue, billboard=True, emissive=True)

z_k = arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.green, shaftwidth=0.05)
txt_z = text(text='z', pos=z_k.pos+z_k.axis, axis=z_k.axis, align='center', height=0.4,
          color=color.green, billboard=True, emissive=True)

##--------------------##


## Datos estrella ##

d = 100 # densidad
Ms = 1500.0 # masa sol
R = ((3.0*Ms)/(4*pi*d))**(1.0/3) # radio sol
sol = sphere(pos = vector(20*R,0,0), radius = R, color = color.white, make_trail=False) # sol

##----------------##


## datos planetas ##

n = 8 # numero de planetas
planetas = []
colores = [color.red,color.blue,color.green,color.yellow,color.orange]
for i in range(n):
    if random()>0.75:
        s = 1
    else:
        s = -1
    Mc = 1.0*randint(10,250) # masa cuerpo
    d = 35 # densidad
    r = ((3.0*Mc)/(4*pi*d))**(1.0/3) # radio cuerpo
    c = sphere(pos = vector(20*R,20 + random()*R*18,0), radius = r, color = colores[randint(0,4)], make_trail=False) # cuerpo
    v0 = vector(s*randint(10,15),0,0) # velocidad inicial
    cuerpo = [c,v0,Mc]
    planetas.append(cuerpo)

##----------------##


## Fuerza Gravitacional ##

# función calculo de fuerza
def Fg(a,b,ma,mb):
    G = 6.67392
    rab = sqrt (((a.pos.x-b.pos.x)**2)+((a.pos.y-b.pos.y)**2))
    F = (G*ma*mb)/((rab)**2)
    return abs(F)
# función signo
def Sig(r1,r2):
    if r1-r2 == 0:
        return 0
    else :
        return (abs(r1-r2)/(r1-r2))
##----------------------##


## inicio de movimiento ##
t = 1000
dt = 1.0/t

while True:

    rate(t)

    for i in planetas:
        
        ## movimiento c
        if abs(i[0].pos.x)-80>80 or abs(i[0].pos.y)>80:
            i[1].x = 0
            i[1].y = 0
            i[0].radius = 0
        i[0].pos.x = i[0].pos.x + i[1].x*dt
        i[0].pos.y = i[0].pos.y + i[1].y*dt
        alfa = abs(atan((sol.pos.y-i[0].pos.y)/(sol.pos.x-i[0].pos.x)))
        a = Fg(sol,i[0],Ms,i[2])/(i[2])
        ax = a*cos(alfa)*Sig(sol.pos.x,i[0].pos.x)
        ay = a*sin(alfa)*Sig(sol.pos.y,i[0].pos.y)
        i[1].x = i[1].x + ax*dt
        i[1].y = i[1].y + ay*dt
    
