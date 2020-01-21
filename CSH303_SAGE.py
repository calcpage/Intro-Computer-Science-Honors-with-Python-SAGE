#CSH303 Variable Scope 2019.1107
show('#1) Local Variables live inside a function,')
show('#1) Global Variables works anywhere else.')
show('')
show('#2) define f(x)=(sqrt(x)+1)/(sqrt(x)-1) but only call sqrt() once')
def f(x):
    root=sqrt(x)
    return (root+1)/(root-1)
show('#2) f(4)=',f(4))
show('#2) f(3.1415926)=',f(3.1415926))
show('#2) f(pi)=',f(pi))
show('#2) f(pi)=',f(pi).n())
show('')
show('#3) Fix this code:')
def factorial(n):
    f=1
    k=2
    while k<=n:
        f*=k #f=f*k
        k+=1 #k=k+1
    return f
show('#3) factorial(5)=',factorial(5))
show('')
show('#4a) compare these 2 functions')
k=10
def kTimes(x):
    return k*x
show('#4a) kTimes(5)=',kTimes(5))
show('#4a) there is no syntax error, there is no semantic error')
show('')
show('#4b) compare these 2 functions')
k=10
def kTimes(x):
    k=5
    return k*x
show('#4b) kTimes(5)=',kTimes(5))
show('#4a) there is no syntax error, there is a semantic error')