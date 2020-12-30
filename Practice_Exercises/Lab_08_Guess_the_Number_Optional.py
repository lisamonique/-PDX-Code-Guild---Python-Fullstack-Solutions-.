print('Lab 08: Guess The Number')

import random

number_of_guess = 0

# set a secret number using the randint() function in the random module
secret = random.randint(1, 10)

while number_of_guess < 10: 

# ask the user for a guess
# convert guess to integer

    guess = int(input('Please guess a number between 1 and 10: '))

    error = ['Tsk Tsk, Someone didn\'t read the instructions...', 'Are you even paying ATTENTION...', 'Read the question SLOWLY...']
    wrong_guess = random.choice(error)

# test conditions   

    if guess == secret:
        number_of_guess += 1
        print(f'WOW!!! You guessed the secret number: {secret}! You did it in {number_of_guess} tries')
        print('Game Over')
        break

    elif guess > 10:
        print (wrong_guess)

    elif guess < secret:
        print(f'Try Again...', end = '')
        print(f'Your guess {guess} was too low!')
        
    elif guess > secret:
        print('Try Again...', end = '')
        print(f'Your guess {guess} was too high!')
 
    number_of_guess += 1

else:
    #number_of_guess = 10
    #print(f'After {number_of_guess} attempts...You\'re The BIGGEST LOSER!') 
    #print('GOODBYE!')
    

    play_again = input('Would you like to play again?')
    valid_choices = ['yes', 'yeah', 'y', 'okay', 'sure']
    if play_again not in valid_choices:
        print('see ya later')