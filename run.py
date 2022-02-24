"""
This section contains all imports
"""
import os
import sys
import random
from words import easy_selection
from words import hard_selection


def get_name():
    """
    Welcome message and get name from user
    """
    print("************************")
    print("       Hangman")
    print("Guess the word to win!")
    print("************************\n")

    while True:
        name_data = input("\033[0;36mEnter your name here: ")

        if validate_data(name_data):
            print(f"Welcome {name_data} \n")
            break


def validate_data(name):
    """
    Validates user input for name
    """
    try:
        if name == "":
            raise ValueError("\033[0;31mPlease input a name \n")

    except ValueError as error:
        print(f"\033[0;31mTry again. {error}")
        return False

    return True


def menu():
    """
    Function for games main menu.
    """
    print("\033[0mMain Menu: \n")
    print("1. Instructions")
    print("2. Start Game")
    print("3. Exit \n")

    while True:
        player_choice = input("\033[0;36mPlease choose from the above menu: ")

        if player_choice == '1':
            instructions()
        elif player_choice == '2':
            choose_word()
        elif player_choice == '3':
            exit()
        else:
            print("\033[0;31mOops,Please choose a valid option from the menu!")


def instructions():
    """
    This option shows the user the basic game instructions
    """
    print(
        "\n"
        "\033[0;32mHow to Play: \n\n"
        "The aim is to make the correct word by guessing "
        "the letters one at a time. \n\n1. To guess, "
        "type a letter of your choice and hit enter. \n2. If you "
        "are right the letter will appear on screen. \n3. If you "
        "are wrong the hangman will start to appear. \n4. You have "
        "6 attempts to guess correctly or its Game Over!! "
    )
    # Give option to play or return to menu.
    print("\033[0;36mAre you ready to play Hangman? \n")

    # Test for valid selection made
    while True:
        lets_go = input("Press 1 for Yes or 2 for No: ")

        if lets_go == '1':
            choose_word()
        elif lets_go == '2':
            menu()
        else:
            print("\033[0;31mPlease make a valid choice.")


def exit():
    """
    Exit game function
    """
    print("\033[0;36mThanks for playing How's it Hanging Goodbye!")
    sys.exit()


def choose_word():
    """
    Generates a random word from the easy or hard selection lists.
    """
    # level_selection = input("\033[0;36mPlease choose a difficulty level: \n")
    # Test for valid selection made
    while True:
        difficulty = input("\033[0;36mPress 1 for Easy and 2 for Hard: ")

        if difficulty == '1':
            word = random.choice(easy_selection)
            start_game(word)
        elif difficulty == '2':
            word = random.choice(hard_selection)
            start_game(word)
        else:
            print("\033[0;31mPlease make a valid choice.")


def start_game(word):
    """
    Using words from words.py, choose a random word
    and promt the user to guess letters.
    """
    attempts = 6
    letters = set(word)
    guesses = []
    # If no turns left shows right answer
    while attempts > 0 and len(letters) > 0:
        show_answer = [
            letters if letters in guesses else "_" for letters in word
        ]
        print(hangman_status(attempts))
        print("\n")
        print(" ".join(show_answer))
        # ask player to take their turn
        # .upper used to capitalise letters to match word lists
        players_turn = input(
            "\033[0mPlease choose a letter:\n").upper().strip()
        # clear terminal
        os.system("cls" if os.name == "nt" else "clear")
        # Test for valid selection made
        if players_turn in guesses:
            print("\033[1;31mOops you already guessed ", players_turn, "\n")
            print("You have used these letters: ")
            print(" ".join(guesses))
        elif len(players_turn) != 1:
            print(
                "\033[1;31mOops please only enter one guess at a time\n"
            )
            print("You have used these letters: ")
            print(" ".join(guesses))
        elif not players_turn.isalpha():
            print("\033[1;31mOops ", players_turn, " is not a letter\n")
            print("You have used these letters: ")
            print(" ".join(guesses))
        elif players_turn not in word:
            print("\033[1;31mAwh try again,", players_turn, "is not right")
            attempts -= 1
            print("\033[0mAttempts Remaining: ", attempts)
            guesses.append(players_turn)
            print("\033[0mYou have used these letters: ")
            print(" ".join(guesses))
        else:
            print("\033[0;32mWOO you got it! \n")
            guesses.append(players_turn)
            print("\033[0mYou have used these letters: ")
            print(" ".join(guesses))
            if players_turn in letters:
                letters.remove(players_turn)
            else:
                print("\033[0;31mPlease make a valid choice.")

        if attempts == 0:
            # No more attempts left.
            print("\033[0mAttempts Remaining: ", attempts)
            guesses.append(players_turn)
            print("\033[0;31mAwh you lose!")

    # Ask user if they want to play again
    print("The correct word was", word, "\n")
    print("\033[0;36mWould you like to play again?")
    play_again()


def play_again():
    """
    Function to allow player to play again or exit to the menu.
    """
    while True:
        go_again = input("Press 1 for Yes or 2 for No: ")

        if go_again == '1':
            choose_word()
        elif go_again == '2':
            menu()
        else:
            print("\033[0;31mPlease make a valid choice.")


def hangman_status(attempts):
    """
    Status of the hangman.
    """
    stages = [
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |     / \\
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |     /
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |      |
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |
            |
            |
            ---
            """,
        """
            --------
            |      |
            |
            |
            |
            |
            ---
            """,
    ]
    return stages[attempts]


def game():
    """
    Function to call other functions used
    """
    get_name()
    menu()
    choose_word()
    start_game()


game()
