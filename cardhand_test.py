#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest

import cardhand


class TestDiceClass(unittest.TestCase):
    """Testing cardhand class."""

    def setUp(self):
        """Instantiate cardhand to keep code D.R.Y."""
        self.cardhand = cardhand.Cardhand()

    def tearDown(self):
        """Delete cardhand instance after use."""
        del self.cardhand

    def test_init_default_object(self):
        """Test the instance and the hand attribute."""
        exp = cardhand.Cardhand
        self.assertIsInstance(self.cardhand, exp)

        exp = []
        res = self.cardhand.hand
        self.assertListEqual(exp, res)
