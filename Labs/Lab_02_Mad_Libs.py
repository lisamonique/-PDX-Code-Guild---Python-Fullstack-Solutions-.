print('Mad Libs Lab')

# collect user inputs

adjective = input("enter a adjective: ")
adjective_1 = input("enter a adjective_1: ")
adjective_2 = input("enter a adjective_2: ")
verb_end_ing = input("enter a verb_end_ing: ")
verb_end_ing_1 = input("enter a verb_end_ing_1: ")
verb_end_ing_2 = input("enter a verb_end_ing_2: ")
verb_end_ing_3 = input("enter a verb_end_ing_3: ")
noun = input("enter a noun: ")
noun_1 = input("enter a noun_1: ")
noun_2 = input("enter a noun_2: ")
plural_noun = input("enter a plural_noun: ")
plural_noun_1 = input("enter a plural_noun_1: ")
plural_noun_2 = input("enter a plural_noun_2: ")
plural_noun_3 = input("enter a plural_noun_3: ")
part_of_the_body = input("enter a part_of_the_body: ")
game = input("enter a game: ")
place = input("enter a place: ")
place_1 = input("enter a place_1: ")
place_2 = input("enter a place_2: ")
place_3 = input("enter a place_3: ")
plant = input("enter a plant: ")
number = input("enter a number: ")

# multi-line f-string

output = f"""
 
A vacation is when you take a trip to some {adjective} {place} with your {adjective_1} family."

Usually you go to some {place_1} that is near a {noun} or up on a {noun_1}."

A good vacation at {place_2} is one where you can ride {plural_noun} or play {game} or go hunting for {plural_noun_1}."

I like to spend my time {verb_end_ing_1} or {verb_end_ing}."

When parents go on a vacation, they spend their time eating three {plural_noun_2} a day, and fathers play golf, and mothers sit around {verb_end_ing_3}."

Last summer, my little brother fell in a {noun_2} and got poison {plant} all over his {part_of_the_body}."

My family is going to go to {place_3}, and I will practice {verb_end_ing_2}."

Parents need vacations more than kids because parents are always very {adjective_2} and because they have to work {number} hours every day all year making enough {plural_noun_3} to pay for the vacation."
"""

print(output)