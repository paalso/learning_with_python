import random

class Card:
    """Represents a standard playing """

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King" ]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{Card.ranks[self.rank]} of {Card.suits[self.suit]}"

    def __eq__(self, other):
        return (self.suit, self.rank) == (other.suit, other.rank)

    def __lt__(self, other):
        return (self.suit, self.rank) < (other.suit, other.rank)

    def __gt__(self, other):
        return (self.suit, self.rank) > (other.suit, other.rank)


class Deck:

    def __init__(self):
        self.cards = []
        for i in range(len(Card.suits)):
            for j in range(1, len(Card.ranks)):
                self.cards.append(Card(i, j))

    def __str__(self):
        return "\n".join(map(str, self.cards))

    def size(self):
        return len(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

    def add_cards(self, *cards):
        if type(cards[0]) == list:
            self.__add_cards_list(cards[0])
        else:
            self.__add_cards_list(cards)

    def __add_cards_list(self, cards_list):
        for card in cards_list:
            self.add_card(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def clear(self):
        self.cards.clear()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.
        hand: destination Hand object
        num: integer number of cards to move
        """
        for _ in range(num):
            hand.add_card(self.pop_card())

    # Exercise 18.2.
    def deal_hands(self, hands_number, cards_per_hand):
        """ Creates 'hands_number' of Hand objects, deals 'cards_per_hands'
        per hand, returns a list of Hands. """

        if self.size() < hands_number * cards_per_hand:
            cards_per_hand = len(self.cards) // hands_number

        hands = [hand.Hand() for _ in range(hands_number)]

        self.shuffle()
        for i in range(hands_number):
            self.move_cards(hands[i], cards_per_hand)

        return hands


class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=""):
        self.label = label
        self.cards = []

    def __str__(self):
        header = f"Hand '{self.label}':\n"
        self.cards.sort()
        result = ""
        for crd in self.cards:
            result += f"{'  ' * crd.suit}{crd}\n"
        return result
