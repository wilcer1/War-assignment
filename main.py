#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
War - the card game.

Rules:
1. Deal out deck of 52 cards between two users.
2. Each player plays a card. Higher card wins. Winner takes both cards.
3. If players tie, then each player puts down three cards, and the third
   card competes.
   If a player has less than 4 cards, then they put down all of their cards
   and their final card competes against the other player's fourth card.
   Continue doing this until tie is broken.
   Winner takes all cards.
   If the last card of one's deck is tied with the other,
   the player with most cards win.
4. Game is over when a player doesn't have any cards. The player with
   cards remaining is the winner.

How to play the game:
1. Create player(s) by typing 'player'
2. Type 'start' to deal the deck
3. Continuously type 'draw' to draw cards

"""

import shell


if __name__ == '__main__':
    print(__doc__)
    shell.Shell().cmdloop()
