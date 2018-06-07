from vpython import *
from math import *
from random import *
import numpy as np

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
Ms = 2e30 # masa sol
au = 1.49e11# unidad astronomica
R = au
sol = sphere(pos = vector(0,0,0), radius = 0.05 * au, color = color.white, make_trail=False) # sol

##----------------##



## Fuerza Gravitacional ##

# función signo
def Sig(r1,r2):
    if r1-r2 == 0:
        return 0
    else :
        return (abs(r1-r2)/(r1-r2))
# función distancia
def dis(a,b):
    return sqrt (((a.pos.x-b.pos.x)**2)+((a.pos.y-b.pos.y)**2))
# función calculo de fuerza
def ag(ca,cb,ma,mb):
    G = 6.67392e-11
    rab = dis(ca,cb)
    rab_x = (ca.pos.x-cb.pos.x)
    rab_y = (ca.pos.y-cb.pos.y)
    F_x = (G*ma*mb)* rab_x/((rab)**3)
    F_y = (G*ma*mb)* rab_y/((rab)**3)
    return np.array([F_x , F_y]) / mb

    #G = 6.67392e-11
    #rab = dis(ca,cb)
    #alfa = abs(asin((ca.pos.y-cb.pos.y)/dis(ca,cb)))
    #F = (G*ma*mb)/((rab)**2)
    #a = abs(F)/mb
    #ax = a*cos(alfa)*Sig(ca.pos.x,cb.pos.x)
    #ay = a*sin(alfa)*Sig(ca.pos.y,cb.pos.y)
    #ac=[ax,ay,a]    
    #return ac
##----------------------##


## datos planetas ##

n = 2 # numero de planetas
planetas = []
colores = [color.red,color.blue,color.green,color.yellow,color.orange]
for i in range(n):
    Mc = 1.0*randint(10,250) # masa cuerpo
    d = 35 # densidad
    r =  0.01 * au#((3.0*Mc)/(4*pi*d))**(1.0/3) # radio cuerpo
    c = sphere(pos = vector(0,R*2,0), radius = r, color = colores[randint(0,4)], make_trail=True) # cuerpos
    a = np.linalg.norm(ag(c,sol,Ms, Mc))
    v0 = vector(sqrt(a*(dis(c,sol))),0,0) # velocidad inicial
    cuerpo = [c,v0,Mc]
    planetas.append(cuerpo)

##----------------##


## inicio de movimiento ##
año = 365 * 24 * 3600
t = 1000
dt = año/2000

while True:

    rate(t)
    
    for i in planetas:
        
        ## movimiento c
        #if abs(i[0].pos.x)-80>80 or abs(i[0].pos.y)>80:
        #   i[1].x = 0
        #    i[1].y = 0
        #    i[0].radius = 0
        i[0].pos.x = i[0].pos.x + i[1].x*dt
        i[0].pos.y = i[0].pos.y + i[1].y*dt
        a = ag(sol,i[0],Ms,i[2])
        ax = a[0]
        ay = a[1]
        i[1].x = i[1].x + ax*dt
        i[1].y = i[1].y + ay*dt
        #print (sqrt(a[2]*dis(i[0],sol)))
