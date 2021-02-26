#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest

import cardhand
import deck
import card


class TestDiceClass(unittest.TestCase):
    """Testing cardhand class."""

    def setUp(self):
        """Instantiate cardhand to keep code D.R.Y."""
        self.cardhand = cardhand.Cardhand()

    def tearDown(self):
        """Delete cardhand instance after use."""
        del self.cardhand

    def test_init_default_object(self):
        """Test the instance and the hand attribute."""
        exp = cardhand.Cardhand
        self.assertIsInstance(self.cardhand, exp)

        exp = []
        res = self.cardhand.hand
        self.assertListEqual(exp, res)

    def test_cards_remaining(self):
        """Test if method returns right int."""
        res = self.cardhand.cards_remaining()
        exp = len(self.cardhand.hand)
        self.assertEqual(exp, res)

    def test_recieve_cards(self):
        """Test if method adds the cards recieved to hand."""
        this_deck = deck.Deck()
        this_deck.build_deck()
        this_deck.shuffle_deck()
        tot_cards = this_deck.deal_deck()
        recieved_cards = tot_cards[0]
        self.cardhand.recieve_cards(recieved_cards)
        res = self.cardhand.cards_remaining()
        self.assertEqual(len(recieved_cards), res)

    def test_war(self):
        """Test if war method works properly."""
        this_deck = deck.Deck()
        this_deck.build_deck()
        this_deck.shuffle_deck()
        tot_cards = this_deck.deal_deck()
        recieved_cards = tot_cards[0]
        self.cardhand.recieve_cards(recieved_cards)

        tot_res = self.cardhand.war()
        res = tot_res[0]
        self.assertIsInstance(res, list)
        self.assertEqual(len(res), 3)
        self.assertIsInstance(res[0], card.Card)

        res = tot_res[1]
        self.assertIsInstance(res, card.Card)
