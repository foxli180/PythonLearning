def total (initial = 5,*numbers, vegetables):
     count=initial
     for number in numbers:
          count += number
     count += vegetables
     return count

print(total(10,1,2,3,vegetables=50))#这里必须制定 vegetables 的值
#print(total(10,1,2,3)) #否则这里会报错
