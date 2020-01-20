#!/usr/bin/python
#pascal.py     MrG    2013.0524

def pascal(n,r):
    if n==r or r==0:
        return 1
    return pascal(n-1,r)+pascal(n-1,r-1)

for n in range(8):
    for r in range(n+1):
        print pascal(n,r),"\t",
    print