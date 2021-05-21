"""
Exercise 18.3. The following are the possible hands in poker,
in increasing order of value and
decreasing order of probability:
- pair: two cards with the same rank
- two pair: two pairs of cards with the same rank
- three of a kind: three cards with the same rank
- straight: five cards with ranks in sequence (aces can be high or low,
so Ace-2-3-4-5 is a straight
and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)
- flush: five cards with the same suit
- full house: three cards with one rank, two cards with another
- four of a kind: four cards with the same rank
- straight flush: five cards in sequence (as defined above) and with the same suit
"""

import collections
import cards


def max_inc_per_one_length(L, i):
    counter = 1
    len_ = len(L)
    sortedL = sorted(L)
    while i < len_ - 1 and sortedL[i + 1] - sortedL[i] == 1:
        counter += 1
        i += 1
    return counter, i


class PokerHand(cards.Hand):
    """Represents a poker hand."""

##    def __init__(self, label=""):
##        super().__init__(label)

    def add_cards(self, *cards):
        super().add_cards(*cards)
        self.init_hists()

    def init_hists(self):
        """Builds both suits and ranks histograms of the hand.
        Stores the result in attribute dictionaries. """
        self.__suit_hist()
        self.__rank_hist()

    def __suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits. """
        self.suits = dict()
        for crd in self.cards:
            self.suits[crd.suit] = self.suits.get(crd.suit, 0) + 1

    def __ranks_by_suits_hist(self):
        """Builds a histogram of the ranks in reverence to the suits that
        appear in the hand
        Stores the result in attribute ranks_by_suits. """
        self.ranks_by_suits = dict()
        for crd in self.cards:
            self.ranks_by_suits.setdefault(crd.suit, []).append(crd.rank)

    def __rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.
        Stores the result in attribute ranks. """
        self.ranks = dict()
        for crd in self.cards:
            self.ranks[crd.rank] = self.ranks.get(crd.rank, 0) + 1

    def print_suits(self):
        if 'suits' not in self.__dict__:
            self.__suit_hist()
        print('Suits:')
        print('-------')
        for suit_id in sorted(self.suits):
            print(cards.Card.suits[suit_id], self.suits[suit_id])

    def print_ranks(self):
        if 'ranks' not in self.__dict__:
            self.__rank_hist()
        print('Ranks:')
        print('-------')
        for rank_id in sorted(self.ranks):
            print(cards.Card.ranks[rank_id], self.ranks[rank_id])

    # Add methods to PokerHand.py named has_pair, has_twopair, etc. that
    # return True or False according to whether or not the hand meets
    # the relevant criteria. Your code should work correctly for “hands” that
    # contain any number of cards (although 5 and 7 are the most common sizes).

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise."""
        return list(self.ranks.values()).count(2) >= 1

    def has_twopair(self):
        """Returns True if the hand has a two pair, False otherwise."""
        return list(self.ranks.values()).count(2) >= 2

    def has_three(self):
        """Returns True if the hand has a three of a kind, False otherwise."""
        return list(self.ranks.values()).count(3) >= 1

    def has_straight(self):
        return self.__has_straight(sorted(self.ranks))

    def __has_straight(self, ranks_):
        if set((1, 10, 11, 12, 13)).issubset(set(ranks_)):
            return True
        for i in range(len(ranks_) - 4):
            len_, _ = max_inc_per_one_length(ranks_, i)
            if  len_ >= 5:
                return True
        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
        Note that this works correctly for hands with more than 5 cards. """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_fullhouse(self):
        """Returns True if the hand has a full house, False otherwise. """
        ranks_values = list(self.ranks.values())
        return ranks_values.count(3) == 1 and ranks_values.count(2) == 1

    def has_four(self):
        """Returns True if the hand has a four of a kind, False otherwise."""
        return list(self.ranks.values()).count(4) >= 1

    def has_straightflush(self):
        self.__ranks_by_suits_hist()
        for ranks_ in self.ranks_by_suits.values():
            if self.__has_straight(ranks_):
                return True
        return False

    poker_hands = collections.OrderedDict({
        has_straightflush: "Straight flush",
        has_four: "Four of a kind",
        has_fullhouse: "Full house",
        has_flush: "Flush",
        has_straight: "Straight",
        has_three: "Three of a kind",
        has_twopair: "Two pair",
        has_pair: "One pair"
    })

    def classify(self):
        self.combinations = [PokerHand.poker_hands[predicate]
                for predicate in PokerHand.poker_hands.keys()
                if predicate(self)]
        return self.combinations

    @classmethod
    def deal_hands(cls, hands_number, cards_per_hand):
        deck = cards.Deck()
        deck.shuffle()

        if deck.size() < hands_number * cards_per_hand:
            cards_per_hand = len(self.cards) // hands_number

        hands = [PokerHand() for _ in range(hands_number)]

        for i in range(hands_number):
            deck.move_cards(hands[i], cards_per_hand)
            hands[i].init_hists()

        return hands
