#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""Unit testing."""

import card
import unittest


class TestCardClass(unittest.TestCase):
    """Test card class."""

    def setUp(self):
        """Instantiate object in setup to keep it D.R.Y."""
        self.card = card.Card()
        self.card.create_card()

    def tearDown(self):
        """Delete setup instantiated object."""
        del self.card

    def test_init_default_object(self):
        """Instantiate card object and check properties."""
        res = self.card
        exp = card.Card
        self.assertIsInstance(res, exp)

    def test_create_card(self):
        """Check if suit and value attributes are assigned correctly."""
        res = self.card.suit
        exp = res in range(1, 4)
        self.assertTrue(exp)

        res = self.card.value
        exp = res in range(1, 14)
        self.assertTrue(exp)

    def test_suit_string(self):
        """Set suit value to 1-4 and check if right string is returned."""
        self.card.suit = 1
        res = self.card.suit_string()
        exp = "Clubs"
        self.assertEqual(res, exp)

        self.card.suit = 2
        res = self.card.suit_string()
        exp = "Hearts"
        self.assertEqual(res, exp)

        self.card.suit = 3
        res = self.card.suit_string()
        exp = "Diamonds"
        self.assertEqual(res, exp)

        self.card.suit = 4
        res = self.card.suit_string()
        exp = "Spades"
        self.assertEqual(res, exp)
