"""Test Highscore Class."""
import unittest
import highscore
import player
import os


class TestHighscoreClass(unittest.TestCase):
    """Test Highscore Class."""

    def setUp(self):
        """Create test_file.txt file."""
        self.highscore = highscore.Highscore("test_file.txt")

        self.test_list = []
        self.test_list.append((1, "Bane"))
        self.test_list.append((2, "Joker"))
        self.test_list.append((3, "Robin"))
        self.test_list.append((4, "Batman"))

    @classmethod
    def tearDownClass(cls):
        """Remove test_file.txt."""
        os.remove("test_file.txt")

    def test_init_default_object(self):
        """Test class attribute."""
        res = self.highscore.path
        exp = "test_file.txt"
        self.assertEqual(res, exp)
        self.assertIsInstance(self.highscore, highscore.Highscore)
        self.assertTrue(os.path.exists(self.highscore.path))

    def test_create_highscore_file(self):
        """Tests if highscore file is created."""
        exp = "test123\n"
        with open(self.highscore.path, "w+") as highscore_file:
            highscore_file.write(exp)
            highscore_file.seek(0)
            res = highscore_file.read()
            self.assertEqual(res, exp)

    def test_sort_highscore(self):
        """Test if sort method works as intended."""
        unsorted_test_list = []
        unsorted_test_list.append((2, "Joker"))
        unsorted_test_list.append((4, "Batman"))
        unsorted_test_list.append((1, "Bane"))
        unsorted_test_list.append((3, "Robin"))

        exp = self.test_list
        res = self.highscore.sort_highscore(unsorted_test_list)
        self.assertListEqual(exp, res)

    def test_write_to_highscore(self):
        """Test if highscore is written to text file."""
        exp = []
        for score, name in self.test_list:
            exp.append(f"{score}:{name}\n")

        self.highscore.write_to_highscore(self.test_list)

        with open("test_file.txt", "r") as test_file:
            res = []
            for line in test_file:
                res.append(line)
        self.assertListEqual(res, exp)

    def test_read_highscore(self):
        """Test reading highscore and adding to list."""

    def test_add_highscore(self):
        """Test add player highscore to file."""
        f = open(self.highscore.path, "w")
        f.close()
        test_player = player.Player("Gimli")
        self.highscore.add_highscore(13, test_player.name)
        res = self.highscore.read_highscore()
        exp = []
        exp.append((13, "Gimli"))
        self.assertEqual(exp, res)

    def test_show_highscore(self):
        """Test the output of show_highscore."""
        res = self.highscore.show_highscore(self.test_list)
        exp = []
        for count, (score, name) in enumerate(self.test_list, 1):
            exp.append((f"{count}. {name} won in {score} rounds."))

        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
