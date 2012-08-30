#printMax.__doc__ 可以打印 ''' 内的注释内容,
def printMax(x,y):
     '''prints the maximum of two numbers.

     the two values must be integers.'''

     x=int(x) #conver to integers ,if possible
     y=int(y)

     if x>y:
          print(x,'is the maxmum')
     elif x==y:
          print(x,'is equal to',y)
     else:
          print(y,'is the maxmum')


printMax(3,5)
printMax(3,3)
#printMax(a,b)
print(printMax.__doc__)
