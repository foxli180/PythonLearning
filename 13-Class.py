class Base:
    def __init__(self):#这里的下划线是两个_
        self.data=[]
    def add(self,x):
        self.data.append(x)
    def addtwice(self,x):
        self.add(x)
        self.add(x)

class Child(Base):
    def plus(self,a,b):
        return a+b

oChild=Child()
oChild.add("str1")
oChild.addtwice("str1")
print (oChild.data)
print (oChild.plus(2,3))

