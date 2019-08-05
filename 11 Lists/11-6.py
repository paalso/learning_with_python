# Chapter 11. Lists
# http://openbookproject.net/thinkcs/python/english3e/lists.html


# Exercise 6
# ===========
# Write a function scalar_mult(s, v) that takes a number, s, and a list, v
# and returns the scalar multiple of v by s.

import sys


def scalar_mult(s, v):
    """ Takes a number, s, and a list, v and returns
    the scalar multiple of v by s """
    result = []
    for e in v:
        result.append(s * e)
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
    test(scalar_mult(0, [1, 2, 3]) == [0, 0, 0])
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])


test_suite()