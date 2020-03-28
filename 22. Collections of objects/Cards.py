class Card:
    # A class attribute is defined outside of any method, and it can be accessed
    # from any of the methods in the class.
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(self.ranks[self.rank], self.suits[self.suit])

    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same... check ranks

        self_rank = self.rank if self.rank != 1 else 14
        other_rank = other.rank if other.rank != 1 else 14
                                                # Modify cmp so that
        if self_rank  > other_rank: return 1    # Aces are ranked
        if self_rank < other_rank: return -1    # higher than Kings
        # Ranks are the same... it's a tie
        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(len(Card.suits)):
            for j in range(1, len(Card.ranks)):
                self.cards.append(Card(i, j))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop(0)

    def is_empty(self):
        return self.cards == []


# Chapter 22. Collections of objects
# http://openbookproject.net/thinkcs/python/english3e/collections.html

# Modify cmp so that Aces are ranked higher than Kings

card_two = Card(0, 2)
card_ace = Card(0, 1)
card_king = Card(0, 13)
card_ace_2 = Card(0, 1)

print(card_ace.cmp(card_two))
print(card_ace.cmp(card_king))
print(card_ace.cmp(card_ace_2))
