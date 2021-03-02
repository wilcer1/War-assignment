#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""Unit testing."""

import unittest
import card


class TestCardClass(unittest.TestCase):
    """Test card class."""

    def setUp(self):
        """Instantiate object in setup to keep it D.R.Y."""
        self.card = card.Card("Diamonds", 2)

    def tearDown(self):
        """Delete setup instantiated object."""
        del self.card

    def test_init_default_object(self):
        """Instantiate card object and check properties."""
        res = self.card
        exp = card.Card
        self.assertIsInstance(res, exp)

        self.card = card.Card("Diamonds", 5)
        self.assertEqual(self.card.value, 5)

        self.card = card.Card("Diamonds", 11)
        res = self.card.value[1]
        exp = 11
        self.assertEqual(res, exp)

        self.card = card.Card("Diamonds", 12)
        res = self.card.value[1]
        exp = 12
        self.assertEqual(res, exp)

        self.card = card.Card("Diamonds", 13)
        res = self.card.value[1]
        exp = 13
        self.assertEqual(res, exp)

        self.card = card.Card("Diamonds", 14)
        res = self.card.value[1]
        exp = 14
        self.assertEqual(res, exp)

    def test_show(self):
        """Check if right string is returned from show method."""
        exp = "2 of Diamonds"
        res = self.card.show()
        self.assertEqual(exp, res)

        self.card = card.Card("Diamonds", 14)
        exp = "Ace of Diamonds"
        res = self.card.show()
        self.assertEqual(exp, res)

    def test_get_value_dressed(self):
        """Check if method returns only if card is dressed."""
        with self.assertRaises(TypeError):
            self.card.get_value_dressed()
        self.card = card.Card("Diamonds", 13)
        res = self.card.get_value_dressed()
        exp = 13
        self.assertEqual(res, exp)
