"""Unit testing."""

import player
import unittest

"""Test Player Class."""


class TestPlayerClass(unittest.TestCase):
    """Test Player Class."""

    pass

    def SetUp(self):
        """Create a player object."""
        self.player = player.Player("Lucas")
        print(self.player)

    def TearDown(self):
        """Delete player object."""
        pass

    def test_init_default_object(self):
        """Test instansiation of player object."""
        self.assertEqual(self.player.name == "Lucas")


if __name__ == "__main__":
    unittest.main()
