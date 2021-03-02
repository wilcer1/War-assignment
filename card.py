#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""Card class."""
 

class Card():
    """Card class."""

    def __init__(self, suit, value):
        """Init the object and set attributes."""
        self.suit = suit
        self.value = value

    def show(self):
        """Return the card as String."""
        return f"{self.value} of {self.suit}"
