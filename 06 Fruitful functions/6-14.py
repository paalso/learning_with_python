## Chapter 6. Fruitful functions
## http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html


## Exercise 14
## ===========
## Write a function called is_even(n) that takes an integer as an argument
## and returns True if the argument is an even number and False if it is odd.

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


def is_even(n):
    return n % 2 == 0


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(is_even(0) == True)
    test(is_even(4) == True)
    test(is_even(1) == False)
    test(is_even(999) == False)

test_suite()
