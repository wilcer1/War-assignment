# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Game class with logic."""

import deck
import cardhand
import player


class Game():
    """Handle all the logic and get called by shell."""

    def __init__(self):
        """Instantiate deck instance."""
        self.deck = deck.Deck()

    def start(self):
        """Create, shuffle and deal deck evenly."""
        self.deck.build_deck()
        self.deck.shuffle_deck()
