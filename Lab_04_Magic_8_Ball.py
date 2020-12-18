
import random

while True:
   
    print('Welcome to the Amazing 8 Ball')

    predictions = ['It is certain!', 'As I see it, YES!', 'Most Likely!', 'Ask again later!', 'My reply is NO!']

    question = input('Ask me any question your HeART DesirEs...')

    random_prediction = random.choice(predictions)

    print('Searching my MaGiC GLoBe...')

    print(random_prediction)

    question = input('Would you like to ask another question?!? yes or no')

    valid_yes = ['yes']
    valid_no = ['no']
    valid_choices = valid_yes + valid_no

    while question not in valid_choices:
        print(f'You chose an invalid selection: {question}')
        question = input('Would you like to ask another question?!? yes or no')

    if question in valid_no:
        print('Goodbye!')
        break

    elif question in valid_yes:
        print('Next Question, Please!')    