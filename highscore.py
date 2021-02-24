"""Highscore Class."""


class Highscore:
    """Highscore Class."""

    def sort_highscore(self, highscore_list):
        """Sort highscore_list."""
        sorted_highscore_list = sorted(highscore_list, reverse=True)
        return sorted_highscore_list

    def write_to_highscore(self, highscore_list):
        """Write to highscore file.."""
        self.sort_highscore(highscore_list)
        with open("test_file.txt", "w") as text_file:
            for score, name in highscore_list:
                text_file.write(f"{name} has {score} points\n")
