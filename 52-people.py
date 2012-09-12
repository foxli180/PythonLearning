people = {
     'Fox':{
          'phone':'2314',
          'addr':'whu'
          },
     'Beth':{
          'phone':'1234',
          'addr':'end'
          },
     'Cecil':{
          'phone':'3518',
          'addr':'dsadsa'
          }
     }
labels ={
     'phone':'phone number',
     'addr':'address'
     }

name = input('Name: ')
request = input('phone number(p) or address(a)? ')

if request=='p':key='phone'
if request=='a':key='addr'

if name in people:print("%s's %s is %s" %\
                        (name,labels.get(key),people.get(name).get(key)))
