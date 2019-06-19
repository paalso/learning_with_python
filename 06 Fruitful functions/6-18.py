## Chapter 6. Fruitful functions
## http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html


## Exercise 18
## ===========
## Write the function f2c(t) designed to return the integer value
## of the nearest degree Celsius for given temperature in Fahrenheit.


import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def f2c(t):
    return round((5 / 9) * (t - 32))


def test_suite():
    """ Run the suite of tests for code in this module (this file)."""
    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)


test_suite()
