#!/usr/bin/python
#ballistics03.py    MrG     2013.0531
#inspired by http://vpython.erikthompson.com
#horizontal and vertical displacement given velocity vector from the ground like a cannon!
#position is a vector!
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
t=0
dt=0.01

finished=False
while not finished:
    rate(100) #loop 100 times per sec
    t+=dt
    x=vx*t #x(t)=vx0*t+x0
    y=-0.5*g*t**2+0*t+vy*t+2 #y(t)=-g*t^2/2+vy0*t+y0
    print "t= " + str(t) + " x= " + str(x) + " y= " + str(y)
    ball.pos=(x,y,0) 
    if y-2<0:
        finished=True