"""Unit testing."""
import unittest
import player
import cardhand


class TestPlayerClass(unittest.TestCase):
    """Test Player Class."""

    def setUp(self):
        """Create a player object."""
        self.player = player.Player("Lucas")

    def tearDown(self):
        """Delete player object."""

    def test_init_default_object(self):
        """Test instansiation of player object."""
        res = self.player.name
        exp = "Lucas"
        self.assertEqual(res, exp)

    def test_change_name(self):
        """Test player name change."""
        self.player.name = "Wille"
        res = self.player.name
        exp = "Wille"
        self.assertEqual(res, exp)

    def test_card_hand(self):
        """Test that card_hand is empty."""
        exp = cardhand.Cardhand
        self.assertIsInstance(self.player.cardhand, exp)

        res = self.player.cardhand.cards_remaining()
        exp = 0
        self.assertEqual(res, exp)
