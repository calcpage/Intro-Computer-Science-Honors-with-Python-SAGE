#CSH305 All About Arguments MrG
show('#1) what does // do?')
def findDiv(x,y):
    return x//y
show('findDiv(3,2)=',findDiv(3,2))
show('findDiv(-7,3)=',findDiv(-7,3))
def findMod(x,y):
    return x%y
show('findMod(3,2)=',findMod(3,2))
show('findMod(-7,3)=',findMod(-7,3))
show('')

show('#2) what does / do?')
def findDiv(x,y):
    return x/y
show('findDiv(3,2)=',findDiv(3,2))
show('findDiv(-7,3)=',findDiv(-7,3))
show('')

show('#3) find the arithmetic mean')
def findMean(a,b):
    return (a+b)/2
show('findMean(5,10)=',findMean(5,10))
show('findMean(5,10)=',findMean(5,10).n())
show('findMean(5,10)=',n(findMean(5,10)))
show('')

show('#4) what does this code do?')
a=1
b=2
def swap(x,y):
    temp=x; x=y; y=temp
    return [x,y]
show('swap(a,b)=',swap(a,b))
show('a=',a)
show('b=',b)
show('')

show('#5) can we fix it?')
def swap(myList):
    temp=myList[0];myList[0]=myList[1];myList[1]=temp
pair=[3,4];show('pair=',pair)
swap(pair);show('pair=',pair)
show('')

show('#6) why not this?')
def swap(myList):
    return [myList[1],myList[0]]
pair=[4,5];show('pair=',pair)
swap(pair);show('pair=',pair)
show('')

show('#7) can we code the quadratic formula calling sqrt() only once?')
def quadForm(a,b,c):
    temp=sqrt(b**2-4*a*c)
    root1=(-b+temp)/(2*a)
    root2=(-b-temp)/(2*a)
    return [root1,root2]
show('quadForm(1,2,-1)=',quadForm(1,2,-1))
show('quadForm(1,2,0)=',quadForm(1,2,0))
show('quadForm(1,2,1)=',quadForm(1,2,1))
show('quadForm(1,2,2)=',quadForm(1,2,2))
show('')

show('#8) how to default arguments work?')
def double(x=0):
    return 2*x
show('double()=',double())
show('double(-2.3)=',double(-2.3))
show('double=',double)
show('')

show('#9a) what happens when you call printNames(5)?')
def printNames(n,obj):
    'prints obj n times'
    count=0
    result='' #initialize to empty string, no spaces
    while count<n:
        result+=str(obj)
        count+=1
    print(result)
#show('printNames(5)=',printNames(5))
show('')

show('#9b) can you fix it?')
def printNames(n,obj='&'):
    'prints obj n times'
    count=0
    result='' #initialize to empty string, no spaces
    while count<n:
        result+=str(obj)
        count+=1
    print(result)
show('printNames(5)=',printNames(5))
show('')

show('#9c) can you get rid of the None?')
def printNames(n,obj='&'):
    'prints obj n times'
    count=0
    result='' #initialize to empty string, no spaces
    while count<n:
        result+=str(obj)
        count+=1
    return(result)
show(printNames(5))
show(printNames(5,6))