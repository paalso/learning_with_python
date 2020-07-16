import Deck, Hand, Card


class CardGame:
    deck = Deck.Deck()
    deck.shuffle()


class OldMaidHand(Hand.Hand):
    def remove_matches(self):
        counter = 0
        hand_copy = self.cards[:]
        for card in hand_copy:
            matching_card = Card.Card(3 - card.suit, card.rank)
            if matching_card in self.cards:
                print('Hand {}: {} matches {}'
                    .format(self.name, str(card), str(matching_card)))
                self.remove(card)
                self.remove(matching_card)
                counter += 1
        return counter


class OldMaidGame(CardGame):
    ''' OldMaidGame is a subclass of CardGame with a new method called play
    that takes a list of players as a parameter.
    '''
    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card.Card(0, 12))

        # Make a hand for each player
        self.hands = list(map(lambda name: OldMaidHand(name), names))

        # Deal the cards
        self.deck.deal(self.hands)
        print('---------- GAME BEGINS!')
        print('---------- Cards have been dealt')
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print('---------- Matches discarded, play begins')
        self.print_hands()

        # Play until all 50 cards are matched
        player = 0
        turns = 0
        num_hands = len(names)
        while matches < 25:
            if self.hands[player].size() != 0:
                matches += self.play_one_turn(player)
                turns += 1
            player = (player + 1) % num_hands

        print("---------- Game is Over in {} turns".format(turns))
        self.print_hands()

    def remove_all_matches(self):
        ''' Returns total count of removed matches'''
        counter = 0
        for hand in self.hands:
            counter += hand.remove_matches()
        return counter

    def print_hands(self):
        for hand in self.hands:
            print(hand)

    # ----------------------------------
    def play_one_turn(self, i):
        neighbor = self.find_neighbor(i)
        card = self.hands[neighbor].pop()
        self.hands[i].cards.append(card)
        print('Hand {} picked {}'.format(self.hands[i].name, card))
        self.hands[i].shuffle()
        return self.hands[i].remove_matches()

    def find_neighbor(self, i):
        players_qty = len(self.hands)
        for j in range(1, players_qty):
            player_number = (i + j) % players_qty
            if self.hands[player_number].size():
                return player_number

def main():
    game = OldMaidGame()
    names = 'Tom', 'Dick', 'Harry'
    game.play(names)


if __name__ == "__main__":
    main()