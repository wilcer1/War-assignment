#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Class for cards in hand."""

import random


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

    def war(self):
        """Return cards for war."""
        face_down = []
        if len(self.hand) > 5:
            for i in range(3):
                index = random.randint(0, len(self.hand) - 1)
                face_down.append(self.hand.pop(index))
            face_up = self.hand.pop(random.randint(0, len(self.hand) - 1))
        else:
            face_up = self.hand.pop(random.randint(0, len(self.hand) - 1))
            for c in self.hand:
                face_down.append(c)
                self.hand.remove(c)
        return face_down, face_up
