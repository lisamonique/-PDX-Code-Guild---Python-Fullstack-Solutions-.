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
    2:'twenty',
    3:'thirty',
    4:'fourty', 
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety',
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

    hundreds_digits = number // 100
    tens_digit = number // 10
    ones_digit = number % 10
    

    if number in hundreds_group: 
       print(hundreds_group[number])   

    elif number <= 19: 
        print(ones_group[number])


    elif ones_digit != 0: 
        if number <= 99 and number >= 21:
            print(tens_group[tens_digit] + '-' + ones_group[ones_digit]) 


    elif ones_digit == 0: 
        print(tens_group[tens_digit])    

  