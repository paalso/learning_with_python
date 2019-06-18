## Chapter 6. Fruitful functions
## http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html


## Exercise 16
## ===========
## Write a function is_factor(f, n) that passes these tests:..


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


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))


test_suite()
