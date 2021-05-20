import unittest

import sys
sys.path.append('../')

# import cards, pokerhand
from cards import Card
from pokerhand import PokerHand


class TestPokerHand(unittest.TestCase):
    def setUp(self):
        self.ph = PokerHand()

        self.cards_set_with_pair_1 = [Card(1,1), Card(2,1), Card(2,3),
                Card(2,4), Card(2,5), Card(2,6), Card(2,7)]

        self.cards_set_with_pair_2 = [Card(1,11), Card(2,1), Card(2,3),
                Card(2,4), Card(2,5), Card(2,6), Card(2,11)]

        self.cards_set_with_pair_3 = [Card(0,2), Card(2,1), Card(2,3),
                Card(2,4), Card(2,5), Card(2,2), Card(2,11)]

        self.cards_set_without_pair_1 = [Card(1,1), Card(2,10), Card(2,3),
                Card(2,4), Card(2,5), Card(2,6), Card(2,7)]

        self.cards_set_without_pair_2 = [Card(1,1), Card(2,10), Card(2,3),
                Card(2,11), Card(2,5), Card(2,6), Card(2,7)]

        self.cards_set_without_pair_3 = [Card(1,1), Card(2,10), Card(2,3),
                Card(2,4), Card(2,5), Card(2,6), Card(2,2)]


    def test_deck_with_pair_1(self):
        self.ph.add_cards(self.cards_set_with_pair_1)
        self.assertTrue(self.ph.has_pair())

    def test_deck_with_pair_2(self):
        self.ph.add_cards(self.cards_set_with_pair_1)
        self.assertTrue(self.ph.has_pair())

    def test_deck_with_pair_3(self):
        self.ph.add_cards(self.cards_set_with_pair_1)
        self.assertTrue(self.ph.has_pair())

    def test_deck_without_pair_1(self):
        self.ph.add_cards(self.cards_set_without_pair_1)
        self.assertFalse(self.ph.has_pair())

    def test_deck_without_pair_2(self):
        self.ph.add_cards(self.cards_set_without_pair_2)
        self.assertFalse(self.ph.has_pair())

    def test_deck_without_pair_3(self):
        self.ph.add_cards(self.cards_set_without_pair_3)
        self.assertFalse(self.ph.has_pair())


unittest.main()
