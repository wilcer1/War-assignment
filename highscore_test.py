"""Test Highscore Class."""
import unittest
import os
import highscore


class TestHighscoreClass(unittest.TestCase):
    """Test Highscore Class."""

    def setUp(self):
        """Create test_highscore.txt file."""
        self.highscore_file = open("test_highscore.txt", "w+")

        self.h = highscore.Highscore()

        self.unsorted_test_list = []
        self.unsorted_test_list.append((2, "Joker"))
        self.unsorted_test_list.append((4, "Batman"))
        self.unsorted_test_list.append((1, "Bane"))
        self.unsorted_test_list.append((3, "Robin"))

        self.test_list = []
        self.test_list.append((4, "Batman"))
        self.test_list.append((3, "Robin"))
        self.test_list.append((2, "Joker"))
        self.test_list.append((1, "Bane"))

    def tearDown(self):
        """Close and remove test file."""
        self.highscore_file.close()
        os.remove("test_highscore.txt")

    def test_create_highscore_file(self):
        """Tests if highscore file is created."""
        exp = "test123\n"
        self.highscore_file.write(exp)
        self.highscore_file.seek(0)
        res = self.highscore_file.read()
        self.assertEqual(res, exp)

    def test_sort_highscore_file(self):
        """Test if sort method works as intended."""
        exp = self.test_list
        res = self.h.sort_highscore(self.unsorted_test_list)
        self.assertListEqual(exp, res)

    def test_write_to_highscore(self):
        """Test if highscore is written to text file."""
        exp = []
        for score, name in self.test_list:
            exp.append(f"{name} has {score} points\n")

        self.h.write_to_highscore(self.test_list)

        with open("test_file.txt", "r") as test_file:

            res = []
            for line in test_file:
                res.append(line)

        self.assertListEqual(res, exp)

    def test_show_highscore(self):
        """Test the output of show_highscore."""
        # exp = "print directly from test_list?"
        # res = self.h.show_highscore

    def test_add_highscore(self):
        """Test add highscore to file."""
        # pass


if __name__ == "__main__":
    unittest.main()
