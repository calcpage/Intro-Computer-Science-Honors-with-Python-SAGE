#CSH402 What Is A Sequence? MrG
show('#1) list a sequence for your own making:')
show('input: ',range(5))
show('output: ')
for n in range(5):
    show(2*n+3)
show('{3,5,7,...,2*n+3}=',[2*n+3 for n in range(5)])
show('{5,2,-1,...,5-3*n}=',[5-3*n for n in range(8)])
show('{5,15,45,...,5*3^n}=',[5*3^n for n in range(10)])
show('{2,1,1/2,..,2*(1/2)^n}=',[2*(1/2)^n for n in range(15)])
show('{2,0.4,0.008,...,2*(0.2)^n}=',[2*(0.2)^n for n in range(4)])
show('')

show('#2) generate this sequence: {1/2, 1/6, 1/12, 1/20, 1/30, 1/42}')
show([1/(n**2+n) for n in range(1,7)])
show('')

show('#3) demonstrate: if a0,a1,a2,a3,... is an arithmetic sequence')
show('#3) demonstrate: then a0,a3,a6,a9,... is also an arithmetic sequence')
show([(7*i+1) for i in range(10)])
show([(7*m+1) for m in range(0,10,3)])
show('')

show('#4) given a(0)=3, a(6)=21 find a(11).')
a(n)=3*n+3
show('a(11)=',a(11))
show([3*n+3 for n in range(12)])
show('')

show('#5) find the general term for this geometric sequence: a(0)=4,a(1)=12,a(2)=36')
a(n)=4*3^n;show('a(n)=',a(n))
#def a(n):
#    return 4*3^n
N=range(5);show('N=',N)
A=[a(j) for j in N];show('A=',A)
AN=zip(N,A);show('AN=',AN)
plot(points(AN))
show('')

show('#6) given geometric sequence: b(0)=1,b(10)=1024; find general term and find b(20)')
var('b,r')
b(n)=b*r^n;show('b(n)=',b(n))
show('b(10)/b(0)=',b(10)/b(0))
show('solve(r^10==1024,r):',solve(r^10==1024,r))
show([1*2^n for n in range(21)])
show('')

show('#7) prove a(n)=(a(n-1)+a(n+1))/2 given an arithmetic seq')
var('a,d')
a(n)=a+d*n
show('a(n-1)=',a(n-1))
show('a(n)=',a(n))
show('a(n+1)=',a(n+1))
show('(a(n-1)+a(n+1))/2=',(a(n-1)+a(n+1))/2)
show('(a(n-1)+a(n+1))/2=',((a(n-1)+a(n+1))/2).simplify_rational())
show('')

show('#8) prove b(n)=sqrt(b(n-1)*b(n+1)) given an geometric seq')
var('b,r')
b(n)=b*r^n
show('b(n-1)=',b(n-1))
show('b(n)=',b(n))
show('b(n+1)=',b(n+1))
show('sqrt(b(n-1)*b(n+1))=',sqrt(b(n-1)*b(n+1)))
show('sqrt(b(n-1)*b(n+1))=',(sqrt(b(n-1)*b(n+1))).canonicalize_radical())
show('')

show('#9) when does {a+n*d}={a*r^n}')
a(n)=4
show('a(n)=',[a(n) for n in range(10)])
show('d=a(5)-a(4)=',a(5)-a(4))
show('r=a(5)/a(4)=',a(5)/a(4))
show('')

show('#10) find limit of {0,1/2,2/3,3/4,...}')
b(n)=n/(n+1)
for n in range(10):
    show(b(n).n())
N=range(100)
B=[b(n) for n in N]
BN=zip(N,B)
show(plot(points(BN)))
show('')

show('#11) find limit of {4,5/2,2,7/4,...}')
b(n)=(n-2)/(n-5)
for n in range(6,16):
    show(b(n).n())
N=range(6,100)
B=[b(n) for n in N]
BN=zip(N,B)
show(plot(points(BN)))
show('')

show('#12) find limit of b(n)=n/sqrt(n**2-1)')
b(n)=n/sqrt(n**2-1)
for n in range(2,16):
    show(b(n).n())
N=range(2,100)
B=[b(n) for n in N]
BN=zip(N,B)
show(plot(points(BN)))