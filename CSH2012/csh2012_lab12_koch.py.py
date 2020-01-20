#!/usr/bin/python
#koch.py     MrG     2013.0530
import turtle

def flake(t, length, depth):
    if depth==1:
        t.fd(length)
    else:
        length/=3
        flake(t,length,depth-1)
        t.left(60)
        flake(t,length,depth-1)
        t.right(120)
        flake(t,length,depth-1)
        t.left(60)
        flake(t,length,depth-1)

alex=turtle.Turtle()
alex.pencolor('green')
alex.pensize(2)
alex.speed(0)

alex.pu()
alex.backward(150)
alex.left(90)
alex.forward(250)
alex.right(90)
alex.pd()

level=5
for i in range(6):
    flake(alex,300,level)
    alex.right(60)

turtle.mainloop()