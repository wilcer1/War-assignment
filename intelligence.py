"""intelligence class"""
win = ", you are pro!"
lose = "Better luck next time "
start = "Good luck have fun!"
war = "This is a war!"
match_point = " has 1 card remaining"


class Intelligence():
    """intelligence class"""

    def win(self, win):  # you won
        """Win function."""
        print(win)

    def lose(self, lose):  # you lost
        print(lose)

    def start(self, start):  # glhf message
        print(start)

    def war(self, war):  # If cards is the same
        print(war)

    def match_point(self, match_point):  # If a player only has 1 card
        print(match_point)
