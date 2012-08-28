number = 23
guess = int(input('Enter a number:'))


if guess == number:
    print('Conguratulations, u guessed it')
    print('(but no prizes! )')
elif guess < number:
    print ('No,it is a lttle higher than that')
else:
    print ('no, it is a little lower than that')

print ('Done')
