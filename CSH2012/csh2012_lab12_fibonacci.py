#!/usr/bin/python
#fibonacci.py    MrG   2013.0528

def fib(one, two, n):
    if n==1:
        return one
    if n==2:
        return two
    return fib(one,two,n-1)+fib(one,two,n-2)

for n in range(100):
    print n, "\t" ,1.0*fib(2,-3,n+2)/fib(2,-3,n+1)
