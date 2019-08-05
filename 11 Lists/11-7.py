# Chapter 11. Lists
# http://openbookproject.net/thinkcs/python/english3e/lists.html


# Exercise 7
# ===========
# Write a function scalar_mult(s, v) that takes a number, s, and a list, v
# and returns the scalar multiple of v by s.

import sys


def dot_product(u, v):
    """ Takes two lists of numbers of the same length, and returns the sum
    of the products of the corresponding elements of each (the dot_product) """
    p = 0
    for i in range(len(u)):
        p += u[i] * v[i]
    return p


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    test(dot_product([1, 1], [1, 1]) ==  2)
    test(dot_product([1, 2], [1, 4]) ==  9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)


test_suite()