#CSH304 More About Pythonic Functions! MrG
show('#1) concatenate 2 strings')
def concatIt(s1,s2):
    return s1+' '+s2
show('concatIt("al","garcia")=',concatIt("al","garcia"))
show('')
show('#2) draw a house!')
def printHouse():
    print(" /\\\n/__\\\n|  |\n|__|")
    #print(" /\\")
    #print("/__\\")
    #print("|  |")
    #print("|__|")
printHouse()
show('')
show('#3) pad your strings!')
def rightJustify(s,w):
    'pad s with correct number of spaces in front'
    return ' '*(w-len(s))+s
show(rightJustify("bob",7))
show(rightJustify("bobbie",7))
show(rightJustify("Baldwin",7))
show(rightJustify("High",7))
show('')
show("#4a) what's wrong with this output?")
def print10Stars():
    print 10*'*'
show('print10Stars()=',print10Stars())
show('')
show('#4b) how to get rid of None?')
def make10Stars():
    return 10*'*'
show('make10Stars()=',make10Stars())
show('')
show('#5) predict the output')
def printTriangle(n,ch):
    while n>0:
        show(n*ch)
        n-=1
        return 1
show("printTriangle(2,'*')=",printTriangle(2,'*'))
show("printTriangle(3,'#')=",printTriangle(3,'#'))
show("printTriangle(2,'*')+printTriangle(3,'#')=",printTriangle(2,'*')+printTriangle(3,'#'))
show('')
show('#6) predict the output')
def sum1ToN(n):
    if n>0:
        return n*(n+1)//2
show('sum1ToN(6)=',sum1ToN(6))
show('sum1ToN(0)=',sum1ToN(0))
show('sum1ToN(-3)=',sum1ToN(-3))
show('')
show('#8) what is the output?')
#show('len(0)=',len(0))
show("len('0')=",len('0'))
show("len('''0''')=",len('''0'''))
show("len('''''')=",len(''''''))
show('len([0])=',len([0]))
show('len([])=',len([]))
#show('len((0))=',len((0)))
show('len(range(0)=',len(range(0)))