<!-- TOC --><a name="hows-it-hanging"></a>
# How's it Hanging

<img src="assets/images/amiresponsive.png" alt="Image of the site on different device screen sizes">
Hangman is a word guessing game. Traditionally hangman is a game played with pen and paper and two or more people. One person picks a word and lets the others guess the letters to find the correct word. For this project I created an electronic version of this game where the user plays against the computer. This was achieved using python to select a random word from a list and check if guesses are right, wrong, already guessed or invalid. My version of the game has two levels of difficulty, easy and hard. A full description of the rules and traditional version of the game can be found <a href="https://en.wikipedia.org/wiki/Hangman_(game)"> here</a>.  

## Table of Contents
<!-- TOC start -->
- [How's it Hanging](#hows-it-hanging)
  * [Flow Chart](#flow-chart)
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
      - [Validation Testing](#validation-testing)
      - [Bugs:](#bugs)
        * [Fixed Bugs:](#fixed-bugs)
    + [Deployment:](#deployment)
    + [References:](#references)
    + [Acknowledgements](#acknowledgements)
<!-- TOC end -->


<a href="https://hows-ithanging.herokuapp.com/">A link to the deployed website can be found here</a>.

<!-- TOC --><a name="flow-chart"></a>
## Flow Chart
<img src="assets/images/flowchart.png" alt="Diagram of flow chart used to design this project">
- The logic for this project was developed through the use of flow charts using the platform <a href="https://lucid.app/lucidchart/635f4e3b-525e-4ce1-a8b6-f5671a598593/edit?beaconFlowId=1FA3280D25486DE5&invitationId=inv_7f909668-620b-464a-a2c8-5221a92b20f6&page=0_0#"> Lucid Charts</a>.

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
- As a player, I want the instructions to be easily accessible.
- As a player, I want the game to be user friendly.
- As a player, I want the game to be fun and engaging.
- As a player, I want there to be a selection of levels. 

<!-- TOC --><a name="coloured-text"></a>
### Coloured Text
- Throughout the design of the project I followed a flow chart and extended this logic to the visual design of the game. I decided to implement a simple colour scheme to improve the overall user experience.
    - The colour red ("\033[0;31m) was used for errors and wrong guesses. 
    - The colour cyan ("\033[0;36m) was used for input lines. 
    - The colour green ("\033[0;32m) was used for the instruction's menu and for correct guesses.

<!-- TOC --><a name="process-flow-chart"></a>
### Process Flow Chart
Lucid Charts was used to design the logic used in the development of this game.

<!-- TOC --><a name="game-features"></a>
### Game Features
Feature | Description | Example
| --- | --- | --- |
Welcome page | Welcome screen | <img src="assets/images/welcome.png" alt="Image of opening page"> 
Name | Asking for users name all characters valid to allow individuality | <img src="assets/images/name.png" alt="Image of name input section"> 
Instructions | Simple game instuctions are shown to the user if selected | <img src="assets/images/instructionstest.png" alt="Image of instructions menu"> 
Attempts | Screen displayed with remaining attempts this counts down with every wrong guess | <img src="assets/screenshots/lose.png" alt="Image of remaining attempts">
Letters Played | Display of previous guesses is shown after every turn | <img src="assets/screenshots/lose.png" alt="Image of the display of previous guesses">  
Winning Message | Screen displayed when user wins | <img src="assets/images/gamewon.png" alt="Image of Winning game"> 
Losing Message | Screen displayed when user loses | <img src="assets/images/gameover.png" alt="Image of losing game"> 
Choice of levels | Screen displayed for choice of levels. Options are 1 for easy and 2 for hard. The choice determines how many letters will be in the word. | <img src="assets/screenshots/leveloption2test.png" alt="Image of difficulty selection"> 
Hangman Images | |
Play again | Screen displayed asking to play again giving the user the option to 1. go again or 2. return to the main menu| <img src="assets/images/playagain.png" alt="Image of play again screen"> 
Clear Terminal | Terminal cleared between turns to improve overall user experience | <img src="assets/images/clear.png" alt="shows just one hangman on screen"> 
 
<!-- TOC --><a name="future-features"></a>
### Future Features
- High Score Display
    - A future feature that I would like to add to the app is to display high scores. This would be achieved using a Google Spreadsheet to store the number of attempts it took, or numbers of games won for each name entered. This scoreboard could then be displayed by printing the contents to the terminal. 
- Level of Difficulty
    - Although this game provides users with the choice of playing an Easy or Hard game, I would like to add more attempts to the Easy level to further distinguish between the two levels. This would be achieved by saving the hangman images in a new file and calling the altered Easy diagrams for the Easy game or the Standard diagrams for the Hard game.

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
- Built-in Python Libraries
    - os -> The os library was imported to create a function to utilise the os.system to clear the terminal. This library was imported to improve the overall user experience and to ensure the terminal is clear between rounds. 

    - random -> The random library was imported to access the built-in method of generating a random word from the word.py file using the "random." method.

    - sys -> The sys library was imported to create a function that allows the user to exit the game. This was achieved using the built in sys.exit() method. 

<!-- TOC --><a name="testing"></a>
### Testing

Feature | Outcome | Example | Pass
| --- | --- | --- |--- |
Name Input | Validate if field is empty | <img src="assets/screenshots/namevalidentryerror.png" alt="Image of error message if no name entered"> | Pass
Name Input | Validate if entry is valid | <img src="assets/screenshots/namevalidentry.png" alt="Image valid name entered"> | Pass
Main menu | Validate if entry is valid - special character input | <img src="assets/screenshots/mainmenuspecialtest.png" alt="Image of error message for invalid character entry"> | Pass
Main menu | Validate if entry is valid - letter input | <img src="assets/screenshots/mainmenulettertest.png" alt="Image of error message for invalid letter entry"> | Pass
Main menu | Validate if entry is valid - number input | <img src="assets/screenshots/mainmenunumtest.png" alt="Image of error message for invalid number entry"> | Pass
Main menu | Validate if field is empty | <img src="assets/screenshots/mainmenuerror.png" alt="Image of error for empty field"> | Pass
Instructions Options | Validate if selection is valid - option 1 | <img src="assets/screenshots/instructionsoption1test.png" alt="image of tets for option 1"> | Pass
Instructions Options | Validate if selection is valid - option 2 | <img src="assets/screenshots/instructionoption2test.png" alt="image of tets for option 2"> | Pass
Instructions Options | Validate if field is empty | <img src="assets/screenshots/instructionspacetest.png" alt="Image of error message for empty field" > | Pass
Instructions Options | Validate if selection is valid - letter test | <img src="assets/screenshots/instructionlettertest.png" alt="Image of error message for invalid letter entry"> | Pass
Instructions Options | Validate if selection is valid - wrong number test | <img src="assets/screenshots/instructionnumtest.png" alt="Image of error message for invalid number entry"> | Pass
Instructions Options | Validate if selection is valid - special character test | <img src="assets/screenshots/instructionspecialtest.png" alt="Image of error message for invalid entry"> | Pass
Level Selection | Validate if selection is valid - option 1 | <img src="assets/screenshots/leveloption1test.png" alt="Image of Level 1 test"> | Pass
Level Selection | Validate if selection is valid - option 2 | <img src="assets/screenshots/leveloption2test.png" alt="Image of Level 2 test"> > | Pass
Level Selection | Validate if field is empty | <img src="assets/screenshots/leveloptiontest.png" alt="Image of empty field test"> > | Pass
Level Selection | Validate if selection is valid - letter | <img src="assets/screenshots/leveloptionlettertest.png" alt="Image of error message for invalid letter entry"> > | Pass
Level Selection | Validate if selection is valid - Number | <img src="assets/screenshots/leveloptionnumbertest.png" alt="Image of error message for invalid Number entry"> > | Pass
Level Selection | Validate if selection is valid - Special Character | <img src="assets/screenshots/levelspecial.png" alt="Image of error message for invalid character entry"> > | Pass
Game Play | Validate if selection is valid - special character test | <img src="assets/screenshots/gamespecialtest.png" alt="Image of error message for invalid character entry"> | Pass
Game Play | Validate if selection is valid - Number test | <img src="assets/screenshots/gamenumtest.png" alt="Image of error message for invalid number entry"> | Pass
Game Play | Validate if field is empty | <img src="assets/screenshots/gamespacetest.png" alt="Image of error message for empty field"> | Pass
Game Play | Validate if selection is valid - Multiple character test | <img src="assets/screenshots/gamemultierror.png" alt="Images of error messages for multiple character guesses made"> <img src="assets/screenshots/gamemultiguesstest.png"> | Pass
Winning Message | Validate if message is correct | <img src="assets/screenshots/win.png" alt="Message for correct guess and winning game"> | Pass
Losing Message | Validate if message is correct | <img src="assets/screenshots/lose.png" alt="Message for incorrect guess and losing game"> | Pass
Play again input | Validate if selection is valid  - option 1 | <img src="assets/screenshots/againop1.png" alt="Image for play again option 1"> | Pass
Play again input | Validate if selection is valid  - option 2 | <img src="assets/screenshots/againop2.png" alt="Image for play again option 2"> | Pass
Play again input | Validate if selection is valid  - letter | <img src="assets/screenshots/againletter.png" alt="Image for play again invalid letter entry"> | Pass
Play again input | Validate if selection is valid  - number | <img src="assets/screenshots/againnum.png" alt="Image for play again invalid number entry"> | Pass
Play again input | Validate if selection is valid  - special | <img src="assets/screenshots/againspecial.png" alt="Image for play again invalid character entry"> | Pass
Play again input | Validate if field is empty | <img src="assets/screenshots/againblank.png" alt="Image for play again error message">| Pass
Exit Game option | Validate if field is empty | <img src="assets/screenshots/mainmenuexittest.png" alt="Image of exit message"> | Pass

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

<!-- TOC --><a name="validation-testing"></a>
#### Validation Testing:
Testing | Results 
| --- | --- | 
Initial validation testing | <img src="assets/images/initialvalidatorresults.png" alt="Image of inital validator results">  
Final validation testing | <img src="assets/images/finalcodevalidation.png" alt="Image of final validator results"> 
Words.py validation testing | <img src="assets/images/wordstest.png" alt="Image of words list validator results"> 

- The code was tested using a PEP8 validator and the initial results were fixed by correcting all of the errors and warnings shown until none remained. 


<!-- TOC --><a name="bugs"></a>
#### Bugs:
<!-- TOC --><a name="fixed-bugs"></a>
##### Fixed Bugs:
Bug | Example |  Description | Fix
| --- | --- | --- | --- | 
Name Entry | <img src="assets/bugs/namebug.png" alt="Image of Name Bug"> <img src="assets/bugs/nameerror.png" alt="Image of Name Function Code"> | This bug was noted during testing. The original code allowed for a space to be entered as a Name. However, this was not a valid entry as it does not print a name to the terminal. | This was fixed by adding an elif statement to the code to ensure that a character needs to be entered. <img src="assets/bugs/namebugfix.png" alt="Image of Name fix">
Numbers accepted | <img src="assets/bugs/numbersbug.png" alt="Image of Number being accepted"> | This bug was noted during testing of the game. It was noted that numbers were accepted as valid guesses by the user. | This bug was fixed by adding the isalpha() method to the elif statement for players_turn. <img src="assets/bugs/numberfix.png" alt="Image of input fix">
Double Hangman | <img src="assets/bugs/doublehangmanbug.png" alt="Image of double hangman on terminal"> | This bug was observed during game play that if a guess was made two hangman images were printed in error. | This bug was fixed by removing the second print(hangman_status(attempts)) that was present in the code. <img src="assets/bugs/doublehangmanbugfix.png" alt="Image of double hangman code update">

<!-- TOC --><a name="deployment"></a>
### Deployment:
The application has been deployed using <a href="">Heroku</a> by following these steps:

Heroku was used to deploy the application.

* Commit changes and push them to GitHub.
* Go to the Heroku's website.
* Create an account or select log in. 
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
- The code used to create the images that display the hangman image to the user were adapted from youtube and github user Kiteco. 
- <a href="https://www.w3schools.com/python/ref_string_isalpha.asp">W3Schools </a>was used as a resource for solving syntax errors and for the isalpha() method. 
- <a href="https://www.askpython.com/python/examples/exit-a-python-program">Askpython </a>was used for the implementation of sys.exit()
- <a href="https://stackoverflow.com/">Stack Overflow </a> was used for assistance with troubleshooting issues.
- <a href="https://www.yawintutor.com/indentationerror-expected-an-indented-block-in-python/#:~:text=The%20python%20IndentationError%3A%20expected%20an,mix%20of%20tabs%20and%20spaces">Yawin Tutor </a>was used for fixing syntax and coding errors that appeared throughout the coding process. 


<!-- TOC --><a name="acknowledgements"></a>
### Acknowledgements
- First I would like to thank my Partner for his love and support throughout the completion of this project.
- I would also like to thank my mentor Marcel for his advice and support.
- My friends for constantly testing the project.
- Tutor Assistance for their help and support.
- Code Institute and its Slack community for their support and providing me with the necessary knowledge to complete this project.