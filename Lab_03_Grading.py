print ('Lab 03: Grading')

'''
Numeric Ranges

A = 90 thru 100
B = 80 thru 89
C = 70 thru 79
D = 60 thru 69
F = 00 thru 59

'''

# ask the user for a number
number = input('Please enter a whole number: ')

# convert number to an integar
number = int(number)

if number >= 95:
# all code in this block will be executed if the condition was true
    result = 'A+'
elif 94 >= number >= 90:
    result = 'A'    
elif 89 >= number >= 85:
    result = 'B+'    
elif 84 >= number >= 80: 
    result = 'B'
elif 79 >= number >= 75:
    result = 'C+'    
elif 74 >= number >= 70:
    result = 'C'
elif 69 >= number >= 65:
    result = 'D+' 
elif 64 >= number >= 60:
    result = 'D'
else:
# if all other conditions are False,
# run the else block
    result = 'F'

print(result)


