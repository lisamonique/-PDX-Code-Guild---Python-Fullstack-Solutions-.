print('Lab 05: Random Emoticon Generator')

'''
#### Lab Instructions ####

Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\. You can view a long list on wikipedia.

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Use concatenation to combine them and display the emoticon

Example output:
:-P

Version 2
Use a while loop to generate 5 emoticons.

Version 3
Randomly generate vertical emoticons like ^_^ (-_-), [*.*]
'''



import random

# Define a list of eyes
eyes = [':', '8', ';', '=', 'B']

# Define a list of noses
noses = ['-', '.', '>']

# Define a list of mouths
mouths = ['D', ')', '(', ']']


# Use a while loop to generate 5 emoticons
i = 0
while i < 5:
    i += 1

# Randomly pick a set of eyes, noses, and mouths    
    random_eyes = random.choice(eyes)

    random_noses = random.choice(noses)

    random_mouths = random.choice(mouths)

# Use concatenation to combine features and display the emoticon
    face = random_eyes + random_noses + random_mouths

# generate vertical emoticons
    print(face, end=' ')

