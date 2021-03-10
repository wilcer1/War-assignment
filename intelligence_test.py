"""Test self.intelligence class."""

import unittest
import intelligence
import player


class TestIntelligenceClass(unittest.TestCase):
    """Test self.intelligence class."""

    def setUp(self):
        """Set up."""
        self.intelligence = intelligence.Intelligence()
        self.player1 = player.Player("Wille")
        self.player2 = player.Player("Lucas")

    def test_win(self):
        """Test win function."""
        self.assertEqual(self.intelligence.WIN, "You are pro!")

    def test_lose(self):
        """Test lose function."""
        self.assertEqual(
            self.intelligence.LOSE,
            "Better luck next time, human trash. AI will prevail! "
        )

    def test_start(self):
        """Test start function."""
        self.assertEqual(self.intelligence.START, "Good luck have fun!")

    def test_war(self):
        """Test war function."""
        self.assertEqual(self.intelligence.WAR, "This is a war!")

    def test_match_point(self):
        """Test match_point function."""
        self.assertEqual(self.intelligence.MATCH_POINT,
                         " has few cards remaining")
