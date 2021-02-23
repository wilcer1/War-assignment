#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Class for cards in hand."""


class Cardhand:
    """cardhand class."""

    def __init__(self):
        """Initialize class."""
        self.hand = []

    def cards_remaining(self):
        """Check how many cards remain in hand."""
        return len(self.hand)

    def recieve_cards(self, cards):
        """Add recieved cards to hand."""
        for c in cards:
            self.hand.append(c)
