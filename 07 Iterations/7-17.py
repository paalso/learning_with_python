## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html


## Exercise 17
## ===========


# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("\nHuman plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result


def game_results_print(human_wins, comp_wins, draws):
    print("\nScore")
    print("======")
    print("Total games:", total_games)
    print("Human wins:  ", human_wins, "   ", round(human_wins / total_games * 100, 1), "%", sep = "")
    print("Comp wins:   ", comp_wins, "   ", round(comp_wins / total_games * 100, 1), "%", sep = "")
    print("Draws:       ", draws, "   ", round(draws / total_games * 100, 1), "%", sep = "")


human_plays_first = True
total_games = 0
human_wins = 0
comp_wins = 0
draws = 0

while True:
    result = play_once(human_plays_first)
    total_games += 1
    if result == 0:
        draws += 1
        print("Game drawn!")
    elif result == 1 and human_plays_first \
        or result == -1 and not human_plays_first:
        human_wins += 1
        print("You win!")
    else:
        comp_wins += 1
        print("I win!")

    print("Current score:", human_wins + draws / 2, \
                        ":", comp_wins + draws / 2, end = "")
    if human_wins > comp_wins:
        print(" in your favour")
    elif comp_wins > human_wins:
        print(" in my favour")

    answer = "none"
    while True:
        answer = input("Do you want to play again (no / yes)?")
        if answer == "no" or answer == "yes":
            break
        print("Didn't understand")

    if answer == "no":
        break

game_results_print(human_wins, comp_wins, draws)
print("\nGoodby!")