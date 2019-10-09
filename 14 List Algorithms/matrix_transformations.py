#-------------------------------------------------------------------------------
# Name:        matrix_transformations
# Purpose:
#
# Author:      PaulS
#
# Created:     07.10.2019
# Copyright:   (c) PaulS 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from testtools import test


def flipped_horizontal(matrix):
    flipped_matrix = []
    for row in matrix:
        flipped_matrix.append(list(reversed(row)))
    return flipped_matrix


def flipped_vertical(matrix):
    flipped_matrix = []
    for row in matrix[::-1]:
        flipped_matrix.append(row)
    return flipped_matrix


def test_suite_flip_horizontal():
    print("Testing 'flipped_horizontal()':")
    m1 = [[1]]
    m2 = [[1,2],
          [3,4]]
    m3 = [[1,2,3],
          [4,5,6],]
    m4 = [[1,2,3,4,5],
          [6,7,8,9,8],
          [0,1,8,5,7],
          [5,1,2,3,0]]

    test(flipped_horizontal(m1) == [[1]])
    test(flipped_horizontal(m2) == [[2,1],
                                    [4,3]])
    test(flipped_horizontal(m3) == [[3,2,1],
                                    [6,5,4]])
    test(flipped_horizontal(m4) == [[5,4,3,2,1],
                                    [8,9,8,7,6],
                                    [7,5,8,1,0],
                                    [0,3,2,1,5]])


def test_suite_flip_vertical():
    print("Testing 'flipped_horizontal()':")
    m1 = [[1]]
    m2 = [[1,2],
          [3,4]]
    m3 = [[1,2,3],
          [4,5,6],]
    m4 = [[1,2,3,4,5],
          [6,7,8,9,8],
          [0,1,8,5,7],
          [5,1,2,3,0]]
    m5 = [[5,4],
          [8,9],
          [7,5],
          [6,1],
          [0,3]]

    test(flipped_vertical(m1) == [[1]])
    test(flipped_vertical(m2) == [[3,4],
                                  [1,2]])
    test(flipped_vertical(m3) == [[4,5,6],
                                  [1,2,3]])
    test(flipped_vertical(m4) == [[5,1,2,3,0],
                                  [0,1,8,5,7],
                                  [6,7,8,9,8],
                                  [1,2,3,4,5]])
    test(flipped_vertical(m5) == [[0,3],
                                  [6,1],
                                  [7,5],
                                  [8,9],
                                  [5,4]])


test_suite_flip_horizontal()
test_suite_flip_vertical()

##m4 = [[1,2,3,4,5],
##      [6,7,8,9,8],
##      [0,1,8,5,7],
##      [5,1,2,3,0]]
##print(flipped_vertical(m4))