import unittest

import sys
sys.path.append('../')

# import cards, pokerhand
from cards import Card
from pokerhand import PokerHand


class TestPokerHand(unittest.TestCase):
    def setUp(self):
        self.ph = PokerHand()

        self.cards_set_with_None = [Card(0,2), Card(1,4), Card(2,6),
                Card(3,8), Card(3,3)]

        self.cards_set_with_straight_flash = [Card(2,7), Card(2,8), Card(2,10),
                Card(2,11), Card(2,9)]

        self.cards_set_with_four = [Card(2,7), Card(2,8), Card(1,7),
                Card(0,7), Card(4,7)]

        self.cards_set_with_fullhouse = [Card(0,6), Card(1,6), Card(3,6),
                Card(0,13), Card(4,13)]

        self.cards_set_with_flash = [Card(2,10), Card(2,9), Card(2,5),
                Card(2,6), Card(2,3)]

        self.cards_set_with_straight = [Card(2,5), Card(1,7), Card(0,6),
                Card(1,9), Card(0,8)]

        self.cards_set_with_three = [Card(0,2), Card(1,2), Card(2,6),
                Card(3,8), Card(3,2)]

        self.cards_set_with_two_pair = [Card(0,2), Card(1,2), Card(2,6),
                Card(3,8), Card(3,6)]

        self.cards_set_with_pair = [Card(0,2), Card(1,2), Card(2,6),
                Card(3,8), Card(3,3)]

    def test_deck_with_straight_flash(self):
        self.ph.add_cards(self.cards_set_with_straight_flash)
        self.assertEqual(self.ph.classify(), "Straight flush")

    def test_deck_with_straight_four(self):
        self.ph.add_cards(self.cards_set_with_four)
        self.assertEqual(self.ph.classify(), "Four of a kind")

    def test_deck_set_with_fullhouse(self):
        self.ph.add_cards(self.cards_set_with_fullhouse)
        self.assertEqual(self.ph.classify(), "Full house")

    def test_deck_with_flash(self):
        self.ph.add_cards(self.cards_set_with_flash)
        self.assertEqual(self.ph.classify(), "Flush")

    def test_deck_with_straight(self):
        self.ph.add_cards(self.cards_set_with_straight)
        self.assertEqual(self.ph.classify(), "Straight")

    def test_deck_with_three(self):
        self.ph.add_cards(self.cards_set_with_three)
        self.assertEqual(self.ph.classify(), "Three of a kind")

    def test_deck_with_pair(self):
        self.ph.add_cards(self.cards_set_with_pair)
        self.assertEqual(self.ph.classify(), "One pair")

    def test_deck_with_two_pair(self):
        self.ph.add_cards(self.cards_set_with_two_pair )
        self.assertEqual(self.ph.classify(), "Two pair")

    def test_deck_with_None(self):
        self.ph.add_cards(self.cards_set_with_None)
        self.assertEqual(self.ph.classify(), None)


unittest.main()

