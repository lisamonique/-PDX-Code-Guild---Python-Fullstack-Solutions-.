print('Lab 12: Blackjack Advice')

import random


cards = {
    'A': 1,
    'J': 10,
    'Q': 10,
    'K': 10,
}

# print welcome message with instructions and card options
print('Choose any of these 3 cards: (2, 3, 4, 5, 6, 7, 8, 9, 10, A, J, Q, or K)')

# ask the user for three playing cards
card_one = input("What's your first card? ").upper()
card_two = input("What's your second card? ").upper()
card_three = input("What's your third card? ").upper()


# point value of each card individually
def point_value(card):
    if card == 'A':
        return 1
    elif card == 'J' or card == 'Q' or card == 'K':
        return 10
    return int(card)


# value of all cards added together
total = point_value(card_one) + point_value(card_two) + point_value(card_three)


# if elif else conditionals to determine the advice
if total == 21:
    print(f"{total}: BLACKJACK")
elif total < 17:
    print(f"{total}: I'd advise you to 'Hit' ")
elif total < 21: 
    print(f"{total}: I'd advise you to 'Stay' ")
else:
    print("Already Busted")
