import unittest

import sys
sys.path.append('../')

# import cards, pokerhand
from cards import Card
from pokerhand import PokerHand


class TestPokerHand(unittest.TestCase):
    def setUp(self):
        self.ph = PokerHand()

        self.cards_set_with_two_pair = [Card(1,1), Card(2,1), Card(0,3),
                Card(2,3), Card(2,5), Card(2,6), Card(2,7)]

        self.cards_set_without_two_pair_1 = [Card(1,1), Card(2,1), Card(3,1),
                Card(2,4), Card(2,5), Card(2,6), Card(2,7)]

        self.cards_set_without_two_pair_2 = [Card(1,1), Card(2,1), Card(3,3),
                Card(2,4), Card(2,5), Card(2,6), Card(2,7)]


    def test_deck_with_two_pair(self):
        self.ph.add_cards(self.cards_set_with_two_pair)
        self.assertTrue(self.ph.has_twopair())

    def test_deck_without_pair_1(self):
        self.ph.add_cards(self.cards_set_without_two_pair_1)
        self.assertFalse(self.ph.has_twopair())

    def test_deck_without_pair_2(self):
        self.ph.add_cards(self.cards_set_without_two_pair_2)
        self.assertFalse(self.ph.has_twopair())


unittest.main()
