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
- As a player, I want the game to be fun and engaging.
- As a player, I want there to be a selection of levels. 

<!-- TOC --><a name="coloured-text"></a>
### Coloured Text
- Throughout the design of the project I followed a flow chart and extended this logic to the visual design of the game. I decided to implement a simple colour scheme to improve the overall user experience.
    - The colour red ("\033[0;31m) was used for errors and wrong guesses. 
    - The colour cyan ("\033[0;36m) was used for input lines. 
    - The colour green ("\033[0;32m) was used for the instructions menu and for correct guesses.

<!-- TOC --><a name="process-flow-chart"></a>
### Process Flow Chart
Lucid Charts was used to design the logic used in the development of this game.

<!-- TOC --><a name="game-features"></a>
### Game Features
- Welcome page 
- Instructions 
- Game
- Winning Message
- Losing Message
- Coloured Text
- Choice of levels
- Hangman Images
- Play again
- Clear Terminal
 
<!-- TOC --><a name="languages-used"></a>
#### Languages Used
- <a href="https://en.wikipedia.org/wiki/Python_(programming_language)"> Python</a>

<!-- TOC --><a name="technology-used"></a>
#### Technology Used
- <a href="https://gitpod.io/workspaces">GitPod</a> was used for writing code, committing, and then pushing to GitHub.
- <a href="https://github.com/AmyDelaney94/">Github</a> was used to store the project after pushing.
- <a href="https://lucid.app/documents#/dashboard">Lucid Charts</a> was used to create and design the flow chart used in the logical design of this project. 
- <a href="http://ami.responsivedesign.is/">Am I Responsive?</a> was used in order to see responsive design throughout the process.
- <a href="http://pep8online.com/">PEP8 online check</a> was used to validate the python code. 
- <a href="http://pep8online.com/">Heroku</a> was used to deploy the application. 

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
The application has been deployed using <a href="">Heroku</a> by following these steps:

Heroku was used to deploy the application.

* Commit changes and push them to GitHub.
* Go to the Heroku's website.
* From the Heroku dashboard, click on "Create new app".
* Enter the "App name" and "Choose a region" before clicking on "Create app".
* Go to "Config Vars" under the "Settings" tab.
* Click on "Reveals Config Vars" and add the KEY: CREDS and the VALUE stored in creds.json file if needed.
* Add the Config Var, KEY: PORT and VALUE: 8000.
* Go to "Buildpacks" section and click "Add buildpack".
* Select "python" and click "Save changes"
* Add "nodejs" buildpack as well using the same process.
* Go to "Deployment method", under the "Deploy" tab select "GitHub" and click on "Connect to GitHub".
* Go to "Connect to GitHub" section and "Search" the repository to be deployed.
* Click "Connect" next the repository name.
* Choose "Automatic deploys" or "Manual deploys" to deploy your application.

<!-- TOC --><a name="references"></a>
### References:
- <a href="https://www.w3schools.com/python/ref_string_isalpha.asp">W3Schools </a>was used as a resource for solving syntax errors and for the isalpha() method. 
- <a href="https://www.askpython.com/python/examples/exit-a-python-program">Askpython </a>was used for the implementation of sys.exit()
- <a href="https://stackoverflow.com/">Stack Overflow </a> was used for assistance with troubleshooting issues.
- <a href="https://www.yawintutor.com/indentationerror-expected-an-indented-block-in-python/#:~:text=The%20python%20IndentationError%3A%20expected%20an,mix%20of%20tabs%20and%20spaces">Yawin Tutor </a>was used for fixing syntax and coding errors that appeared throughout the coding process. 


<!-- TOC --><a name="acknowledgements"></a>
### Acknowledgements
- First I would like to thank my Partner for his love and support throughout the completion of this project.
- I would also like to thank my mentor Marcel for his advice and support.
- My friends for constantly testing the project on their different devices.
- Tutor Assistance for their help and support.
- Code Institute and its Slack community for their support and providing me with the necessary knowledge to complete this project.