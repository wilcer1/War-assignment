"""Highscore Class."""
import os


class Highscore:
    """Highscore Class."""

    # Make highscore_list an attribute??

    def __init__(self, path):
        """Set path to highscore_file."""
        self.path = path
        if not os.path.exists(path):
            create = open(path, "x")
            create.close()

    @classmethod
    def sort_highscore(cls, highscore_list):
        """Sort highscore_list."""
        sorted_highscore_list = sorted(highscore_list)
        return sorted_highscore_list

    def write_to_highscore(self, highscore_list):
        """Write to highscore file.."""
        self.sort_highscore(highscore_list)
        with open(self.path, "w") as text_file:
            for score, name in highscore_list:
                text_file.write(f"{score}:{name}\n")

    def add_highscore(self, score, name):
        """Add player and score to highscore list."""
        highscore_list = self.read_highscore()
        highscore_list.append((score, name))
        self.write_to_highscore(highscore_list)

    def read_highscore(self):
        """Read highscore from file and return list."""
        highscore_list = []
        with open(self.path, "r") as text_file:
            for line in text_file:
                line = line.rstrip("\n")
                temp = line.split(":")
                score = int(temp[0])
                name = temp[1]
                highscore_list.append((score, name))

        sorted_highscore_list = self.sort_highscore(highscore_list)
        return sorted_highscore_list

    @classmethod
    def show_highscore(cls, highscore_list):
        """Show highscore."""
        show_list = []
        for count, (score, name) in enumerate(highscore_list, 1):
            if count <= 20:
                show_list.append((f"{count}. {name} won in {score} rounds."))

        return show_list
