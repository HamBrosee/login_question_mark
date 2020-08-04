# Ask for username and password or create a new acc
import sys


def loop():
    print('Welcome to Butt Bangerz INC, what would you like to do today? Login or Register.')

    if str.lower(input()) == 'login':
        userName = input('What is your username?\n')
        if userName == 'Assblaster9000':
            password = input('What is your password?\n')
            if password == 'bigbootybitches666':
                print(f'Welcome, {userName}')
                sys.exit()

        else:
            print(f'I\'m sorry, the username {userName} is not on file, please try again.')

    else:
        newUserName = input('What would you like to register a new account? What would you like as your username? \n')
        if str.lower(newUserName) != 'assblaster9000':
            response = input(f'You\'ve selected {newUserName} as your username, is this to your liking?\n')
            if response == 'yes':
                newPassWord = input('What would you like your password to be?\n')
                if newPassWord == newPassWord:
                    print(f'Thank you for registering {newUserName}, your password is {newPassWord}. Don\'t forget it!')
                    sys.exit()
        else:
            print('Please enter a username that isn\'t in use!')




    return loop()


loop()
