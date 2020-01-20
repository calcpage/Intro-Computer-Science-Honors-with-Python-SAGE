#!/usr/bin/python
#tree.py    MrG    2013.0521
import random
import turtle

def tree(branchLen,t,s):
    if branchLen > 0:
        t.pensize(s)
        if branchLen==8:
             t.color("darkgreen")
        else:
             t.color("brown")
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-8,t,s-1)
        t.left(40)
        tree(branchLen-8,t,s-1)
        t.right(20)
        t.backward(branchLen)
        t.color("brown")

t = turtle.Turtle()
t.left(90)
t.up()
t.backward(100)
t.down()
t.speed(100)
tree(80,t,10)
turtle.mainloop()