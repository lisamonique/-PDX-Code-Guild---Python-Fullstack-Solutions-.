print("Lab 18: ATM ")



# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

# ATM with class containing two attributes: (1) balance, (2) interest rate ###
# implement initializer #

balance = 0
interest_rate = 0.01
print_transaction = []

class ATM: 
    def __init__(self, balance, interest_rate, print_transaction): # this is the initializer
        self.balance = balance   # 1st 'attribute' or 'member variables'
        self.interest_rate = interest_rate   # 2nd 'attribute' or 'member variables'    
        self.print_transaction = print_transaction   # create empty list to maintain transactions

        # implement folllowing functions; which are called: 'member functions' or 'method' 
    def balance(self):   # returns the account balance
        return self.balance

    def deposit(self, amount):   # deposits the given amount in the account
        self.balance += amount
        self.print_transaction.append(f'user deposited ${amount}')

    def check_withdrawal(self, amount):   # returns true if the withdrawn amount won't put the account in the negative
        if self.balance > 0:
            return True
        

    def withdraw(self, amount):  # withdraws the amount from the account and returns it
        self.balance -= amount
        self.print_transaction.append(f'user withdrew ${amount}')

    def calc_interest(self): # returns the amount of interest calculated on the account
        interest = self.balance * self.interest_rate
        return interest

    def print_transactions(self):   # print out the list of user transactions
       self.print_transaction


print('Welcome to the ATM')

atm = ATM(balance, interest_rate, print_transaction) # create an instance of our class
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transaction':
        for history in atm.print_transaction:
            print(history)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transaction - print transaction history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

'''
### Version 2 ###

# Have the ATM maintain a list of transactions.
# Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'.
# Add a new method `print_transactions()` to your class for printing out the list of transactions.

'''

