# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unittesting shell."""

import shell
import unittest
import game


class TestShellClass(unittest.TestCase):
    """Testing shell class."""

    def setUp(self):
        """Instantiate shell in setUp to keep code D.R.Y."""
        self.shell = shell.Shell()
        self.game = game.Game()

    def tearDown(self):
        """Delete setup instance after usage."""
        del self.shell

    def test_init_default_object(self):
        """Check instance of shell and game."""
        exp = shell.Shell
        self.assertIsInstance(self.shell, exp)
        exp = game.Game
        self.assertIsInstance(self.game, exp)
