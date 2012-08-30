from mymodule import sayhi,__version__
#from mymodule import * #这里使用 * 不会导入__version__(可以理解为双下划线开头的变量是private的)

sayhi()# 如果指定了导入的function 那可以直接调用function 而不需要module 名
print('Version',__version__)
