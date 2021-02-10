// ('Lab 01: Random Password Generator')

// import random
// import string

// # list of characters
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

// # user enters value 
let password_length = prompt('How many characters would you like in your password?: ')

password_characters = ''

// # generate random password and convert to string
for i in range(password_length):
    
    password = random.choice(letters + digits + symbols)

    password_characters += password

// # print password created
alert(password_characters)


// Grading Lab w/ JavaScript

let grade = prompt("Enter you grade.")

if (grade >= 90 && grade <= 100){
    alert("You got an A")
}

else if (grade >= 80 && grade < 90){
    alert("You got an B")
}

else if (grade >= 70 && grade < 80){
    alert("You got a C")
}

else if (grade >= 60 && grade < 70){
    alert("You got a D")
}

else{
    alert("You got a F")
}

