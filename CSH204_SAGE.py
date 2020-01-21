#CSH204 2019.1023 Intro To Coding
show("#1) What's A Doc String?")
def first(s):
    '''this function returns the first char of a string s'''
    return s[0]
show('#1) first("Hello, World!") = ',first("Hello, World!"))
show('#1) the doc string = ',first.__doc__)
show('')
show('#2) list some reserved words: def, while, return')
show('')
show('#3) fix the code!')
def goodCode(x):
    return x^2-1
show('#3) goodCode(4)=',goodCode(4))
show('')
show('#4) what does this code do?')
print('one is better than \none' +\
'; two is better than one')
show('')
show('#5) what does this code do?')
print('Python is #1')
show('')
show('#6) fix the code')
def mystery(n):
    'Returns n cubed'
    return n**3
show('#6) mystery(3)=',mystery(3))
show('#6) the doc string = ',mystery.__doc__)
show('')
show('#7 find first and last character of a string')
def firstAndLast(s):
    'return the first and last char of s'
    #return s[0]+s[-1]
    return s[0]+s[len(s)-1]
show("#7) firstAndLast('Baldwins')=",firstAndLast('Baldwins'))
show('#7) the doc string = ',firstAndLast.__doc__)
show('')
show('#8) let us draw a triangle!')
def triangle(s):
    return 5*s+'\n '+3*s+'\n  '+s
show("#8) triangle('*')=",triangle('*'))