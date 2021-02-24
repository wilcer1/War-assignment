# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unittesting game."""

import unittest
import game
import cardhand
import deck


class TestGameClass(unittest.TestCase):
    """Testing game class."""

    def setUp(self):
        """Instantiate game in setUp to keep code D.R.Y."""
        self.game = game.Game()

    def tearDown(self):
        """Delete setup instance after usage."""
        del self.game

    def test_init_default_object(self):
        """Check if self.game is instance of Game."""
        exp = game.Game
        self.assertIsInstance(self.game, exp)

        exp = deck.Deck
        self.assertIsInstance(self.game.deck, exp)

    def test_start(self):
        """Test start method."""
        self.game.Start()
        


