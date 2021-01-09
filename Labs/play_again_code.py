    ### Code that asks user to repeat question ###
    
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