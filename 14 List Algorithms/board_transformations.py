#-------------------------------------------------------------------------------
# Name:        board_transformations
# Purpose:
#
# Author:      PaulS
#
# Created:     07.10.2019
# Copyright:   (c) PaulS 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
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
"""

from testtools import test


def mirror_x(board):
    size = len(board)
    return [size - 1 - el for el in board]


def mirror_y(board):
    return board[::-1]


def turn_right(board):
    size = len(board)
    return [size - 1 - board.index(i) for i in range(size)]


def turn_right(board):
    size = len(board)
    return [size - 1 - board.index(i) for i in range(size)]


def turn_left(board):
    size = len(board)
    result = [0 for i in range(size)]
    for i in range(size):
        result[size - 1 - board[i]] = i
    return result


def turn_180(board):
    size = len(board)
    result = [0 for i in range(size)]
    for i in range(size):
        result[size - 1 - i] = size - 1 - board[i]
    return result


def turn_270(board):
    return turn_right(turn_180(board))


def turn_left_mirrored(board):
    return turn_left(mirror_x(board))


def turn_right_mirrored(board):
    return turn_right(mirror_x(board))


transformations = [ mirror_x, mirror_y, \
                    turn_left, turn_right, turn_180, \
                    turn_left_mirrored, turn_right_mirrored]


def generate_symmetry_group(bd):
    symmetry_group = [bd]
    for trans in transformations:
        symmetry_group.append(trans(bd))
    return symmetry_group

"""
# Tests
test(mirror_x([0]) == [0])
test(mirror_x([1,3,5,0,2,4]) == [4,2,0,5,3,1])

test(mirror_y([0]) == [0])
test(mirror_y([1,3,5,0,2,4]) == [4,2,0,5,3,1])

test(turn_right([0]) == [0])
test(turn_right([1,3,5,0,2,4]) == [2,5,1,4,0,3])
test(turn_right([3,0,2,5,1,6,4]) == [5,2,4,6,0,3,1])

test(turn_left([0]) == [0])
test(turn_left([1,3,5,0,2,4]) == [2,5,1,4,0,3])
test(turn_left([3,0,2,5,1,6,4]) == [5,3,6,0,2,4,1])

test(turn_180([0]) == [0])
test(turn_180([1,3,5,0,2,4]) == [1,3,5,0,2,4])
test(turn_180([3,0,2,5,1,6,4]) == [2,0,5,1,4,6,3])
"""

##bd = [3, 5, 7, 1, 6, 0, 2, 4]
##g = generate_symmetry_group(bd)
##print(g)