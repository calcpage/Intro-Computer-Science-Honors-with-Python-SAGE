#!/usr/bin/python
#factorial.py    MrG    2013.0517

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print "i\tfact(i)"
for i in range(100):
    print i,"\t",fact(i)
