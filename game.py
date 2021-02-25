# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Game class with logic."""

import deck
import random
import player


class Game():
    """Handle all the logic and get called by shell."""

    def __init__(self):
        """Instantiate deck instance."""
        self.deck = deck.Deck()
        self.player1 = None
        self.player2 = None

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
        """If player 2 is not set, create new
            instance with name computer"""
        if self.player1 is None and self.player2 is None:
            return "Create player(s) first"
        else:
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
        else:
            p1_int =\
                random.randint(0, self.player1.cardhand.cards_remaining())
            p1_card = self.player1.cardhand.hand.pop(p1_int)
            p2_int =\
                random.randint(0, self.player2.cardhand.cards_remaining())
            p2_card = self.player2.cardhand.hand.pop(p2_int)
            return p1_card, p2_card

    def round_winner(self, card1, card2):
        """Give cards to winner, if equal call war, return string."""
        winner_cards = []
        winner_cards.append(card1)
        winner_cards.append(card2)
        if isinstance(card1.value, tuple):
            card1_value = card1.value[1]
        else:
            card1_value = card1.value
        if isinstance(card2.value, tuple):
            card2_value = card2.value[1]
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
            winner_cards.append(self.player1.cardhand.war()[0])
            p1_face_up = self.player1.cardhand.war()[1]
            winner_cards.append(self.player2.cardhand.war()[0])
            p2_face_up = self.player2.cardhand.war()[1]
            winner_cards.append(p1_face_up)
            winner_cards.append(p2_face_up)
            if p1_face_up > p2_face_up:
                self.player1.cardhand.recieve_cards(winner_cards)
                print(f"")
                
