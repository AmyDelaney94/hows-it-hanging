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
