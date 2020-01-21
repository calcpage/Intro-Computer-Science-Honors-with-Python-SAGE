#!/usr/bin/python
#movingTurtles.py	MrG	2013.0409
import turtle
import random

t=turtle.Turtle()
t.color("red")
t.pensize(5)
t.speed(100)

wn=turtle.Screen()
wn.bgcolor("grey")

print wn.window_width()
print wn.window_height()

def isInScreen(wn,t):
    xmin = -wn.window_width()/2
    xmax = wn.window_width()/2
    ymin = -wn.window_height()/2
    ymax = wn.window_height()/2

    x = t.xcor()
    y = t.ycor()

    if x<xmin or x>xmax:
        return False
    if y<ymin or y>ymax:
        return False
    return True

while isInScreen(wn,t):
    t.fd(50)
    isInScreen(wn,t)
    coin=random.randrange(2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)
    
turtle.mainloop()
