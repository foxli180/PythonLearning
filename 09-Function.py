def sum(a,b):
    return a+b

func = sum

r=func(5,6)
print(r)

def add(a,b=2): #可以提供默认值
    m=a+b
    return m

r = add(1)
print (r)

r= add(1,5)
print (r)
