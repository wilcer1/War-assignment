"""Intelligence class."""

WIN = ", you are pro!"
LOSE = "Better luck next time "
START = "Good luck have fun!"
WAR = "This is a war!"
MATCH_POINT = " has 1 card remaining"


class Intelligence():
    """Intelligence class."""

    @classmethod
    def win(cls):
        """Win function."""
        print(WIN)

    @classmethod
    def lose(cls):
        """Lose function."""
        print(LOSE)

    @classmethod
    def start(cls):
        """Start function."""
        print(START)

    @classmethod
    def war(cls):
        """War function."""
        print(WAR)

    @classmethod
    def match_point(cls):
        """Match_point function."""
        print(MATCH_POINT)
