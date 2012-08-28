while True:
     s = input('Enter sth:')
     if s == 'quite':
          break
     if len(s) < 3:
          print ('Too small')
          continue

     print('Input is of sufficient length!')
