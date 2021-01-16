print('Lab 09: ROT Cipher')

# create dictionary for each character and its corresponding character
cipher = {
    'a': 'n',
    'b': 'o',
    'c': 'p',
    'd': 'q',
    'e': 'r',
    'f': 's',
    'g': 't',
    'h': 'u',
    'i': 'v',
    'j': 'w',
    'k': 'x',
    'l': 'y',
    'm': 'z',
    'n': 'a',
    'o': 'b',
    'p': 'c',
    'q': 'd',
    'r': 'e',
    's': 'f',
    't': 'g',
    'u': 'h',
    'v': 'i',
    'w': 'j',
    'x': 'k',
    'y': 'l',
    'z': 'm',
}

### VERSION 1 ###

# request prompt from user
statement = input('Give me a Phrase: ')


# loop through the character of string entered by user
character = ''
for char in statement:
    if char in cipher:
       character += cipher[char]     

# print result
print(f'{statement} to {character}')

