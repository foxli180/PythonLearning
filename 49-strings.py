website = 'http://www.baidu.com'
print (website)
# website[-3:] = 'org' #这里会报错,string 应该是被当成了 元组而不是序列
y = list (website) #转化为序列
y[-3:] ='org'
print (y)
y = tuple(y) #再转化为元组
print (y)
print (website) # y =list(website) 和y =website 不一样,前者应该是创建新的内存空间,后者应该是指向同一片内存空间

for item in y:
    print(item, end='')
