print('Lab 11: Make Change')

print('Welcome to the Change Maker 5000 (tm)')

'''
while True:

# user input
    dollar = int(input('Enter a dollar amount:'))

    penny = dollar//.01
    nickel = dollar//.05
    dime = dollar//.10
    quarter = dollar//.25
    half_dollar = dollar//.50

    # user input
    #change = int(input('Would you like to make more change:'))

    dollar = float(dollar)

    total = dollar

    print({nickel})
    print({nickel})
    print({nickel})

    print('Thanks for the Business!')
'''
'''
# allow the user to choose whether they want to play again
    more_change = input('Would you like to play again? yes/no: ')

    valid_yes = ['y', 'yes', 'yep']
    valid_no = ['n', 'no', 'nope']
    valid_choices = valid_yes + valid_no

    while more_change not in valid_choices:
        print(f'You chose an invalid selection: {more_change}')
        more_change = input('Would you like to play again? yes/no: ')


    if more_change in valid_no:
        print('Goodbye!')
        break

    elif more_change in valid_yes:
        print('Okay, Lets Play')

#----------------------------------------------------------------------------#

### Version 2 ###
'''

'''
coins = [
    ('half-dollar', 50)
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
'''



def combine(nums1, nums2):
    
    num for num1 in (num1,num2) for num in num2

print(combine) # ['a', 1, 'b', 2, 'c', 3]