database = [
     ['albert','1234'],
     ['dibert','4343'],
     ['smith' ,'5678'],
     ['fox'   ,'2234']
     ]
username = input('UserName: ')
password = input('Password: ')

if [username,password] in database:
     print('Access Granted')
else:
     print('Access Failed')
