number = 3
play = 1 
points = 1000
level_user = input('Choose a level: easy, medium or hard: \n')
print('You chose {}'.format(level_user))

if(level_user == 'easy'):
    number_of_guesses = 20
elif(level_user == 'medium'):
    number_of_guesses = 10
elif(level_user == 'hard'):
    number_of_guesses = 5

for play in range(1, number_of_guesses + 1):
    print('Guess {} of {}'.format(play, number_of_guesses))
    guess = int(input('I am thinking of a number. What is it?  \n'))
    print('You entered: {}'.format(guess))

    right = guess == number
    higher = guess > number
    lower = guess < number

    if(right):
        print('You guessed it!')
        break
    elif(higher):
        print('Too high!')
    elif(lower):
        print('Too low!')

    points_losses = abs(number - guess)
    points = points - points_losses

    print('You have {} points.'.format(points))

    if(play == number_of_guesses):
        print('You ran out of guesses. The number was {}'.format(number))

print('End of the game')


