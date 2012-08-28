x = 50

def func():
     global x  #x成为了全局变量,对它的修改对全局生效

     print ('x is',x)
     x=2
     print ('change global x to',x)

func()
print('Value of x is',x)
