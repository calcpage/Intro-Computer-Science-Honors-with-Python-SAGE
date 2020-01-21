#!/usr/bin/python
#ballistics04.py    MrG     2013.0531
#inspired by http://vpython.erikthompson.com
#horizontal and vertical displacement like a cannon with a cross wind!
#position is a vector!
#velocity is a vector!
from visual import *

scene.width=800
scene.height=600
scene.autoscale=0
scene.range=(100,100,100) #(l,w,h)
scene.center=(50,40,0) #pos vector

ball=sphere(pos=(0,2,0),radius=2,color=color.red)
ground=box(pos=(50,-1,0),size=(100,2,10),color=color.green)

g=9.8 #m/s/s
vel=40 #m/s
ang=80 #degrees
ang=ang*pi/180 #radians
vx=vel*cos(ang)
vy=vel*sin(ang)
vz=0
vThrow=vector(vx,vy,vz)
vWind=vector(2,1,-5)
vTotal=vThrow+vWind
t=0
dt=0.01

finished=False
while not finished:
    rate(100) #loop 100 times per sec
    t+=dt
    x=vTotal.x*t #x(t)=vx0*t+x0
    y=-0.5*g*t**2+0*t+vTotal.y*t+2 #y(t)=-g*t^2/2+vy0*t+y0
    z=vTotal.z*t #z(t)=vz0*t+z0
    print "t= " + str(t) + " x= " + str(x) + " y= " + str(y)
    ball.pos=(x,y,z) 
    if y-2<0:
        finished=True
        mylabel=label(pos=(50,60,0),text="seconds in flight: "+str(t),height=10)
