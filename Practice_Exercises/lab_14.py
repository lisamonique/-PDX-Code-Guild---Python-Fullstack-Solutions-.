import random

'''
ones = ['one', 'two','three']

number = random.randint(0,3) # input('Enter a number please')

if number < 10:
print(f'{number}: {ones[number]}')

elif number < 19:
    x = number - 10
    print(f'{number}: {teens[x]}')

    

'''


print("Lab 14: Number to Phrase")

hundreds_group = {
    100:'one-hundred',
    200:'two-hundred',
    300:'three-hundred',
    400:'four-hundred',
    500:'five-hundred',
    600:'six-hundred',
    700:'seven-hundred',
    800:'eight-hundred',
    900:'nine-hundred'
}

tens_group = {
    20:'twenty',
    30:'thirty',
    40:'fourty', 
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
}

ones_group = {
    0:'zero',
    1:'one',
    2:'two',
    3:'three',
    4:'four', 
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
}

while True:

    number = int(input('Enter a number: '))

    tens_digit = number//10
    ones_digit = number%10

    if number in hundreds_group:
        print('We made it') 
        print(hundreds_group[number])   

    elif number in tens_group:
        print('tens work')
        print(tens_group[number])   

       
    elif number in ones_group:
        print('it work!!')
        print(ones_group[number])   

    elif ones_digit <= 99:
        print('silly')
        print(tens_group[tens_digit] + '-' + ones_group[ones_digit])  

