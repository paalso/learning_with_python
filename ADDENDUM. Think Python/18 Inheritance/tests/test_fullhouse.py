import unittest

import sys
sys.path.append('../')

# import cards, pokerhand
from cards import Card
from pokerhand import PokerHand


class TestPokerHand(unittest.TestCase):
    def setUp(self):
        self.ph = PokerHand()

        self.cards_set_with_fullhouse_1 = [Card(1,1), Card(2,1), Card(3,1),
                Card(2,4), Card(3,4), Card(2,6), Card(2,7)]

        self.cards_set_with_fullhouse_2 = [Card(3,10), Card(2,10), Card(1,1),
                Card(3,1), Card(0,10), Card(2,6), Card(2,7)]

        self.cards_set_without_fullhouse = [Card(1,1), Card(2,1), Card(3,1),
                Card(2,4), Card(2,5), Card(2,6), Card(2,7)]


    def test_deck_with_fullhouse_1(self):
        self.ph.add_cards(self.cards_set_with_fullhouse_1)
        self.assertTrue(self.ph.has_fullhouse())

    def test_deck_with_fullhouse_2(self):
        self.ph.add_cards(self.cards_set_with_fullhouse_2)
        self.assertTrue(self.ph.has_fullhouse())

    def test_deck_without_fullhouse(self):
        self.ph.add_cards(self.cards_set_without_fullhouse)
        self.assertFalse(self.ph.has_fullhouse())


unittest.main()
