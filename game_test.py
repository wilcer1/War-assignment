# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unittesting game."""

import unittest
import game
import player
import card
import deck


class TestGameClass(unittest.TestCase):
    """Testing game class."""

    def setUp(self):
        """Instantiate game in setUp to keep code D.R.Y."""
        self.game = game.Game()

    def tearDown(self):
        """Delete setup instance after usage."""
        del self.game

    def test_init_default_object(self):
        """Check if self.game is instance of Game."""
        exp = game.Game
        self.assertIsInstance(self.game, exp)

    def test_set_get_players(self):
        """Test the setters and getters."""
        with self.assertRaises(ValueError):
            self.game.set_player(3, "Wille")

        with self.assertRaises(TypeError):
            self.game.set_player(1, 5)

        res = self.game.get_players()
        exp = (None, None)
        self.assertEqual(res, exp)

        self.game.set_player(1, "Wille")
        self.game.set_player(2, "Timmy")
        self.game.start()
        res = self.game.get_players()
        p_1 = res[0]
        p_2 = res[1]
        self.assertIsInstance(p_1, player.Player)
        self.assertIsInstance(p_2, player.Player)

        res = p_1.name
        exp = "Wille"
        self.assertEqual(res, exp)
        res = p_2.name
        exp = "Timmy"
        self.assertEqual(exp, res)

    def test_set_player_name(self):
        """Test if method changes player name."""
        self.game.set_player(1, "Wille")
        p_1 = self.game.player1
        exp = "Lucas"
        self.game.set_player_name("Lucas", p_1)
        self.assertEqual(exp, p_1.name)

    def test_start(self):
        """Test start method."""
        self.game.set_player(1, "Wille")
        self.game.start()
        p_1, p_2 = self.game.get_players()
        res = p_1.cardhand.cards_remaining()
        self.assertEqual(res, 26)
        res = p_2.cardhand.cards_remaining()
        self.assertEqual(res, 26)

    def test_draw(self):
        """Test continue method."""
        res = self.game.draw()
        exp = "Create player(s) and start game first"
        self.assertEqual(res, exp)

        self.game.set_player(1, "Wille")
        self.game.start()
        p_1, p_2 = self.game.get_players()
        p_1_card, p2_card = self.game.draw()
        res1 = p_1.cardhand.cards_remaining()
        res2 = p_2.cardhand.cards_remaining()
        self.assertEqual(res1, 25)
        self.assertEqual(res2, 25)

        self.assertIsInstance(p_1_card, card.Card)
        self.assertIsInstance(p2_card, card.Card)

    def test_round_winner(self):
        """Test round_winner method."""
        self.game.set_player(1, "Wille")
        self.game.start()
        p_1, p_2 = self.game.get_players()
        p_1_card = card.Card("Diamonds", 5)
        p2_card = card.Card("Diamonds", 4)
        self.game.round_winner(p_1_card, p2_card)
        self.assertNotEqual(p_1.cardhand.cards_remaining(),
                            p_2.cardhand.cards_remaining())

        p_1_card = card.Card("Diamonds", 11)
        p2_card = card.Card("Diamonds", 13)
        self.game.round_winner(p_1_card, p2_card)
        self.assertEqual(p_1.cardhand.cards_remaining(),
                         p_2.cardhand.cards_remaining())

        self.game.start()
        p_1, p_2 = self.game.get_players()
        self.game.draw()
        p_1_card = card.Card("Diamonds", 5)
        p2_card = card.Card("Clubs", 5)
        self.game.round_winner(p_1_card, p2_card)
        exp = p_1.cardhand.cards_remaining() > p_2.cardhand.cards_remaining()\
            or p_2.cardhand.cards_remaining() > p_1.cardhand.cards_remaining()
        self.assertTrue(exp)

    def test_war(self):
        """Test the war class."""
        self.game.set_player(1, "Wille")
        self.game.start()
        p_1, p_2 = self.game.get_players()
        self.game.war([])
        exp = p_1.cardhand.cards_remaining() > p_2.cardhand.cards_remaining()\
            or p_2.cardhand.cards_remaining() > p_1.cardhand.cards_remaining()
        self.assertTrue(exp)

        p_1.cardhand.hand.clear()
        cardlist = []
        crd_1 = card.Card("Diamonds", 2)
        crd_2 = card.Card("Diamonds", 5)
        cardlist.append(crd_1)
        cardlist.append(crd_2)
        p_1.cardhand.recieve_cards(cardlist)
        pre_war = p_1.cardhand.cards_remaining()
        self.game.war([])
        post_war = p_1.cardhand.cards_remaining()
        self.assertNotEqual(pre_war, post_war)

        self.game.start()
        p_2.cardhand.hand.clear()
        p_2.cardhand.recieve_cards(cardlist)
        pre_war = p_2.cardhand.cards_remaining()
        self.game.war([])
        post_war = p_2.cardhand.cards_remaining()
        self.assertNotEqual(pre_war, post_war)

    def test_check_cards(self):
        """Test check cards method."""
        self.game.set_player(1, "Wille")
        self.game.set_player(2, "Timmy")
        p_1, p_2 = self.game.get_players()
        cards = []
        card1 = card.Card("Diamonds", 5)
        cards.append(card1)
        p_1.cardhand.recieve_cards(cards)
        p_2.cardhand.recieve_cards(cards)
        self.assertTrue(self.game.check_cards())

        dck = deck.Deck()
        dck.build_deck()
        dck1 = dck.get_deck()
        p_1.cardhand.recieve_cards(dck1)
        self.assertTrue(self.game.check_cards())

        self.game.start()
        self.assertFalse(self.game.check_cards())

    def test_check_for_winner(self):
        """Test checkforwinner method."""
        self.game.set_player(1, "Wille")
        self.game.set_player(2, "Timmy")
        p_1, p_2 = self.game.get_players()
        self.assertTrue(self.game.check_for_winner())
        crd = card.Card("Diamonds", 5)
        p_1.cardhand.hand.append(crd)
        self.assertTrue(self.game.check_for_winner())
        p_2.cardhand.hand.append(crd)
        self.assertFalse(self.game.check_for_winner())
