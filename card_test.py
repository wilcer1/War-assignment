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
