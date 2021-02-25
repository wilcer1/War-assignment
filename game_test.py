# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unittesting game."""

import unittest
import game
import player
import card


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

    def test_set_get_players(self):
        """Test the setters and getters."""
        with self.assertRaises(ValueError):
            self.game.set_player(3, "Wille")

        with self.assertRaises(TypeError):
            self.game.set_player(1, 5)

        res = self.game.get_players()
        exp = (None, None)
        self.assertEqual(res, exp)

        self.game.set_player(1, "Wille")
        self.game.start()
        res = self.game.get_players()
        p1 = res[0]
        p2 = res[1]
        self.assertIsInstance(p1, player.Player)
        self.assertIsInstance(p2, player.Player)

        res = p1.name
        exp = "Wille"
        self.assertEqual(res, exp)

    def test_start(self):
        """Test start method."""
        res = self.game.start()
        exp = "Create player(s) first"
        self.assertEqual(exp, res)

        self.game.set_player(1, "Wille")
        self.game.start()
        p1, p2 = self.game.get_players()
        res = p1.cardhand.cards_remaining()
        self.assertEqual(res, 26)
        res = p2.cardhand.cards_remaining()
        self.assertEqual(res, 26)

    def test_draw(self):
        """Test continue method."""
        res = self.game.draw()
        exp = "Create player(s) and start game first"
        self.assertEqual(res, exp)

        self.game.set_player(1, "Wille")
        self.game.start()
        p1, p2 = self.game.get_players()
        p1_card, p2_card = self.game.draw()
        res1 = p1.cardhand.cards_remaining()
        res2 = p2.cardhand.cards_remaining()
        self.assertEqual(res1, 25)
        self.assertEqual(res2, 25)

        self.assertIsInstance(p1_card, card.Card)
        self.assertIsInstance(p2_card, card.Card)
