import unittest

import sys
sys.path.append('../')

# import cards, pokerhand
from cards import Card
from pokerhand import PokerHand


class TestPokerHand(unittest.TestCase):
    def setUp(self):
        self.ph = PokerHand()

        self.cards_set_with_flash = [Card(1,2), Card(2,2), Card(2,10),
                Card(2,9), Card(2,5), Card(2,6), Card(3,5)]

        self.cards_set_without_flash = [Card(1,2), Card(2,2), Card(2,10),
                Card(2,9), Card(2,5), Card(3,5)]

    def test_deck_with_flash(self):
        self.ph.add_cards(self.cards_set_with_flash)
        self.assertTrue(self.ph.has_flush())

    def test_deck_without_flash(self):
        self.ph.add_cards(self.cards_set_without_flash)
        self.assertFalse(self.ph.has_flush())


unittest.main()

