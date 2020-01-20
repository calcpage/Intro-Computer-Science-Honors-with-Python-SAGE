#!/usr/bin/python
#squareColor.py	MrG	2013.0318
import turtle
alex=turtle.Turtle()
alex.pensize(10)
alex.color("red")

def drawSquare(t, size):
    for i in ['red','gray','blue','green']:
	t.color(i)
        t.forward(size)
        t.left(90)

size=40
for i in range(15):
    drawSquare(alex, size)
    alex.right(18)
    size=size+10

turtle.mainloop()