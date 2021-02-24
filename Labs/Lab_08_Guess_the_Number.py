# print('Lab 08: Guess The Number')


# import random

# number_of_guess = 0

# while number_of_guess < 10:

# # set a secret number using the randint() function in the random module
#     secret = random.randint(1, 10)

# # ask the user for a guess
#     guess = input('Please guess a number between 1 and 10: ')

# # convert guess to integer
#     guess = int(guess)

# # test conditions
#     if guess == secret:
#         number_of_guess += 1
#         print(f'WOW!!! You guessed the secret number: {secret}! You did it in {number_of_guess} tries')
#         print('Game Over')
#         break

#     elif guess < secret:
#         print(f'Try Again...', end = '')
#         print(f'Your guess {guess} was too low! The secret was {secret}')
   
#     elif guess > secret:
#         print('Try Again...', end = '')
#         print(f'Your guess {guess} was too high! The secret was {secret}')
   
#     number_of_guess += 1

# else:
#     number_of_guess = 10
#     print(f'After {number_of_guess} attempts...You\'re The BIGGEST LOSER!') 
#     print('GOODBYE!')

import random

while True:
    guesses = 1
    choice = random.randint(1, 10)
    user = None
    while user != choice:

        user = input("Pick a number between 1-10: ")

        while True:
            try:
                user = int(user)
                if user < 1 or user > 10:
                    raise Exception()
                break
            except:
                print("Invalid input")
                user = input("Pick a number between 1-10: ")


        if user < choice:
            guesses += 1
            print("Too low, try again.")
        else:
            guesses += 1
            print("Too high, guess again")
    else:
        print("You guessed correctly!")
        print(f"It took you {guesses} guesses.")

        play_again = input("Would you like to play again? ").lower()
        valid_choices = ["yes", "y", "yeah", "sure", "ok"]
        if play_again not in valid_choices:
            break
        
