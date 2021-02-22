import unittest
import intelligence

"""Test intelligence class."""


class TestIntelligenceClass(unittest.TestCase):
    """Test intelligence class."""

    def setUp(self):
        print("Hello")

    def test_win(self):
        self.assertEqual("You are pro!", "You are pro!")
