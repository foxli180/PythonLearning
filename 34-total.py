def total(initial=5,*numbers,**keywords): #initial 是global name 不能少,这个参数好像是固定的
     count = initial
     for number in numbers:
          count += number
     for key in keywords:
          count += keywords[key]
     return count

print(total(10,1,2,3,vegetables=50,fruits=100))
print(total())
