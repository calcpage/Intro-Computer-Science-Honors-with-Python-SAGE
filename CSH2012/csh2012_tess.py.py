#!/usr/bin/python
import turtle # set the window background colour

wn = turtle.Screen() # set the window title
wn.bgcolor("lightgreen") 
wn.title("Hello, Tess!") 

tess = turtle.Turtle(shape='triangle') # tell tess to change her color
tess.color("blue") # tell tess to set her pen width
tess.pensize(3) 
tess.forward(50)
tess.left(120)
tess.forward(50)

turtle.mainloop()