# War assignment
A02 Sustainable programming

# Developers
This game is developed by Lucas Carlsson, Timmy Bergvall and Wille Cervin.

# Before playing the game!
If you only want to play the game, follow this step:
Before running the game install playsound by writing "pip install playsound" in the directory where the game is placed.

If you want to play the game and make tests on our program, follow this step:
To install everything you need, (use gitbash) and write "pip install -r requirements.txt" in the directory where the game is placed.
You can also write "make install", it will do the same thing.

# How to run the game
This is an alternative way to run the program!
1. Open gitbash and make sure that you are in the directory where the game is placed
2. Write the following command; "Python main.py"
3. Write "player" and choose between 1 or 2 players by typing "1" or "2"
4. Enter the name for your player
5. Write "start" to deal the deck and start the game
6. Then write draw until you either win or lose

# Useful commands for game
Command "autodraw" runs the whole game until a winner is set (cheat)
Command "q" "EOF" "quit" and "exit" stops the program
Command "change_name" makes it posible to change your name whenever you want
Command "help" and "?" shows the command list
Command "highscore" views the highscore list
Command "start" deal the deck

# How to make tests and documentation
If you want to run a test file 
1. Be sure you are in the right directory 
2. Then use "coverage run -m unittest discover . "filenameYouWantToTest_test.py""

If you run the command "make test" it first looks at flake8 then pylint.

If you run the command "make coverage" It will check test on everything.

1. To generate a documentation of the code install pycco with this command "pip install pycco"
2. Then use this command "pycco *.py" to generate the documentation!
