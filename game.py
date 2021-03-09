# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Game class with logic."""

import random
from playsound import playsound
import deck
import player
import highscore
import intelligence


class Game():
    """Handle all the logic and get called by shell."""

    def __init__(self):
        """Instantiate deck instance."""
        self.deck = deck.Deck()
        self.intelligence = intelligence.Intelligence()
        self.player1 = None
        self.player2 = None
        self.rounds = 0
        self.winner = None
        self.started = False

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

    @classmethod
    def set_player_name(cls, new_name, player):
        """Change the name of the player."""
        player.name = new_name

    def get_players(self):
        """Return all players created."""
        return self.player1, self.player2

    def start(self):
        """Create, shuffle and deal deck evenly."""
        self.rounds = 0
        self.started = True
        self.winner = None
        # If player 2 is not set, create new
        # instance with name computer

        if self.player2 is None:
            self.player2 = player.Player("Computer")

        self.intelligence.recieve_players(self.player1, self.player2)

        self.deck.build_deck()
        self.deck.shuffle_deck()
        decksplit = self.deck.deal_deck()
        self.player1.cardhand.hand.clear()
        self.player2.cardhand.hand.clear()
        self.player1.cardhand.recieve_cards(decksplit[0])
        self.player2.cardhand.recieve_cards(decksplit[1])
        print("Deck has been dealt, type draw to draw card ;)")
        self.intelligence.start()

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
            self.intelligence.card_1_win(card1, card2)
        elif card1_value < card2_value:
            self.player2.cardhand.recieve_cards(winner_cards)
            self.intelligence.card_2_win(card1, card2)
        else:
            self.war(winner_cards)

    def war(self, winner_cards):
        """War function."""
        if not self.check_for_winner():
            if self.check_cards():
                if self.player1.cardhand.cards_remaining() <= 4:
                    p1_face_down, p1_face_up = self.player1.cardhand.last_war()
                    p2_face_down, p2_face_up = self.player2.cardhand.war()
                    self.intelligence.match_point(self.player1)
                elif self.player2.cardhand.cards_remaining() <= 4:
                    p2_face_down, p2_face_up = self.player2.cardhand.last_war()
                    p1_face_down, p1_face_up = self.player1.cardhand.war()
                    self.intelligence.match_point(self.player2)
            else:
                p1_face_down, p1_face_up = self.player1.cardhand.war()
                p2_face_down, p2_face_up = self.player2.cardhand.war()

            self.intelligence.war()

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
                self.player1.cardhand.recieve_cards(winner_cards)
                self.intelligence.war_card_1_win(p1_face_up, p2_face_up,
                                                 winner_cards)
            elif p2_face_up_value > p1_face_up_value:
                self.player2.cardhand.recieve_cards(winner_cards)
                self.intelligence.war_card_2_win(p1_face_up, p2_face_up,
                                                 winner_cards)
            else:
                self.intelligence.war_tie(p1_face_up, p2_face_up)
                self.war(winner_cards)
        else:
            self.winner.cardhand.recieve_cards(winner_cards)

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
        if self.winner is None:
            if self.player1.cardhand.cards_remaining() == 0:
                print("------------------------------------------------")
                print(f"{self.player2.name} wins the game!")
                self.winner = self.player2
                if self.player2.name != "Computer" and self.rounds != 0:
                    playsound("win.mp3")
                    self.add_to_hiscore(self.player2.name)
                self.started = False
                print(f"It took {self.rounds} rounds")
                return True
            if self.player2.cardhand.cards_remaining() == 0 and\
                    self.rounds != 0:
                print("------------------------------------------------")
                print(f"{self.player1.name} wins the game!")
                playsound("win.mp3")
                self.winner = self.player1
                self.add_to_hiscore(self.player1.name)
                self.started = False
                print(f"It took {self.rounds} rounds")
                return True
        else:
            print("Game already over, type 'start' to redeal the deck")
            return False

    def add_to_hiscore(self, player_name):
        """Add result to highscore txt."""
        hiscore = highscore.Highscore("highscore.txt")
        if self.rounds > 1:
            hiscore.add_highscore(self.rounds, player_name)

    @classmethod
    def show_hiscore(cls):
        """Print highscore list."""
        hiscore = highscore.Highscore("highscore.txt")
        hiscore_list = hiscore.show_highscore(hiscore.read_highscore())
        print("------------------------------------------------")
        for result in hiscore_list:
            print(result)
        print("------------------------------------------------")
