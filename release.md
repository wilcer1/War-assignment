# Releases 

## Release 1.0 (26/2 2021):
First executable version.
Working without implementation of the highscore and intelligence classes.
Uses shell and cmd loop to manage input and run game.
Classes game, cardhand, deck, card and player used for functionality.
First release where shell works.
Still has bugs and only runs on certain conditions.

### Release 1.1 (1/3 2021):
Mostly functioning version.
Without implementation of the highscore and intelligence classes.
Bugfixes made, still some bugs left.
Added functionality for counting rounds played.
Added method for handling dressed cards in card class.
Added deal method in deck class.
Added testcases.
Fixed war function in game class.
Changed formatting of the show method in card class.
Shell fully functional.

## Release 2.0 (3/3 2021):
Highscore merged and functioning with application.
Highscore storing in textfile added.
Fixed multiple linting errors.
Multiple bugs fixed.
Formatting of show method in card class changed. 
Suited cards changed to tuples to store both value and name.
Roundwinner method introduced in game, to handle who wins the rounds.
Path issue in highscore class fixed.
Syntax fixes.

### Release 2.1(8/3 2021):
Intelligence incorporated and working with application.
Added unittesting, reached 98% unittest coverage.
Bugs still present.
Fixed the bug where a tie on the last card would make cards dissapear.
Fixed multiple Pylint errors.
Fixed multiple Flake8 errors.

### Release 2.2 (9/3 2021):
README.md added.
Multiple Flake8 and Pylint fixes.
Added unittesting.
Created limit on show_highscore to limit the highscore table.
Revamped intelligence to handle most of the output in the application.
Added sound effects to the application.
Fixed multiple bugs.
Game fully functional with no known bugs.

### Release 2.2.1 (12/3 2021):
Fixed a bug for autodraw.