#CSH105 Pythonic Functions 2019.0925 MrG
show('#1) What does % do?')
def mod3(n):
    return n%3
show('mod3(0)=',mod3(0))
show('mod3(1)=',mod3(1))
show('mod3(2)=',mod3(2))
show('mod3(3)=',mod3(3))
show('mod3(4)=',mod3(4))
show('mod3(5)=',mod3(5))
show('mod3(6)=',mod3(6))
show('')
show('#2) Write function that increments by 1')
def incrementByOne(x):
    return x+1
show('incrementByOne(3)=',incrementByOne(3))
show('incrementByOne(-4)=',incrementByOne(-4))
show('incrementByOne(1.5)=',incrementByOne(1.5))
show('')
show('#3) What does math.abs() do?')
show('abs(-2.6)=',abs(-2.6))
show('abs(7.1)=',abs(7.1))
plot(abs(x))
show('')
show('#4) sum(1,2,3,...,n)')
def sum1ToN(n):
    return (n+1)/2*n
show('1+2+3+4+5+6=',sum1ToN(6))
show('')
show('#5) make a function to find reciprocals')
def reciprocal(x):
    return 1/x
show('reciprocal(2.0)=',reciprocal(2.0))
show('reciprocal(-11/2)=',reciprocal(-11/2))
show('')
show('#6) combine incrementByOne() and double()')
def double(n):
    return 2*n
show('double(incrementByOne(5))=',double(incrementByOne(5)))
show('incrementByOne(double(5))=',incrementByOne(double(5)))
show('')
show('#7) can you increment a string literal?')
show('incrementByOne("123") does not support string+1')
show('')
show('#8) can you double a string literal')
show('double(double("123"))=',double(double("123")))
show('"123"+"123"=',"123"+"123")
show('')
show('#9) output the first letter of a string')
def firstLetter(s):
    return s[0]
show('firstLetter("Baldwin")=',firstLetter("Baldwin"))
show('')
show('#10) can you apply firstLetter to a list?')
show('firstLetter([1,2,3,4,5]")=',firstLetter([1,2,3,4,5]))
show('')
show('#11&12) what are the list operators?')
show('range(1,15,2)=',range(1,15,2))
show('sum(range(1,15,2))=',sum(range(1,15,2)))
show('min(range(1,15,2))=',min(range(1,15,2)))
show('max(range(1,15,2))=',max(range(1,15,2)))
show('')
show('#13) redo #4 without any arithmetic operators other than +')
def sum1ToN(n):
    return sum(range(n+1))
show('sum1ToN(6)=',sum1ToN(6))
show('')
show('#14) implement the pseudo code from example 1 in section 104 using python')
def numDigits(n):
    count=1
    power=10
    while power<=n:
        count=count+1
        power=power*10
    return count
show('numDigits(4321)=',numDigits(4321))