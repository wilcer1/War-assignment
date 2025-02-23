# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Import cards to use in deck."""

import random
import card


class Deck:
    """Deck class."""

    def __init__(self):
        """Create empty list to store cards in."""
        self.deck = []
        self.suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

    def build_deck(self):
        """Build the deck using a nested for loop to avoid duplicates."""
        for suit in self.suits:
            for value in range(2, 15):
                self.deck.append(card.Card(suit, value))

    def get_deck(self):
        """Return deck attribute."""
        return self.deck

    def shuffle_deck(self):
        """Switch positions of the iterator index and the random num index."""
        random.shuffle(self.deck)

    def deal_deck(self):
        """Distribute deck evenly, return 2 lists of cards."""
        player1 = []
        player2 = []
        for _i in range(0, int(len(self.deck)/2)):
            player1.append(self.deck.pop())
            player2.append(self.deck.pop())
        return player1, player2
