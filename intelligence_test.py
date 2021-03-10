"""Test intelligence class."""

import unittest
import intelligence


class TestIntelligenceClass(unittest.TestCase):
    """Test intelligence class."""

    def setUp(self):
        """Set up."""

    def test_win(self):
        """Test win function."""
        self.assertEqual(intelligence.WIN, "You are pro!")

    def test_lose(self):
        """Test lose function."""
        self.assertEqual(intelligence.LOSE,
                         "Better luck next time, human trash. "
                         + "AI will prevail!")

    def test_start(self):
        """Test start function."""
        self.assertEqual(intelligence.START, "Good luck have fun!")

    def test_war(self):
        """Test war function."""
        self.assertEqual(intelligence.WAR, "This is a war!")

    def test_match_point(self):
        """Test match_point function."""
        self.assertEqual(intelligence.MATCH_POINT,
                         " has few cards remaining")
