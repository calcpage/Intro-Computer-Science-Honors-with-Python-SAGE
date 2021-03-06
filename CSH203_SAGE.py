#CSH203 What's An Interpreter 2019.1018 MrG
show('#1) Python has no redundancy')
show('')
show('#2) what do 2+-2 and 2++2 mean?')
show('2+-2=',2+-2)
show('2++2=',2++2)
show('')
show('#3) what does 2+++2 mean?')
show('2+++2=',2+++2)
show('2+(+(+2))=',2+(+(+2)))
show('')
show('#4) what do 2**3 and 2**4 mean?')
show('#4) 2**3=',2**3)
show('#4) 2**4=',2**4)
show('#4) 2^3=',2^3)
show('#4) 2^4=',2^4)
show('')
show('#5) what does "abc"+"def" mean')
show('#5) "abc"+"def"=',"abc"+"def")
show('#5) "abc"+"def"=','abc'+'def')
show('')
show('#6) what does 3*"12" do?')
show('#6) 3*"12"=',3*"12")
show('#6) 5*"abc"=',5*"abc")
show('')
show('#7) what is the order of operations in python?')
show('9-8*2+6=',9-8*2+6)
show('(5-1)*(1+2)**3=',(5-1)*(1+2)**3)
show('')
show('#8) which parentheses are redundant: (x-2)**3+(3*x)?')
f(x)=(x-2)**3+(3*x)
g(x)=(x-2)**3+3*x
h(x)=x-2**3+3*x
i(x)=x-2**3+(3*x)
show(plot([f(x),g(x),h(x),i(x)],-1,10))
show('')
show('#9) what is the order of operations: 1+reciprocal(2*5)')
def reciprocal(x):
    return 1/x
show('1+reciprocal(2*5)=',1+reciprocal(2*5))
show('1+reciprocal(2*5)=',1+reciprocal(2*5).n())
show('1+reciprocal(2*5)=',(1+reciprocal(2*5)).n())
show('1+reciprocal(2*5)=',n(1+reciprocal(2*5)))
show('')
show('#10) Pythonic Order Of Operations:')
show('#10) 1st ORDER: +,- (UNARY)')
show('#10) 2nd ORDER: ()')
show('#10) 3rd ORDER: ^,** (BINARY)')
show('#10) 4th ORDER: *,/,//,% (BINARY)')
show('#10) 5th ORDER: +,- (BINARY)')