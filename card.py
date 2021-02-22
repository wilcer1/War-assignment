#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""Card class."""

import random


class Card():
    """Card class."""

    def __init__(self):
        """Init the object and set attributes."""
        random.seed()

    def create_card(self):
        """Assign the attributes that the card should contain."""
        self.suit = random.randint(1, 4)
        self.value = random.randint(1, 14)

    def suit_string(self):
        """Return suit as string depending on value of int attribute suit."""
        if self.suit == 1:
            return "Clubs"
        elif self.suit == 2:
            return "Hearts"
        elif self.suit == 3:
            return "Diamonds"
        else:
            return "Spades"
