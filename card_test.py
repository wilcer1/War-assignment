#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""Unit testing."""

import card
import unittest


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

    def test_show(self):
        """Check if right string is returned from show method."""
        exp = "2 of Diamonds"
        res = self.card.show()
        self.assertEqual(exp, res)
<<<<<<< Updated upstream
=======

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
>>>>>>> Stashed changes
