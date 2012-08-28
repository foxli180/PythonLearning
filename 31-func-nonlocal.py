def func_outer():
     x = 2
     y = 3
     print ('x is',x)
     print ('y is',y)
     
     def func_inner():
          nonlocal x #介于 local 和 global 之间,
          global y
          x = 5
          y = 5

     func_inner()
     print('Change local x to',x)
     print('Change local y to',y)

func_outer()
#print('value of x is',x)
print('value of y is',y)
