# Chapter 14. List Algorithms
# http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html

# Exercise 4
# ===========
"""
Chess boards are symmetric: if we have a solution to the queens problem,
its mirror solution — either flipping the board on the X or in the Y axis,
is also a solution. And giving the board a 90 degree, 180 degree, or
270 degree rotation is also a solution. In some sense, solutions that are
just mirror images or rotations of other solutions — in the same family —
are less interesting than the unique “core cases”. Of the 92 solutions for
the 8 queens problem, there are only 12 unique families if you take rotations
and mirror images into account.

a. Write a function to mirror a solution in the Y axis,
b. Write a function to mirror a solution in the X axis,
c. Write a function to rotate a solution by 90 degrees anti-clockwise, and
use this to provide 180 and 270 degree rotations too.
d. Write a function which is given a solution, and it generates the family
of symmetries for that solution. For example, the symmetries of
[0,4,7,5,2,6,1,3] are
[[0,4,7,5,2,6,1,3],[7,1,3,0,6,4,2,5],
 [4,6,1,5,2,0,3,7],[2,5,3,1,7,4,6,0],
 [3,1,6,2,5,7,4,0],[0,6,4,7,1,3,5,2],
 [7,3,0,2,5,1,6,4],[5,2,4,6,0,3,1,7]]

Now adapt the queens program so it won’t list solutions that are in the same
family. It only prints solutions from unique families.
"""

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
    import random
    rng = random.Random()   # Instantiate a generator

    SIZE = 9
    MAX_ATTEMPTS_QUOTIENT = 50

    different_positions = 300
    bd = list(range(SIZE))
    all_solutions = []
    uniq_solutions = 0
    total_attempts = 0
    average_attempts = None
    flag = False

    for i in range(different_positions):
        attempts = 0

        while(True):
            rng.shuffle(bd)
            attempts += 1
            total_attempts += 1

            if average_attempts != None and \
                        attempts % (10 * average_attempts) == 0:
                print(f"{attempts} attempts, average = {average_attempts}")

            if average_attempts != None and \
                        attempts > MAX_ATTEMPTS_QUOTIENT * average_attempts:
                flag = True
                break

            if not has_clashes(bd) and bd not in all_solutions:

                symmetry_group = [bd.copy()]
                for trans in transformations:
                    next_form = trans(bd)
                    if next_form not in symmetry_group:
                        symmetry_group.append(next_form)

                all_solutions.extend(symmetry_group.copy())

                uniq_solutions += 1
                print("Next unique solution # {0:2}: {1} in {2} attempts".\
                    format(uniq_solutions, bd, attempts), end=", ")
                print(f"{len(symmetry_group)} solutions in the symmetry group")
                average_attempts = total_attempts // uniq_solutions

                break

    print(f"Found {len(all_solutions)} solutions")
    print(f"{average_attempts} attempts per solution in average")
    if flag: print("Special break")



main()
