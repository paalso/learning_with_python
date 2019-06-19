## Chapter 6. Fruitful functions
## http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html


## Exercise 19
## ===========
## Now do the opposite: write the function c2f which converts
## Celsius to Fahrenheit


import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def c2f(t):
    return round((9 / 5) * t + 32)


def test_suite():
    """ Run the suite of tests for code in this module (this file)."""
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)


test_suite()
