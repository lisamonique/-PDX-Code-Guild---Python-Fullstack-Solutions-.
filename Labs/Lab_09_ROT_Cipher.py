print('Lab 09: ROT Cipher')


cipher = {
    'a': '0',
    'b': '1',
    'c': '2',
    'd': '3',
    'e': '4',
    'f': '5',
    'g': '6',
    'h': '7',
    'i': '8',
    'j': '9',
    'k': '10',
    'l': '11',
    'm': '12',
    'n': '13',
    'o': '14',
    'p': '15',
    'q': '16',
    'r': '17',
    's': '18',
    't': '19',
    'u': '20',
    'v': '21',
    'w': '22',
    'x': '23',
    'y': '24',
    'z': '25',
},{
    'a': '0',
    'b': '1',
    'c': '2',
    'd': '3',
    'e': '4',
    'f': '5',
    'g': '6',
    'h': '7',
    'i': '8',
    'j': '9',
    'k': '10',
    'l': '11',
    'm': '12',
    'n': '13',
    'o': '14',
    'p': '15',
    'q': '16',
    'r': '17',
    's': '18',
    't': '19',
    'u': '20',
    'v': '21',
    'w': '22',
    'x': '23',
    'y': '24',
    'z': '25',  
}

'''
while True:

# request prompt from user
    statement = input('Give me a Phrase:')

# return user input into string
    phrase = (list(statement))

    for phrase in cipher:
        print(cipher.get(phrase), end = '')

    else:
        break    

# get character at given index
#statement = ''
#print(''[0])
#---------------------------#
#if statement in cipher:
#print(ord())
#print(phrase)
'''

statement = input('Give me a Phrase:')
phrase = (list(statement))
print(cipher[phrase], end = '')