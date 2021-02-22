# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test deck class."""

import unittest
import deck
import card


<<<<<<< Updated upstream
class TestDeckClass(unittest.TestCase):
=======
class TestGameClass(unittest.TestCase):
>>>>>>> Stashed changes
    """Test deck class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = deck.Deck()
        exp = deck.Deck
        self.assertIsInstance(res, exp)

    def test_build_deck(self):
        """Check if the build deck method creates a correct deck."""
        self.deck = deck.Deck()
        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
<<<<<<< Updated upstream
        self.deck.build_deck()
        res_list = self.deck.deck
        exp_list = []
        for s in suits:
            for v in range(2, 14):
                exp_list.append(card.Card(s, v))
        index = 0

        for i in exp_list:
            self.assertEqual(i.show(), res_list[index].show())
            index += 1

    def test_shuffle_deck(self):
        """Test the shuffle method to see if it really shuffles."""
        self.deck = deck.Deck()
        self.deck.build_deck()

        og_deck = self.deck.deck

        self.deck.shuffle_deck()
        index = 0
        duplicates = 0

        for i in self.deck.deck:
            if i.show() == og_deck[index].show():
                duplicates += 1
            index += 1

        self.assertLess(duplicates, 10)
=======
        res = self.deck.build_deck
        exp = []
        for s in suits:
            for v in range(1, 14):
                exp.append(card.Card(s, v))

        self.assertEqual(res, exp)
>>>>>>> Stashed changes
