<!-- TOC --><a name="hows-it-hanging"></a>
# How's it Hanging

<img src="assets/images/amiresponsive.png" alt="Image of the site on different device screen sizes">
Hangman is a word guessing game. Traditionally hangman is a game played with pen and paper and two or more people. One person picks a word and lets the others guess the letters to find the correct word. For this project I created an electronic version of this game where the user plays against the computer. This was achieved using python to slect a random word from a list and check if guesses are right, wrong, already guessed or invalid. My version of the game has two levels of difficulty, easy and hard. A full description of the rules and traditional version of the game can be found <a href="https://en.wikipedia.org/wiki/Hangman_(game)"> here</a>.  


## Table of Contents
<!-- TOC start -->
- [How's it Hanging](#hows-it-hanging)
  * [User Experience](#user-experience)
    + [Project Goals](#project-goals)
    + [User Stories](#user-stories)
    + [Coloured Text](#coloured-text)
    + [Process Flow Chart](#process-flow-chart)
    + [Game Features](#game-features)
      - [Technology Used](#technology-used)
      - [Languages Used](#languages-used)
    + [Testing](#testing)
      - [User Stories Testing](#user-stories-testing)
      - [Bugs:](#bugs)
        * [Fixed Bugs:](#fixed-bugs)
    + [Deployment:](#deployment)
    + [References:](#references)
    + [Acknowledgements](#acknowledgements)
<!-- TOC end -->


<a href="https://hows-ithanging.herokuapp.com/">A link to the deployed website can be found here</a>.


<!-- TOC --><a name="user-experience"></a>
## User Experience
<!-- TOC --><a name="project-goals"></a>
### Project Goals
- The game is easy to navigate and user friendly.
- The game to loop and allow the player to continue to play after each game. 
- The game should have a choice of difficulty levels.
- It should be clear how many attempts are left in the game. 
- To provide the user with an easy to find instructions section to explain how the game works.

<!-- TOC --><a name="user-stories"></a>
### User Stories
- As a player, I want the instructions to be easily accessable.
- As a player, I want the game to be user friendly.
- As a player, I want the game to work on multiple devices.
- As a player, I want the game to be fun and engaging.
- As a player, I want there to be a selection of levels. 

<!-- TOC --><a name="coloured-text"></a>
### Coloured Text
- Throughout the design of the project I followed a flow chart and extended this logic to the visual design of the game. 
    - The colour red was used for errors and wrong guesses. 
    - The colour cyan was used for input lines. 
    - The colour green was used for the instructions menu and for correct guesses.  


<!-- TOC --><a name="process-flow-chart"></a>
### Process Flow Chart
Lucid Charts was used to design the logic used in the development of this game.

<!-- TOC --><a name="game-features"></a>
### Game Features
- Choice of levels
- Name input
- Instructions 
- 
 
<!-- TOC --><a name="technology-used"></a>
#### Technology Used
<!-- TOC --><a name="languages-used"></a>
#### Languages Used
- Python

- GitPod
    -  GitPod was used for writing code, committing, and then pushing to GitHub.
- GitHub
    - GitHub was used to store the project after pushing.
- Lucid Charts

- Am I Responsive?
    - Am I Responsive was used in order to see responsive design throughout the process.


<!-- TOC --><a name="testing"></a>
### Testing
<!-- TOC --><a name="user-stories-testing"></a>
#### User Stories Testing
- As a user I want the game to be easy to navigate.
    - This was achieved by using the numbers 1 and 2 for Yes and No consistently throughout the game. 
- As a user I want the game to loop and allow players to continue playing or exit after each round. 
    - This was achieved by asking player if they want to play again after each win or loss with 1 starting the game again and 2 bringing the user back to the main menu. 
- As a user I want it to be clear how many attempts are left.
    - This was achieved by printing the remaining attempts after each round of the game. 
- As a user I want to give the user a choice of difficulty.
    - This was achieved by providing the user with a choice of easy or hard difficulty levels at the start of each game. 
- To provide the user with an easy to find instructions section to explain how the game works.
    - This was achieved by providing an instructions option on the main menu. 

<!-- TOC --><a name="bugs"></a>
#### Bugs:
<!-- TOC --><a name="fixed-bugs"></a>
##### Fixed Bugs:

<!-- TOC --><a name="deployment"></a>
### Deployment:


<!-- TOC --><a name="references"></a>
### References:
- W3Schools was used as a resource for solving syntax errors and for the isalpha()
method.https://www.w3schools.com/python/ref_string_isalpha.asp
- Askpython was used for the implementation of sys.exit()
https://www.askpython.com/python/examples/exit-a-python-program
- Stack Overflow Used for assistance with troubleshooting issues.
- https://www.yawintutor.com/indentationerror-expected-an-indented-block-in-python/#:~:text=The%20python%20IndentationError%3A%20expected%20an,mix%20of%20tabs%20and%20spaces. used for fixing syntax and coding errors. 


<!-- TOC --><a name="acknowledgements"></a>
### Acknowledgements
- First I would like to thank my Partner for his love and support throughout the completion of this project.
- I would also like to thank my mentor Marcel for his advice and support.
- My friends for constantly testing the project on their different devices.
- Tutor Assistance for their help and support.
- Code Institute and its Slack community for their support and providing me with the necessary knowledge to complete this project.