#!/usr/bin/python
#parse.py    MrG    2013.0513
import turtle
alex=turtle.Turtle()
alex.pensize(10)
alex.color('red')
alex.speed(10)

input = open("mystery.dat","r")
for line in input:
    if line[0]=="D":
        alex.pd()
    elif line[0]=="U":
        alex.pu()
    else:
	point=line.split()
        alex.goto(int(point[0]),int(point[1]))

turtle.mainloop()
input.close()