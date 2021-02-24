"""Test Highscore Class."""
import unittest
import os
import player


class TestHighscoreClass(unittest.TestCase):
    """Test Highscore Class."""

    def setUp(self):
        pass

    def tearDown(self):
        os.remove("test_highscore.txt")

    def test_create_highscore_file(self):
        """Tests if highscore file is created"""
        test_string = "test123\n"
        with open("test_highscore.txt", "w") as highscore_file:
            highscore_file.write(test_string)
        with open("test_highscore.txt", "r") as highscore_file:
            self.assertEqual(highscore_file.read(), test_string)


if __name__ == "__main__":
    unittest.main()
