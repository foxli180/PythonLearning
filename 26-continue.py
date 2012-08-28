while True:
     s = input('Enter sth:')
     if s == 'quite':
          break
     if len(s) < 3:
          print ('Too small')
          continue # continue 会跳过之后的语句只有输入大于2个字符的时候才会打印下面语句

     print('Input is of sufficient length!')
