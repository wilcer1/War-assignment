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
        # If player 2 is not set, create new
        # instance with name computer
        if self.player1 is None and self.player2 is None:
            return "Create player(s) first"

        if self.player2 is None:
            self.player2 = player.Player("Computer")

        self.deck.build_deck()
        self.deck.shuffle_deck()
        decksplit = self.deck.deal_deck()
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
            print(f"{self.player1.name} wins!\n{card1.show()} beats\
                 {card2.show()}")
        elif card1_value < card2_value:
            self.player2.cardhand.recieve_cards(winner_cards)
            print(f"{self.player2.name} wins!\n{card2.show()} beats\
                 {card1.show()}")
        else:
            self.war(winner_cards)

        print(f"{self.player1.name} cards remaining:\
             {self.player1.cardhand.cards_remaining()}")
        print(f"{self.player2.name} cards remaining:\
             {self.player2.cardhand.cards_remaining()}")

    def war(self, winner_cards):
        """War function."""
        print("WAAAAAAR!!!")
        p1_face_down, p1_face_up = self.player1.cardhand.war()
        p2_face_down, p2_face_up = self.player2.cardhand.war()
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
            print(f"{self.player1.name} Wins!\n{p1_face_up.show()} beats\
                {p2_face_up.show()}!")
            print(f"All {len(winner_cards)} cards go to {self.player1.name}")
            self.player1.cardhand.recieve_cards(winner_cards)
        elif p2_face_up_value > p1_face_up_value:
            print(f"{self.player2.name} Wins!\n{p2_face_up.show()} beats\
                {p1_face_up.show()}!")
            print(f"All {len(winner_cards)} cards go to {self.player2.name}")
            self.player2.cardhand.recieve_cards(winner_cards)
        else:
            self.war(winner_cards)
        print(f"{self.player1.name} cards remaining:\
             {self.player1.cardhand.cards_remaining()}")
        print(f"{self.player2.name} cards remaining:\
             {self.player2.cardhand.cards_remaining()}")

    def check_cards(self):
        """Check if players have less than or 5 cards."""
        if self.player1.cardhand.cards_remaining() <= 5:
            return True
        if self.player2.cardhand.cards_remaining() <= 5:
            return True
        return False

    def check_for_winner(self):
        """Check if anyone won."""
        if self.player1.cardhand.cards_remaining() == 0:
            print("player 2 wins")
            return True
        if self.player2.cardhand.cards_remaining() == 0:
            print("player1 wins")
            return True

        return False


    def add_to_highscore(self):
        """Add result to highscore."""
        hiscore = highscore.Highscore("highscore.txt")
        hiscore_list = hiscore.read_highscore()
        hiscore.write_to_highscore()
