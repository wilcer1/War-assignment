"""Highscore Class."""


class Highscore:
    """Highscore Class."""

    # Make highscore_list an attribute??

    def sort_highscore(self, highscore_list):
        """Sort highscore_list."""
        sorted_highscore_list = sorted(highscore_list)
        return sorted_highscore_list

    def write_to_highscore(self, highscore_list):
        """Write to highscore file.."""
        self.sort_highscore(highscore_list)
        with open("test_file.txt", "w") as text_file:
            for score, name in highscore_list:
                text_file.write(f"{name} has {score} points\n")

    def add_highscore(self, score, name, highscore_list):
        """Add player and score to highscore list."""
        highscore = (score, name)
        highscore_list.append(highscore)
        return highscore_list
        # write_to_highscore(highscore_list)

    def show_highscore(self, highscore_list):
        """Show highscore."""
        for count, (score, player) in enumerate(highscore_list, 1):
            print(f"{count}. {player} won in {score} rounds.")
