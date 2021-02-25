#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""Card class."""


class Card():
    """Card class."""

    def __init__(self, suit, value):
        """Init the object and set attributes."""
        self.suit = suit
        if value == 11:
            self.value = ("Jack", 11)
        elif value == 12:
            self.value = ("Queen", 12)
        elif value == 13:
            self.value = ("King", 13)
        elif value == 14:
            self.value = ("Ace", 14)
        else:
            self.value = value

    def show(self):
        """Return the card as String."""
        if isinstance(self.value, tuple):
            return f"{self.value[0]} of {self.suit}", self.value[1]
        else:
            return f"{self.value} of {self.suit}"
