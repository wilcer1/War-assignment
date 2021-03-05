# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Game class with logic."""

import random
import deck
import player
import highscore


class Game():
    """Handle all the logic and get called by shell."""

    def __init__(self):
        """Instantiate deck instance."""
        self.deck = deck.Deck()
        self.player1 = None
        self.player2 = None
        self.rounds = 0

    def set_player(self, playernum, name):
        """Create a player."""
        if playernum > 2:
            raise ValueError("Maximum of 2 players")
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        if playernum == 1:
            self.player1 = player.Player(name)
        elif playernum == 2:
            self.player2 = player.Player(name)

    def get_players(self):
        """Return all players created."""
        return self.player1, self.player2

    def start(self):
        """Create, shuffle and deal deck evenly."""
        self.rounds = 0
        # If player 2 is not set, create new
        # instance with name computer
        if self.player1 is None and self.player2 is None:
            return "Create player(s) first"

        if self.player2 is None:
            self.player2 = player.Player("Computer")

        self.deck.build_deck()
        self.deck.shuffle_deck()
        decksplit = self.deck.deal_deck()
        self.player1.cardhand.hand.clear()
        self.player2.cardhand.hand.clear()
        self.player1.cardhand.recieve_cards(decksplit[0])
        self.player2.cardhand.recieve_cards(decksplit[1])

    def draw(self):
        """Draw cards and return them."""
        if self.player1 is None and self.player2 is None:
            return "Create player(s) and start game first"

        p1_cards = self.player1.cardhand.cards_remaining() - 1
        p2_cards = self.player2.cardhand.cards_remaining() - 1
        p1_int = random.randint(0, (p1_cards))
        p1_card = self.player1.cardhand.hand.pop(p1_int)
        p2_int = random.randint(0, (p2_cards))
        p2_card = self.player2.cardhand.hand.pop(p2_int)
        return p1_card, p2_card

    def round_winner(self, card1, card2):
        """Give cards to winner, if equal call war, return string."""
        self.rounds += 1
        winner_cards = []
        winner_cards.append(card1)
        winner_cards.append(card2)
        if isinstance(card1.value, tuple):
            card1_value = card1.get_value_dressed()
        else:
            card1_value = card1.value
        if isinstance(card2.value, tuple):
            card2_value = card2.get_value_dressed()
        else:
            card2_value = card2.value

        if card1_value > card2_value:
            self.player1.cardhand.recieve_cards(winner_cards)
            print("------------------------------------------------")
            print(f"{self.player1.name} wins!\n{card1.show()} beats "
                  + f"{card2.show()}")
            print(f"{self.player1.name} cards remaining: "
                  + f"{self.player1.cardhand.cards_remaining()}")
            print(f"{self.player2.name} cards remaining: "
                  + f"{self.player2.cardhand.cards_remaining()}")
            print("------------------------------------------------")
        elif card1_value < card2_value:
            self.player2.cardhand.recieve_cards(winner_cards)
            print("------------------------------------------------")
            print(f"{self.player2.name} wins!\n{card2.show()} beats "
                  + f"{card1.show()}")
            print(f"{self.player1.name} cards remaining: "
                  + f"{self.player1.cardhand.cards_remaining()}")
            print(f"{self.player2.name} cards remaining: "
                  + f"{self.player2.cardhand.cards_remaining()}")
            print("------------------------------------------------")
        else:
            self.war(winner_cards)

    def war(self, winner_cards):
        """War function."""
        if self.check_cards():
            if self.player1.cardhand.cards_remaining() <= 4:
                p1_face_down, p1_face_up = self.player1.cardhand.last_war()
                p2_face_down, p2_face_up = self.player2.cardhand.war()
            elif self.player2.cardhand.cards_remaining() <= 4:
                p2_face_down, p2_face_up = self.player2.cardhand.last_war()
                p1_face_down, p1_face_up = self.player1.cardhand.war()
        else:
            p1_face_down, p1_face_up = self.player1.cardhand.war()
            p2_face_down, p2_face_up = self.player2.cardhand.war()

        print("WAAAAAAR!!!")

        winner_cards.append(p1_face_up)
        winner_cards.append(p2_face_up)
        for card in p1_face_down:
            winner_cards.append(card)
        for card in p2_face_down:
            winner_cards.append(card)
        if isinstance(p1_face_up.value, tuple):
            p1_face_up_value = p1_face_up.get_value_dressed()
        else:
            p1_face_up_value = p1_face_up.value
        if isinstance(p2_face_up.value, tuple):
            p2_face_up_value = p2_face_up.get_value_dressed()
        else:
            p2_face_up_value = p2_face_up.value

        if p1_face_up_value > p2_face_up_value:
            print("------------------------------------------------")
            print(f"{self.player1.name} wins!\n{p1_face_up.show()} beats "
                  + f"{p2_face_up.show()}")
            print(f"All {len(winner_cards)} cards go to {self.player1.name}")
            self.player1.cardhand.recieve_cards(winner_cards)
            print("------------------------------------------------")
        elif p2_face_up_value > p1_face_up_value:
            print("------------------------------------------------")
            print(f"{self.player2.name} wins!\n{p2_face_up.show()} beats "
                  + f"{p1_face_up.show()}")
            print(f"All {len(winner_cards)} cards go to {self.player2.name}")
            self.player2.cardhand.recieve_cards(winner_cards)
            print("------------------------------------------------")
        else:
            print("------------------------------------------------")
            print("Tie!!")
            print(f"{p1_face_up.show()} is equal to {p2_face_up.show()}")
            print("------------------------------------------------")
            self.war(winner_cards)

        print(f"{self.player1.name} cards remaining: "
              + f"{self.player1.cardhand.cards_remaining()}")
        print(f"{self.player2.name} cards remaining: "
              + f"{self.player2.cardhand.cards_remaining()}")

    def check_cards(self):
        """Check if players have less than or 4 cards."""
        if self.player1.cardhand.cards_remaining() <= 4 or\
                self.player2.cardhand.cards_remaining() <= 4:
            return True
        return False

    def check_for_winner(self):
        """Check if anyone won."""
        if self.player1.cardhand.cards_remaining() == 0:
            print(f"{self.player2.name} wins")
            if self.player2.name != "Computer":
                self.add_to_hiscore(self.player2.name)
            return True
        if self.player2.cardhand.cards_remaining() == 0:
            print(f"{self.player1.name} wins")
            self.add_to_hiscore(self.player1.name)
            return True

        return False

    def add_to_hiscore(self, player_name):
        """Add result to highscore."""
        hiscore = highscore.Highscore("highscore.txt")
        hiscore.add_highscore(self.rounds, player_name)

    @classmethod
    def show_hiscore(cls):
        """Print highscore list."""
        hiscore = highscore.Highscore("highscore.txt")
        hiscore_list = hiscore.show_highscore(hiscore.read_highscore())
        for result in hiscore_list:
            print(result)
