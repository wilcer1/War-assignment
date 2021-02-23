# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Import cards to use in deck."""

import card
import random


class Deck:
    """Deck class."""

    def __init__(self):
        """Create empty list to store cards in."""
        self.deck = []
        self.suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

    def build_deck(self):
        """Build the deck using a nested for loop to avoid duplicates."""
        for s in self.suits:
            for v in range(2, 14):
                self.deck.append(card.Card(s, v))

    def get_deck(self):
        """Return deck attribute."""
        return self.deck

    def shuffle_deck(self):
        """Switch positions of the iterator index and the random num index."""
        random.shuffle(self.deck)

