# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unittesting game."""

import unittest
import mock
import game


class TestGameClass(unittest.TestCase):
    """Testing game class, use mock on objects needed from other modules."""

    @mock.patch("card.Card")
    @mock.patch("player.Player")
    @mock.patch("deck.Deck")
    @mock.patch("cardhand.Cardhand")
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
    
    def test_start(self, mock):
        """Test start method."""
        self.game.start()
        
        self.assertIsInstance(self.game.deck.deck[0], )

        res = len(self.game.deck.deck)
        self.assertEqual(res, 52)

