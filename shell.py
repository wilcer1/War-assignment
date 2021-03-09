# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using cmd module and specifically cmdloop and a shell for main program."""

import cmd
import game


class Shell(cmd.Cmd):
    """Class with command arguments to play the cardgame."""

    intro = 'Welcome to War. Type help or ? to list commands.\n'
    prompt = '(...) '

    def __init__(self):
        """Initialize shell and game."""
        super().__init__()
        self.game = game.Game()
        self.players = 0

    def do_player(self, _):
        """Create player(s)."""
        if self.game.player1 is None and\
                self.game.player2 is None:
            try:
                self.players = int(input("1 or 2 players? "))
            except ValueError:
                print("Only 1 or 2 allowed ")
                self.do_player("player")
            else:
                if self.players not in range(1, 3):
                    print("You can only be 1 or 2 players ")
                    self.do_player("player")
            if self.players == 1:
                name = input("Enter your name: ")
                self.game.set_player(1, name)
                print("Player(s) created, type start to start the game")
                self.players = 0
            elif self.players == 2:
                name = input("Enter Player 1's name: ")
                while not isinstance(name, str):
                    print("Name must be a string")
                    name = input("Enter player 1's name: ")

                name2 = input("Enter Player 2's name: ")
                while not isinstance(name2, str):
                    print("Name must be a string")
                    name = input("Enter player 2's name: ")
                self.players = 0

                self.game.set_player(1, name)
                self.game.set_player(2, name2)
                print("Player(s) created, type start to start the game")
        else:
            print("Players already created. Type 'change_name' to change name")

    def do_start(self, _):
        """Start the game and deal the deck."""
        if not self.game.started:
            if self.game.player1 is None:
                print("Create at least one player first, type 'player'")
            else:
                self.game.start()
        else:
            print("Game already started, type 'draw' to draw card")

    def do_draw(self, _):
        """Draw a new card."""
        if not self.game.started:
            print("You need to start the game first, type 'start'")
        else:
            if not self.game.check_for_winner():
                if self.game.check_cards():
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
        if not self.game.started:
            print("You need to start the game first, type 'start'")
        else:
            while not self.game.check_for_winner():
                self.do_draw("draw")

    def do_highscore(self, _):
        """Show highscore list."""
        self.game.show_hiscore()

    def do_change_name(self, _):
        """Change name of player if player exists."""
        if self.game.player1 is None and self.game.player2 is None:
            print("No players created")
        else:
            old_name = input("Enter your current name: ")
            if old_name == self.game.player1.name:
                new_name = input("Enter your desired name: ")
                self.game.set_player_name(new_name, self.game.player1)
                print(f"Name changed from {old_name} to {new_name}")
            elif old_name == self.game.player2.name:
                new_name = input("Enter your desired name: ")
                self.game.set_player_name(new_name, self.game.player2)
                print(f"Name changed from {old_name} to {new_name}")
            else:
                print("No such player")
