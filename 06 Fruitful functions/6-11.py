##Chapter 6. Fruitful functions
##http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html


## Exercise 11
## ===========
##Write a compare function that returns
##1 if a > b, 0 if a == b, and -1 if a < b

import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def compare(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    return 0


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)


test_suite()
