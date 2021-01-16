print('Lab 17: Quote API')

import requests
import json


### VERSION 1 ###

response = requests.get("https://favqs.com/api/qotd")

quote = json.loads(response.text)

print(quote["quote"]["author"])
print(quote["quote"]["body"])



### Version 2 ###

while True:

    page = 1
    quotes = 0

    # Prompt the user for a keyword
    key_word = input('Enter a keyword to search for quotes: ')

    # string concatenation to build the URL
    url = 'https://favqs.com/api/quotes?page=' + str(page) + '&filter=' + key_word

    # API endpoint requires an API key be included in a request header
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} 

    # parse the JSON in the response into a python dictionary
    response = requests.get(url, headers=headers)
    quotes_return = json.loads(response.text)
 
    for quote in quotes_return:
        if quotes <= 25:
            print(quotes_return['quotes'][quotes]['body'])
            print(quotes_return['quotes'][quotes]['author'])
            quotes += 1


### Code that asks user to repeat question ###
    
    # allow the user to choose whether they want to continue
    play_again = input("Do you want to see the next page of results? 'Next' or 'Done' ")

    valid_yes = ['next', 'Next', 'next page', 'Next Page']
    valid_no = ['done', 'Done', 'finish']
    valid_choices = valid_yes + valid_no

    if play_again in valid_no:
        print('Til Next Time!')
        break

    elif play_again in valid_yes:
        page += 1
    
    else:   
        break