# Chapter 11. Lists
# http://openbookproject.net/thinkcs/python/english3e/lists.html


# Exercise 5
# ===========
# Lists can be used to represent mathematical vectors...
# Write a function add_vectors(u, v) that takes two lists of numbers of
# the same length, and returns a new list containing the sums of
# the corresponding elements of each:

import sys


def add_vectors(u, v):
    """ Takes two lists of numbers of the same length, and returns a new list
    containing the sums of the corresponding elements of each """
    result = []
    for i in range(len(u)):
        result.append(u[i] + v[i])
    return result


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    test(add_vectors([], []) == [])
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])


test_suite()