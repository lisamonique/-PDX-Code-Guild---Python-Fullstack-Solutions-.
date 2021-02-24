print('Lets Play ROCK🗿..PAPER📃..SCISSORS✂️')

while true

// # list of choice
let options = 'rock', 'paper', 'scissors'
# user makes a move
    player1_selection = input ('Make your Move... Rock? Paper? OR Scissors?')

    player2_selection = random.choice(options)

    print ('My turn! I choose...')

    print (player2_selection)

    if player1_selection == 'rock' and player2_selection == 'rock':
# all code in this block will be executed if the condition was true
        result = 'tie'
# perform another check if the if statement was false    
    elif player1_selection == 'rock' and player2_selection == 'paper':
        result = 'computer wins'    
    elif player1_selection == 'rock' and player2_selection == 'scissors':
        result = 'jalisa wins'
    elif player1_selection == 'paper' and player2_selection == 'rock':
        result = 'jalisa wins'
    elif player1_selection == 'paper' and player2_selection == 'paper':
        result = 'tie wins'
    elif player1_selection == 'paper' and player2_selection == 'scissors':
        result = 'computer wins'           
    elif player1_selection == 'scissors' and player2_selection == 'rock':
        result = 'computer wins'
    elif player1_selection == 'scissors' and player2_selection == 'paper':
        result = 'jalisa wins'
    elif player1_selection == 'scissors' and player2_selection == 'scissors':
        result = 'tie'    

    print(result)

# allow the user to choose whether they want to play again
    play_again = input('Would you like to play again? yes/no: ')

    valid_yes = ['y', 'yes', 'yep']
    valid_no = ['n', 'no', 'nope']
    valid_choices = valid_yes + valid_no

    while play_again not in valid_choices:
        print(f'You chose an invalid selection: {play_again}')
        play_again = input('Would you like to play again? yes/no: ')


    if play_again in valid_no:
        print('Goodbye!')
        break

    elif play_again in valid_yes:
        print('Okay, Lets Play')
    