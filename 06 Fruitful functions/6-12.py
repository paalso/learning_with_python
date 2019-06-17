##Chapter 6. Fruitful functions
##http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html


## Exercise 12
## ===========
##Write a function called hypotenuse that returns the length
##of the hypotenuse of a right triangle given the lengths of
##the two legs as parameters:

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


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)

test_suite()
