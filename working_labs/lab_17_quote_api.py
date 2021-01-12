print('Lab 17: Quote API')

import requests
import json

### VERSION 1 ###

response = requests.get("https://favqs.com/api/qotd")

data = json.loads(response.text)

for qotd in data:
    print(str(data["quote"]["author"]))
    print(str(data["quote"]["body"]))

### Version 2 ###

while True:
   

    key_word = input('Enter a keyword to search for quotes: ')





    # allow the user to choose whether they want to play again
    play_again = input("enter 'next page' or 'done': ")

    valid_yes = ['next page']
    valid_no = ['done']
    valid_choices = valid_yes + valid_no

    while play_again not in valid_choices:
        print(f'You chose an invalid selection: {play_again}')
        play_again = input("enter 'next page' or 'done': ")

    if play_again in valid_no:
        continue

    #elif play_again in valid_yes:
        #### continue with next <list of quotes> ####