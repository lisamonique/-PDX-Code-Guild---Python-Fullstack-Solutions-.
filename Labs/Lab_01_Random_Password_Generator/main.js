// ('Lab 01: Random Password Generator')

// # list of characters
let letters = string.ascii_letters
let digits = string.digits
let symbols = string.punctuation

// # user enters value 
let password_length = prompt('How many characters would you like in your password?: ')

let password_characters = ''

// # generate random password and convert to string
for i in range(password_length)
    
    password = random.choice(letters + digits + symbols)

    password_characters += password

// # print password created
alert(password_characters)

