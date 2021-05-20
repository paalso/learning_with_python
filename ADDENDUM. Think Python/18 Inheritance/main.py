import cards, pokerhand
from cards import Card


def evaluate_probabilities(experiments_number,
        hands_number=7, cards_per_hand =7):

    poker_combinations = ["Straight flush", "Four of a kind", "Full house",
            "Flush", "Straight", "Three of a kind", "Two pair", "One pair"]
    frequencies = {comb: 0 for comb in poker_combinations}

    for _ in range(experiments_number):
        poker_hands = pokerhand.PokerHand.deal_hands(
                hands_number, cards_per_hand)
        for ph in poker_hands:
            combination = ph.classify()
            if combination:
                frequencies[combination] += 1

    dealing_number = experiments_number * hands_number
    probabilities = {comb: frequencies[comb] / dealing_number
            for comb in poker_combinations}

    return probabilities


def main():
    experiments_number = 10000
    hands_number, cards_per_hand = 7, 7

    print("Probabilities of poker combinations (dealing with {} cards:)"
            .format(cards_per_hand))
    print("============================================================\n")

    for comb, val in evaluate_probabilities(experiments_number,
            hands_number, cards_per_hand).items():
            if val:
                print("{:<15} {:>8.4%} (one time in {:>7.2f})"
                        .format(comb, val, round(1/val, 2)))
            else:
                print("{:<15} {:>8.4%} (one time in    --- )"
                        .format(comb, val))

if __name__ == '__main__':
    main()
