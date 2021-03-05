# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using cmd module and specifically cmdloop and a shell for main program."""

import cmd
import sys
import game


class Shell(cmd.Cmd):
    """Class with command arguments to play the cardgame."""

    intro = 'Welcome to War. Type help or ? to list commands.\n'
    prompt = '(...) '

    def __init__(self):
        """Initialize shell and game."""
        super().__init__()
        self.game = game.Game()

    def do_player(self, _):
        """Create player(s)."""
        players = int(input("1 or 2 players?"))
        if not isinstance(players, int):
            raise TypeError("1 or 2 allowed")
        if players not in range(1, 3):
            print("You can only be 1 or 2 players")
            self.do_player("player")
        if players == 1:
            name = input("Enter your name: ")
            if not isinstance(name, str):
                raise TypeError("Must be a string")
            self.game.set_player(1, name)
            print("Player(s) created, type start to start the game")
        elif players == 2:
            name = input("Enter Player 1's name: ")
            if not isinstance(name, str):
                raise TypeError("Must be a string")
            name2 = input("Enter Player 2's name: ")
            if not isinstance(name, str):
                raise TypeError("Must be a string")
            self.game.set_player(1, name)
            self.game.set_player(2, name2)
            print("Player(s) created, type start to start the game")

    def do_start(self, _):
        """Start the game and deal the deck."""
        if self.game.player1 is None:
            print("Create atleast one player first")
        else:
            self.game.start()
            print("Deck has been dealt, type draw to draw card")

    def do_draw(self, _):
        """Draw a new card."""
        if self.game.check_for_winner():
            print(f"It took {self.game.rounds} rounds")
            sys.exit()
        elif self.game.check_cards():
            self.game.war([])
        else:
            p1_card, p2_card = self.game.draw()
            self.game.round_winner(p1_card, p2_card)

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Thank you for playing, come back soon")
        return True

    def do_quit(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_q(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)

    def do_autodraw(self, _):
        """Draw until end."""
        while not self.game.check_for_winner():
            self.do_draw("draw")

    def do_highscore(self, _):
        """Show highscore list."""
        self.game.show_hiscore()

    def do_change_name(self, _):
        """Change name of player if player exists."""
        old_name = input("Enter your current name: ")
        if old_name == self.game.player1.name:
            new_name = input("Enter your desired name: ")
            self.game.set_player_name(new_name, self.game.player1)
        elif old_name == self.game.player2.name:
            new_name = input("Enter your desired name: ")
            self.game.set_player_name(new_name, self.game.player2)
        else:
            print("No such player")
