import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(len(Card.Card.suits)):
            for rank in range(1, len(Card.Card.ranks)):
                self.cards.append(Card.Card(suit, rank))

    def __str__(self):
        s = ''
        for i, card in enumerate(self.cards):
            blanks = ' ' * i
            s += f'{blanks}{card.rank} of {card.suit}\n'
        return s

    def shuffle(self):
        import random
        length = len(self.cards)
        for i in range(length):
            j = random.randrange(length)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def remove(self, card):
        '''  takes a card as a parameter, removes it, and returns True if
        the card was in the deck and False otherwise
        '''
        if card in self.cards:
            self.cards.remove(card)

    def pop(self):
        if not self.is_empty():
            return self.cards.pop()

    def is_empty(self):
        return self.cards == []


def main():
    red_deck = Deck()
    print(red_deck)

    red_deck.shuffle()
    print(red_deck)
    print(len(red_deck.cards))

    last_card = red_deck.pop()
    print(last_card)

    print(red_deck)
    print(len(red_deck.cards))


if __name__ == "__main__":
    main()