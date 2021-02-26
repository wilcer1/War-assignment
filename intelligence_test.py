import unittest
import intelligence

"""Test intelligence class."""


class TestIntelligenceClass(unittest.TestCase):
    """Test intelligence class."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_win(self):
        """Test win function"""
        self.assertEqual(intelligence.win, "You are pro!")
        intelligence.Intelligence.win(self, intelligence.win)

    def test_lose(self):
        """Test lose function"""
        self.assertEqual(intelligence.lose, "Better luck next time")
        intelligence.Intelligence.lose(self, intelligence.lose)

    def test_start(self):
        """Test start function"""
        self.assertEqual(intelligence.start, "Good luck have fun!")
        intelligence.Intelligence.start(self, intelligence.start)

    def test_war(self):
        """Test war function"""
        self.assertEqual(intelligence.war, "This is a war!")
        intelligence.Intelligence.war(self, intelligence.war)

    def test_match_point(self):
        self.assertEqual(intelligence.match_point, " has 1 card remaining")
        intelligence.Intelligence.match_point(self, intelligence.match_point)
