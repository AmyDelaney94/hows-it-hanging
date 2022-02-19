# from pprint import pprint


def get_name():
    """
    Welcome message and get name from user
    """
    print("************************")
    print("       Hangman")
    print("Guess the word to win!")
    print("************************\n")

    while True:
        name_data = input("Enter your name here: ")

        if validate_data(name_data):
            print(f"Welcome {name_data}")
            break


def validate_data(name):
    """
    Validates user input for name
    """
    try:
        if name == "":
            raise ValueError("Please input a name \n")

    except ValueError as error:
        print(f"Try again. {error}")
        return False

    return True


get_name()

def menu():
    print('{:*70}'.format("Main Menu: \n"))
    print('{:*70}'.format('1. Instructions '))
    print('{:*70}'.format('2. Start Game '))
    print('{:*70}'.format('3. Exit '))

while True:
        player_choice = input("Please choose from the above menu: ")

        if player_choice == '1':
            instructions()
        elif player_choice == '2':
            # Game function here!
        elif player_choice == '3':
            # Exit function
        else:
            print('{:*70}'.format(' Please choose a valid option from the menu! '))


def instructions():
    """
    This option shows the user the basic game instructions
    """
    print(
        "To play Hangman, you need to guess the letters one "
        "at a time, to make the correct word. \n To guess "
        "type a letter of your choice and hit enter. \n If you "
        "are right the letter will appear on screen, but if you "
        "are wrong the hangman will start to appear. \n You have "
        "6 attempts to guess correctly or its Game Over!! "
    )

