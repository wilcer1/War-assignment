# War assignment
## A02 Sustainable programming
You can run this game against a computer or against your friend, by choosing 1 or 2 players.
This war game is based on cards where the one with 0 cards loses.
We implemented Intelligence by using the class to handle almost all of the outputs.
The game also has unique outputs when playing agains the computer.

# Developers
This game is developed by Lucas Carlsson, Timmy Bergvall and Wille Cervin.

# Before playing the game!
*Use Git Bash for these commands*
## If you only want to play the game, follow this step:
Before running the game install playsound by writing "pip install playsound" in the directory where the game is placed.

If you want to play the game and make tests on our program, follow this step:<br/>
To install everything you need, and write "pip install -r requirements.txt" in the directory where the game is placed.<br/>
You can also write "make install", it will do the same thing.<br/>

# How to run the game
## This is an alternative way to run the program!
1. Open gitbash and make sure that you are in the directory where the game is placed
2. Write the following command; "Python main.py"
3. Write "player" and choose between 1 or 2 players by typing "1" or "2"
4. Enter the name for your player
5. Write "start" to deal the deck and start the game
6. Then write draw until you either win or lose

# Useful commands for game
Command "autodraw" runs the whole game until a winner is set (cheat)<br/>
Command "q", "EOF", "quit" and "exit" stops the program<br/>
Command "change_name" makes it posible to change your name whenever you want<br/>
Command "help" and "?" shows the command list<br/>
Command "highscore" views the highscore list<br/>
Command "start" deals the deck<br/>

# How to make tests and documentation
## If you want to run tests
This is how you can run tests without makefile:<br/>
1. Be sure you are in the right directory 
2. Then use "coverage run -m unittest discover . "filenameYouWantToTest.py""
3. To get the coverage report write "coverage -m report"

If you want to run test on all files excluding linters you can use the command "make unittest"<br/>
If you want to run test on all files including linters you can use the command "make test"<br/>
If you want to run test on all files excluding linters and get coverage report you can use the command "make coverage"<br/>
If you want to test linters on all files you can use the command "make lint"<br/>

## If you want to get documentation

To generate uml diagrams use the command "make pyreverse"<br/>
the diagrams generated can be found in doc/pyreverse<br/>

To get documentation you can use the command "make pdoc"<br/>
the generated documents can be found in doc/pydoc<br/>

If you want to generate both pydoc and uml you can use the command "make doc"<br/>

If the above method for generating documentation doesnt work you can use this method:<br/>
1. Install pycco with this command "pip install pycco"
2. Then use this command "pycco *.py" to generate the documentation.
the generated documents can be found in docs<br/>
