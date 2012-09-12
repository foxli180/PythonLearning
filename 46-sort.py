numbers = [5,2,9,7]
x = ['abc','ab','a']
y = numbers
numbers.sort()
print (numbers)
x.sort(key=len)
print (x)
y.sort(reverse=True)
print (y)
print (numbers)
print (x)
