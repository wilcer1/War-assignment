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
      self.assertEqual(intelligence.win, "You are pro!")

    def test_lose(self):
      self.assertEqual(intelligence.lose, "Better luck next time")

    def test_start(self):
      self.assertEqual(intelligence.start, "Good luck have fun!")

    def test_war(self):
      self.assertEqual(intelligence.war, "This is a war!")
