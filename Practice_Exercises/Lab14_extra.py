print("Lab 14: Number to Phrase")

'''

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

    hundreds_digits = number//100
    tens_digit = number//10
    ones_digit = number%10
    
    if number in hundreds_group:  ##### WORKS ####
        print('We made it') 
        print(hundreds_group[number])   

    elif number in ones_group:   ##### WORKS ####
        print('it works!!')
        print(ones_group[number])

    elif ones_digit == 0:    ##### WORKS #####    
        print('halleuyah')
        print(tens_group[number])       
    
    if tens_digit == 7:
        print('silly')
        print(tens_group[tens_digit] + '-' + ones_group[ones_digit]) 

'''

import random


#           0       1      2       3       4       5      6        7        8       9
ones =  ["zero", "one",     "two",   "three",     "four",     "five",    "six",    "seven",     "eight",     "nine",
"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# number = 20 #random.randint(0, 99)# input("Enter a number from 0-99: ")

def number_to_phrase(number):
    if number < 20:
        return f"{number}: {ones[number]}"
    elif number < 100:
        tens_digit = number // 10
        ones_digit = number % 10
        if ones_digit:
            return f"{number}: {tens[tens_digit]}-{ones[ones_digit]}"
        else:
            return f"{number}: {tens[tens_digit]}"
    elif number < 1000:
        hundreds_digit = number // 100
        tens_digit = number % 100 // 10
        ones_digit = number % 10
        under_twenty = number % 100
        if 0 < under_twenty < 20:
            return f"{number}: {ones[hundreds_digit]} hundred and {ones[under_twenty]}"
        elif ones_digit and tens_digit:
            return f"{number}: {ones[hundreds_digit]} hundred and {tens[tens_digit]}-{ones[ones_digit]}"
        elif ones_digit:
            return f"{number}: {ones[hundreds_digit]} hundred and {ones[ones_digit]}"
        elif tens_digit:
            return f"{number}: {ones[hundreds_digit]} hundred and {tens[tens_digit]}"
        else:
            return f"{number}: {ones[hundreds_digit]} hundred"



for i in range(900, 920):
    print(number_to_phrase(i))