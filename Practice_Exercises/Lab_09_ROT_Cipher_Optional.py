print('Lab 09: ROT Cipher')


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


# request prompt from user
statement = input('Give me a Phrase:')

# return user input into string
phrase = (list(statement))

character = ''

for char in phrase:
    #word = char in statement
    if char in character:
        print(char)
        #character += (statement[phrase])
        #print(statement[phrase], end = '')
        #print(f'{statement} to {character}')
'''
    else:
        character += phrase
        print(character)
'''


'''
#---------------------------------#
# get character at given index
#statement = ''
#print(''[0])
#---------------------------#
#if statement in cipher:
#print(ord())
#print(phrase)
# get -13 for each letter
#-------------------------------------#

statement = input('Give me a Phrase:')
phrase = (list(statement))
print(cipher[phrase], end = '')
#----------------------------------#
'''