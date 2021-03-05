# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test deck class."""

import unittest
import deck
import card


class TestGameClass(unittest.TestCase):
    """Test deck class."""

    def setUp(self):
        """Set up the deck instance."""
        self.deck = deck.Deck()

    def tearDown(self):
        """Delete instance after use."""
        del self.deck

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = deck.Deck()
        exp = deck.Deck
        self.assertIsInstance(res, exp)

    def test_build_deck(self):
        """Check if the build deck method creates a correct deck."""
        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

        self.deck.build_deck()
        res_list = self.deck.deck
        exp_list = []
        for suit in suits:
            for value in range(2, 15):
                exp_list.append(card.Card(suit, value))
        index = 0

        for i in exp_list:
            self.assertEqual(i.show(), res_list[index].show())
            index += 1

        exp = 52
        res = len(res_list)
        self.assertEqual(res, exp)

    def test_get_deck(self):
        """Return deck and compare to attribute."""
        self.deck.build_deck()

        res = self.deck.get_deck()
        exp = self.deck.deck
        index = 0
        for i in exp:
            self.assertEqual(i.show(), res[index].show())
            index += 1

    def test_shuffle_deck(self):
        """Test the shuffle method to see if it really shuffles."""
        self.deck.build_deck()

        sorted_deck = []
        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
        for suit in suits:
            for value in range(2, 15):
                sorted_deck.append(card.Card(suit, value))
        self.deck.shuffle_deck()

        duplicates = 0
        for i in range(len(sorted_deck)):
            if sorted_deck[i].show() == self.deck.get_deck()[i].show():
                duplicates += 1

        self.assertLess(duplicates, 10)

    def test_deal_deck(self):
        """Test so the deck deals correctly between players."""
        self.deck.build_deck()
        self.deck.shuffle_deck()
        res = self.deck.deal_deck()
        player1 = res[0]
        player2 = res[1]
        self.assertEqual(len(player1), len(player2))
