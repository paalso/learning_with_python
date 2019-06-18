##Chapter 6. Fruitful functions
##http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html


## Exercise 13
## ===========
## Write a function slope(x1, y1, x2, y2) that returns the slope of the line
## through the points (x1, y1) and (x2, y2). Be sure your implementation
## of slope can pass the following tests:..
## Then use a call to slope in a new function named
## intercept(x1, y1, x2, y2) that returns the y-intercept
## of the line through the points (x1, y1) and (x2, y2)

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


def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def intercept(x1, y1, x2, y2):
    return y1 - slope(x1, y1, x2, y2) * x1


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)

test_suite()
