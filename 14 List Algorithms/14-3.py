# Chapter 14. List Algorithms
# http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html

# Exercise 3
# ===========
# Adapt the queens program so that we keep a list of solutions that have already
# printed, so that we don’t print the same solution more than once.

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

    different_positions = 4
    size = 4
    bd = list(range(size))
    solutions_list = []

    for i in range(different_positions):
        attempts = 0
        while(True):
            rng.shuffle(bd)
            attempts += 1
            print(bd)
##            print("{0}, {1}".format(bd, ))
            if not has_clashes(bd) and bd not in solutions_list:
                solutions_list.append(bd)
                print("Found next unique solution {0} in {1} attempts".\
                    format(bd, attempts))
                break


main()
