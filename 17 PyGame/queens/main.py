import random
import pygame
import draw_queens
from board_transformations import *


def share_diagonal(x0,y0,x1,y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    return abs(x0 - x1) == abs(y0 - y1)


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):
        if share_diagonal(i,bs[i], c,bs[c]):
            return True
    return False


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for c in range(1, len(the_board)):
        if col_clashes(the_board, c):
            return True
    return False


def main():
    rng = random.Random()   # Instantiate a generator

    SIZE = 8
    MAX_ATTEMPTS_QUOTIENT = 100

    bd = list(range(SIZE))
    all_solutions = set()
    fundamentals = 0
    total_attempts = 0
    average_attempts = None

    attempts = 0

    while(True):
        rng.shuffle(bd)
        attempts += 1
        total_attempts += 1

        if average_attempts != None and \
            attempts == MAX_ATTEMPTS_QUOTIENT * average_attempts:
            break

        if not has_clashes(bd) and tuple(bd) not in all_solutions:

            symmetry_group = set()
            symmetry_group.add(tuple(bd))
            for trans in transformations:
                next_form = trans(bd)
                symmetry_group.add(tuple(next_form))

            all_solutions |= symmetry_group
            fundamentals += 1

            print("Next unique solution # {0:2}: {1} in {2} attempts".\
                format(fundamentals, bd, attempts), end=", ")
            print(f"{len(symmetry_group)} solutions in the symmetry group")
            average_attempts = total_attempts // fundamentals

            draw_queens.draw_board(bd)


    print(f"Found {len(all_solutions)} solutions, {fundamentals} fundanentals")
    print(f"{average_attempts} attempts per solution in average")


if __name__ == '__main__':
    main()

