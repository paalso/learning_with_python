# Chapter 11. Lists
# http://openbookproject.net/thinkcs/python/english3e/lists.html


# Exercise 8
# ===========
# Extra challenge for the mathematically inclined: Write a function
# cross_product(u, v) that takes two lists of numbers of length 3 and
# returns their cross product. You should write your own tests.

import sys


def cross_product(u, v):
    """ Takes two lists of numbers of length 3 and
        returns their cross product """
    u_x, u_y, u_z = u
    v_x, v_y, v_z = v
    return [u_y * v_z - u_z * v_y, u_z * v_x - u_x * v_z, u_x * v_y - v_x * u_y]


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    test(cross_product([1, 2, 3], [2, 1, -2]) ==  [-7, 8, -3])
    test(cross_product([-1, 2, -2], [2, 1, -1]) ==  [0, -5, -5])


test_suite()