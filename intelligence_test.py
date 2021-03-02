import unittest
import intelligence
import player

"""Test intelligence class."""


class TestIntelligenceClass(unittest.TestCase):
    """Test intelligence class."""

    def setUp(self):
        """Set up."""
        self.player1 = player.Player("Wille")
        self.player2 = player.Player("Lucas")

    def tearDown(self):
        """TearDown."""
        pass

    def test_win(self):
        """Test win function."""
        self.assertEqual(intelligence.win, ", you are pro!")
        print(f'{self.player1.name} is tha madda facking name')
        intelligence.Intelligence.win(self, intelligence.win)

    def test_lose(self):
        """Test lose function."""
        self.assertEqual(intelligence.lose, "Better luck next time ")
        intelligence.Intelligence.lose(self, intelligence.lose)

    def test_start(self):
        """Test start function."""
        self.assertEqual(intelligence.start, "Good luck have fun!")
        intelligence.Intelligence.start(self, intelligence.start)

    def test_war(self):
        """Test war function."""
        self.assertEqual(intelligence.war, "This is a war!")
        intelligence.Intelligence.war(self, intelligence.war)

    def test_match_point(self):
        """Test match_point function."""
        self.assertEqual(intelligence.match_point, " has 1 card remaining")
        intelligence.Intelligence.match_point(self, intelligence.match_point)


if __name__ == "__main__":
    unittest.main()
