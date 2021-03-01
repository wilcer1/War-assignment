"""Test Highscore Class."""
import unittest
import highscore
import player


class TestHighscoreClass(unittest.TestCase):
    """Test Highscore Class."""

    def setUp(self):
        """Create test_file.txt file."""
        self.h = highscore.Highscore("test_file.txt")

        self.unsorted_test_list = []
        self.unsorted_test_list.append((2, "Joker"))
        self.unsorted_test_list.append((4, "Batman"))
        self.unsorted_test_list.append((1, "Bane"))
        self.unsorted_test_list.append((3, "Robin"))

        self.test_list = []
        self.test_list.append((1, "Bane"))
        self.test_list.append((2, "Joker"))
        self.test_list.append((3, "Robin"))
        self.test_list.append((4, "Batman"))

    @classmethod
    def tearDownClass(cls):
        """Remove test file."""
        # os.remove("test_file.txt")

    def test_init_default_object(self):
        """Test class attribute."""
        res = self.h.path
        print(res)
        exp = "test_file.txt"
        self.assertEqual(res, exp)
        self.assertIsInstance(self.h, highscore.Highscore)

    def test_create_highscore_file(self):
        """Tests if highscore file is created."""
        exp = "test123\n"
        with open("test_file.txt", "w+") as self.highscore_file:
            self.highscore_file.write(exp)
            self.highscore_file.seek(0)
            res = self.highscore_file.read()
            self.assertEqual(res, exp)

    def test_sort_highscore(self):
        """Test if sort method works as intended."""
        exp = self.test_list
        res = self.h.sort_highscore(self.unsorted_test_list)
        self.assertListEqual(exp, res)

    def test_write_to_highscore(self):
        """Test if highscore is written to text file."""
        exp = []
        for score, name in self.test_list:
            exp.append(f"{score}:{name}\n")

        self.h.write_to_highscore(self.test_list)

        with open("test_file.txt", "r") as test_file:
            res = []
            for line in test_file:
                res.append(line)
        self.assertListEqual(res, exp)

    def test_read_highscore(self):
        """Test reading highscore and adding to list."""

    def test_add_highscore(self):
        """Test add player highscore to file."""
        # Remove added player from test_list to not fuck up rest of the test
        # if run out of order, .
        test_player = player.Player("Gimli")
        self.h.add_highscore(13, test_player.name)
        res = self.h.read_highscore(self.h.path)
        exp = self.test_list
        exp.append((13, "Gimli"))
        self.assertEqual(exp, res)

    def test_show_highscore(self):
        """Test the output of show_highscore."""
        # exp = "print directly from test_list?"
        # res = self.h.show_highscore


if __name__ == "__main__":
    unittest.main()
