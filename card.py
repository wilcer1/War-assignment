#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""Card class."""


class Card():
    """Card class."""

    def __init__(self, suit, value):
        """Init the object and set attributes."""
        self.suit = suit
        if value == 11:
            self.value = "Jack"
        elif value == 12:
            self.value = "Queen"
        elif value == 13:
            self.value = "King"
        elif value == 14:
            self.value = "Ace"
        else:
            self.value = value

    def show(self):
        """Return the card as String."""
        return f"{self.value} of {self.suit}"
