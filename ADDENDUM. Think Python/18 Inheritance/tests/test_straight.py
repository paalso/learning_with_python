import unittest

import sys
sys.path.append('../')

# import cards, pokerhand
from cards import Card
from pokerhand import PokerHand


class TestPokerHand(unittest.TestCase):
    def setUp(self):
        self.ph = PokerHand()

        self.cards_set_with_straight_1 = [Card(1,13), Card(2,12), Card(2,11),
                Card(0,10), Card(3,9), Card(2,6), Card(2,7)]

        self.cards_set_with_straight_2 = [Card(0,5), Card(2,6), Card(2,11),
                Card(3,7), Card(0,4), Card(2,6), Card(1,8)]

        self.cards_set_with_straight_3 = [Card(0,5), Card(2,6), Card(2,2),
                Card(3,4), Card(0,3)]

        self.cards_set_with_straight_4 = [Card(0,1), Card(2,3), Card(2,2),
                Card(3,5), Card(0,4)]

        self.cards_set_with_straight_5 = [Card(0,11), Card(2,10), Card(2,1),
                Card(3,12), Card(0,13)]

        self.cards_set_without_straight_1 = [Card(1,1), Card(2,1), Card(3,2),
                Card(0,2), Card(2,5), Card(2,6), Card(2,7)]

        self.cards_set_without_straight_2 = [Card(0,11), Card(2,10), Card(2,10),
                Card(3,12), Card(0,10)]

    def test_deck_with_straight_1(self):
        self.ph.add_cards(self.cards_set_with_straight_1)
        self.ph.init_hists()
        self.assertTrue(self.ph.has_straight())

    def test_deck_with_straight_2(self):
        self.ph.add_cards(self.cards_set_with_straight_2)
        self.assertTrue(self.ph.has_straight())

    def test_deck_with_straight_3(self):
        self.ph.add_cards(self.cards_set_with_straight_3)
        self.assertTrue(self.ph.has_straight())

    def test_deck_with_straight_4(self):
        self.ph.add_cards(self.cards_set_with_straight_4)
        self.assertTrue(self.ph.has_straight())

    def test_deck_with_straight_5(self):
        self.ph.add_cards(self.cards_set_with_straight_5)
        self.ph.init_hists()
        self.assertTrue(self.ph.has_straight())

    def test_deck_without_straight_1(self):
        self.ph.add_cards(self.cards_set_without_straight_1)
        self.assertFalse(self.ph.has_straight())

    def test_deck_without_straight_2(self):
        self.ph.add_cards(self.cards_set_without_straight_2)
        self.assertFalse(self.ph.has_straight())



unittest.main()
