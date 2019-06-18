## Chapter 6. Fruitful functions
## http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html


## Exercise 15
## ===========
## Now write the function is_odd(n) that returns True when n is odd and
## False otherwise. Include unit tests for this function too.
## Finally, modify it so that it uses a call to is_even to determine
## if its argument is an odd integer, and ensure that its test still pass.


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


def is_odd(n):
    return not is_even(n)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(is_odd(0) == False)
    test(is_odd(4) == False)
    test(is_odd(1) == True)
    test(is_odd(999) == True)

test_suite()
