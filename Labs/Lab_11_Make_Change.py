print('Lab 11: Make Change')

### Version 1 ###

print('Welcome to the Change Maker 5000 (tm)')

while True:

    dollar = float(input('Enter a dollar amount: $'))

    quarters = dollar//.25
    dollar %= .25
    dimes = dollar//.10
    dollar %= .10
    nickels = dollar//.05
    dollar %= .05
    pennies = dollar//.01
    
    print(f'Your change is {quarters} quarter(s), {dimes} dime(s), {nickels} nickle(s), {pennies} penny(ies).')
    
    # allow the user to choose whether they want to play again
    play_again = input('Would you like to make more change? yes/no: ')

    valid_yes = ['y', 'yes', 'yep']
    valid_no = ['n', 'no', 'nope']
    valid_choices = valid_yes + valid_no

    while play_again not in valid_choices:
        print(f'You chose an invalid selection: {play_again}')
        play_again = input('Would you like to make more change? yes/no: ')

    if play_again in valid_no:
        print('Thanks for the Business!!')
        break

    elif play_again in valid_yes:
        continue

#----------------------------------------------------------------------------#