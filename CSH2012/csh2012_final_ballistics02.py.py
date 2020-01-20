#!/usr/bin/python
#ballistics02.py    MrG     2013.0531
#inspired by http://vpython.erikthompson.com
#horizontal and vertical displacement without air resitance a la Galileo
#position is a vector!
from visual import *

scene.width=800
scene.height=600
scene.autoscale=0
scene.range=(100,100,100) #(l,w,h)
scene.center=(0,40,0) #pos vector

ball=sphere(pos=(0,102,0),radius=2,color=color.red)
ground=box(pos=(0,-1,0),size=(100,2,10),color=color.green)
building=box(pos=(0,50,0),size=(6,100,6),color=color.blue)

g=9.8 #m/s/s
t=0
dt=0.01

finished=False
while not finished:
    rate(100) #loop 100 times per sec
    t+=dt
    x=5*t #x(t)=vx0*t+x0
    y=-0.5*g*t**2+0*t+15*t+100 #y(t)=-g*t^2/2+vy0*t+y0
    print "t= " + str(t) + " x= " + str(x) + " y= " + str(y)
    ball.pos=(x,y,0) 
    if y-2<0:
        finished=True