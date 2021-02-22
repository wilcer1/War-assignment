# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Import cards to use in deck."""

import card
<<<<<<< Updated upstream
import random
=======
>>>>>>> Stashed changes


class Deck:
    """Deck class."""

    def __init__(self):
<<<<<<< Updated upstream
        """Create empty list to store cards in."""
        self.deck = []
        self.suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

    def build_deck(self):
        """Build the deck using a nested for loop to avoid duplicates."""
        for s in self.suits:
            for v in range(2, 14):
                self.deck.append(card.Card(s, v))

    def shuffle_deck(self):
        """Switch positions of the iterator index and the random number index."""
        for c in range(len(self.deck) - 1, 0, -1):
            i = random.randint(0, c)
            self.deck[c], self.deck[i] = self.deck[i], self.deck[c]
=======
        """Create empty list to store cards in"""
        self.cards = []
>>>>>>> Stashed changes
