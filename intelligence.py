"""Intelligence class."""

from playsound import playsound

WIN = "You are pro!"
LOSE = "Better luck next time, human trash. AI will prevail! "
START = "Good luck have fun!"
WAR = "This is a war!"
MATCH_POINT = " has few cards remaining"


class Intelligence:
    """Intelligence class."""

    def __init__(self):
        """Initialize class."""
        self.player1 = None
        self.player2 = None

    def recieve_players(self, p_1, p_2):
        """Recieve the players."""
        self.player1 = p_1
        self.player2 = p_2

    def card_1_win(self, card1, card2):
        """Print when card 1 wins."""
        print("------------------------------------------------")
        print(f"{self.player1.name} wins!\n{card1.show()} beats "
              + f"{card2.show()}")
        print(
            f"{self.player1.name} cards remaining: "
            + f"{self.player1.cardhand.cards_remaining()}"
        )
        print(
            f"{self.player2.name} cards remaining: "
            + f"{self.player2.cardhand.cards_remaining()}"
        )
        print("------------------------------------------------")
        if self.player2.name == "Computer":
            print("------------------------------------------------")
            print(WIN)
            print("------------------------------------------------")

    def card_2_win(self, card1, card2):
        """Print when card 2 wins."""
        print("------------------------------------------------")
        print(f"{self.player2.name} wins!\n{card2.show()} beats "
              + f"{card1.show()}")
        print(
            f"{self.player1.name} cards remaining: "
            + f"{self.player1.cardhand.cards_remaining()}"
        )
        print(
            f"{self.player2.name} cards remaining: "
            + f"{self.player2.cardhand.cards_remaining()}"
        )
        print("------------------------------------------------")
        if self.player2.name == "Computer":
            print("------------------------------------------------")
            print(LOSE)
            print("------------------------------------------------")

    def war_card_1_win(self, card1, card2, winner_cards):
        """Print when card1 wins war."""
        print("------------------------------------------------")
        print(f"{self.player1.name} wins!\n{card1.show()} beats "
              + f"{card2.show()}")
        print(f"All {len(winner_cards)} cards go to " + f"{self.player1.name}")
        print("------------------------------------------------")

    def war_card_2_win(self, card1, card2, winner_cards):
        """Print when card2 wins war."""
        print("------------------------------------------------")
        print(f"{self.player2.name} wins!\n{card2.show()} beats "
              + f"{card1.show()}")
        print(f"All {len(winner_cards)} cards go to " + f"{self.player2.name}")
        print("------------------------------------------------")

    @classmethod
    def war_tie(cls, card1, card2):
        """Print if war is tie."""
        print("------------------------------------------------")
        print("Tie!!")
        print(f"{card1.show()} is equal to {card2.show()}")
        print("------------------------------------------------")

    @classmethod
    def lose(cls):
        """Lose function."""
        print(LOSE)
        playsound("lose.mp3")

    @classmethod
    def start(cls):
        """Start function."""
        print(START)
        playsound("start.mp3")

    @classmethod
    def war(cls):
        """War function."""
        print("------------------------------------------------")
        print(WAR)
        print("------------------------------------------------")

    @classmethod
    def match_point(cls, player):
        """Match_point function."""
        print(player.name, MATCH_POINT)
        playsound("match_point.mp3")

    @classmethod
    def win(cls, player):
        """win function."""
        print("------------------------------------------------")
        print(f"{player.name} wins the game!\nType 'Restart' to restart the game")
        playsound("win.mp3")
