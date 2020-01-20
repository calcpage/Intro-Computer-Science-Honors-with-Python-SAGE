#!/usr/bin/python
#sphere.py    MrG     2013.0531
#inspired by Kirby Urner 
# http://www.youtube.com/user/kirbyurner 
# http://www.4dsolutions.net/ocn/index.html
from visual import *
from random import randint

scene.width=1100
scene.height=1100
scene.range=(100,100,100)
thecolors=[color.green,color.red,color.orange,color.cyan,color.magenta,color.yellow]

for i in range(1000):
    place=(randint(-1000,1000),randint(-100,100),randint(-10,10))
    rsize=randint(0,10)
    rcolor=randint(0,5)
    ball=sphere(pos=place,radius=rsize,color=thecolors[rcolor])