word = ['a','b','c','d','e','f','g']
a = word[2]
print ("a is: "+a)
b = word[1:3]
print ("b is: ")
print (b)
c =word [:2]
print ("c is: ")
print (c)
d = word[0:]
print ("d is: ")
print (d)
#print ("d is: "+d) #error can not convert list to str

#合并
e = word[:2]+word[2:]
print ("e is: ")
print (e)
f = word[-1] #the last elements
print ("f is: "+f)
g = word[-4:-2]
print ("g is: ")
print (g)
l = len(word)
print ("Length of word is: "+ str(l))
#add new element
print ("add new element")
word.append('h')
print (word)

#delete element
del word[0]
print (word)
del word[1:3]
print (word)


