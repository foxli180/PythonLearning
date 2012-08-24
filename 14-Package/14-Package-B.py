#包B 引用 A
from A import add_func
#或者 import 14-Package-A

print ("Import add_func from module 14-Package-A")
print ("Result of 1 plus 2 is: ")
print (add_func(1,2))
