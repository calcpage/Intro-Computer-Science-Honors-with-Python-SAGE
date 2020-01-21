#CSH405 What's An Iteration? 2020.0109 MrG
show('#2) print out any times table!')
def timesTable(num,nMax):
    n=1
    ans=num
    print('n\tans')
    while ans<=nMax:
        print(str(n)+'\t'+str(ans))
        n+=1
        ans+=num
show('timesTable(5,88)=',timesTable(5,22))
show('')

show('#4) make a table: n, s1(n), s2(n), 3*s2(n)/s1(n)')
show('#4) RESULT: 3*s2(n)/s1(n)=2*n+1')
show('#4) RESULT: 3*s2(n)/(n*(n+1)/2)=2*n+1')
show('#4) RESULT: s2(n)=n*(n+1)*(2*n+1)/6')
def mystery(nMax):
    n=1
    sum1=1
    sum2=1
    print('n\tsum1\tsum2\t3*sum2/sum1')
    while n<=nMax:
        print(str(n)+'\t'+str(sum1)+'\t'+str(sum2)+'\t'+str(3*sum2/sum1))
        n+=1
        sum1+=n
        sum2+=n^2
show('mystery(10)=',mystery(10))
show('')

show('#6) write myPow(x,n) that returns x^n but use a product loop')
def myPow(x,n):
    count=0
    power=1
    while count<n:
        count+=1
        power*=x
    return power
show('myPow(3,4)=',myPow(3,4))
show('myPow(15.3,160)=',myPow(15.3,160))
show('')

show('#8) nake a table of perfect numbers!')
def sumOfDivisors(number):
    mySum=0
    divisor=1
    while divisor<number:
        if number%divisor==0:
            mySum+=divisor
        divisor+=1
    return mySum
show('sumOfDivisors(6)=',sumOfDivisors(6))
print('number\tperfect')
for i in range(1,10):
    if i==sumOfDivisors(i):
        print(str(i)+'\tTRUE!!!')
    else:
        print(str(i)+'\tfalse')
show('')

show('#1) 1+3+5+7+...+N=?')
def sumOdd(n):
    term=1
    sum=1
    print('term\tsum')
    while term<n:
        print(str(term)+'\t'+str(sum))
        term+=2
        sum+=term
print(sumOdd(11))
show('')

show('#3) print out a table of factorials')
def factTable(n):
    product=1
    count=1
    print('n\tfactorial')
    while count<n:
        print(str(count)+'\t'+str(product))
        count+=1
        product*=count
print(factTable(11))
show('')

show('#5) print our a square of length n')
def printSqr(n):
    print(n*'*')
    line=1
    while line<n-1:
        print('*'+(n-2)*' '+'*')
        line+=1
    print(n*'*')
print(printSqr(5))
show('')

show('#7) find the smallest divisor of n>1')
def smallestDiv(n):
    divisor=2
    while divisor<n:
        if n%divisor==0:
            return divisor
        divisor+=1
show('smallestDiv(25)=',smallestDiv(25))