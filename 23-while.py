number = 23
running = True

while running:
    guess = int(input('Enter an integar:'))

    if guess == number:
        print('you get it! con~')
        running = False
    elif guess < number:
        print('No, it is a little higher than that!')
    else:
        print('No, it is a little lower than that!')

else:
    print ('End of while loop')


print ('Done')
