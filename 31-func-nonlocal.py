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
     print('Change local y to',y) #这里y还是 3,因为局部变量y的作用域是 func_ouer
                                  #global 影响的是top level的变量

func_outer()
#print('value of x is',x)
print('value of y is',y)
