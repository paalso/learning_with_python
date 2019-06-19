## Chapter 6. Fruitful functions
## http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html


## Exercise 17
## ===========
## Write a function is_multiple(f, n) to satisfy these unit tests:..


import sys
import math


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def is_factor(n, m):
    return m % n == 0


def is_multiple(m, n):
    return is_factor(n, m)


def test_suite():
    """ Run the suite of tests for code in this module (this file)."""
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))


test_suite()
