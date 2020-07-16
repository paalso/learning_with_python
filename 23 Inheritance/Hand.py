import Deck, Card

class Hand(Deck.Deck):

    def __init__(self, name=""):
        self.name = name
        self.cards = []

    def __str__(self):
        s = f'Hand {self.name} '
        if self.is_empty():
            return s + 'is empty\n'
        s += f'contains {len(self.cards)} cards:\n'
        return s + Deck.Deck.__str__(self)

    def add(self, card):
        self.cards.append(card)

    def print(self):
        print(str(self))

    def size(self):
        return len(self.cards)


def main():
    deck = Deck.Deck()
    deck.shuffle()
    hand = Hand("frank")
    deck.deal([hand], 5)
    print(hand)


if __name__ == "__main__":
    main()