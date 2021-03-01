"""Highscore Class."""


class Highscore:
    """Highscore Class."""

    # Make highscore_list an attribute??

    def __init__(self, path):
        """Set path to highscore_file."""
        self.path = path

    def sort_highscore(self, highscore_list):
        """Sort highscore_list."""
        sorted_highscore_list = sorted(highscore_list)
        return sorted_highscore_list

    def write_to_highscore(self, highscore_list):
        """Write to highscore file.."""
        self.sort_highscore(highscore_list)
        with open("test_file.txt", "w") as text_file:
            for score, name in highscore_list:
                text_file.write(f"{score}:{name}\n")

    def add_highscore(self, score, name):
        """Add player and score to highscore list."""
        highscore_list = self.read_highscore(self.path)
        highscore_list.append((score, name))
        self.write_to_highscore(highscore_list)

    def read_highscore(self, path):
        """Read highscore from file and return list."""
        highscore_list = []
        with open(path, "r") as highscore_file:
            for line in highscore_file:
                line = line.rstrip("\n")
                temp = line.split(":")
                score = int(temp[0])
                name = temp[1]
                highscore_list.append((score, name))

        sorted_highscore_list = self.sort_highscore(highscore_list)
        return sorted_highscore_list

    def show_highscore(self, highscore_list):
        """Show highscore."""
        for count, (score, player) in enumerate(highscore_list, 1):
            print(f"{count}. {player} won in {score} rounds.")
