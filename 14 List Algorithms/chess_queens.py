# Chapter 14. List Algorithms
# http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html

# Exercise 2
# ===========
# Modify the queens program to solve some boards of size 4, 12, and 16.
# What is the maximum size puzzle you can usually solve in under a minute?

from testtools import test

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
    import random
    rng = random.Random()   # Instantiate a generator

    different_positions = 1
    size = 10
    bd = list(range(size))

    for i in range(different_positions):
        attempts = 0
        while(True):
            rng.shuffle(bd)
            attempts += 1
            if not has_clashes(bd):
                print("Found solution {0} in {1} attempts".format(bd, attempts))
                break


main()
