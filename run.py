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
            print(f"Welcome {name_data} \n")
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


def menu():
    print("Main Menu: \n")
    print("1. Instructions")
    print("2. Start Game")
    print("3. Exit \n")

    while True:
        player_choice = input("Please choose from the above menu: ")

        if player_choice == '1':
            instructions()
        elif player_choice == '2':
            print('Ola')
        elif player_choice == '3':
            print('Exit function')
        else:
            print("Ooops, Please choose a valid option from the menu!")
            

def instructions():
    """
    This option shows the user the basic game instructions
    """
    print(
        "\n"
        "How to Play: \n\n"
        "The aim is to make the correct word by guessing "
        "the letters one at a time. \n\n1. To guess, "
        "type a letter of your choice and hit enter. \n2. If you "
        "are right the letter will appear on screen. \n3. If you "
        "are wrong the hangman will start to appear. \n4. You have "
        "6 attempts to guess correctly or its Game Over!! "
    )

get_name()
menu()