# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Game class with logic."""

import deck
import cardhand


class Game():
    """Handle all the logic and get called by shell."""
    
    def __init__(self):
        """Instantiate deck instance."""
        self.deck = deck.Deck()



