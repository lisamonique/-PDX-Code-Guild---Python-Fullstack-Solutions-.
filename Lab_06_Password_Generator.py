print('Lab 06: Password Generator')

import random
import string

# list of characters
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# user enters value 
# convert to integar
password_length = int(input('How many characters would you like in your password?: '))


password_characters = ''

for i in range(password_length):
    
    password = random.choice(letters + digits + symbols)

    password_characters += password


print(password_characters)

