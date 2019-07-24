## Chapter 9. Tuples
## http://openbookproject.net/thinkcs/python/english3e/tuples.html

## Exercise 1
## ===========
# We’ve said nothing in this chapter about whether you can pass tuples as
# arguments to a function. Construct a small Python example to test whether this
# is possible, and write up your findings.

import sys

def distance_to_center(p):
    """ Get the distance to the origin a cartesian coordinate space """
    sum = 0
    for c in p:
        sum += c * c
    return sum ** 0.5


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(distance_to_center((3, 4)) == 5)
    test(distance_to_center((3, 4, 0)) == 5)
    test(distance_to_center((1, 1, 1)) == 1.7320508075688772)
    test(distance_to_center((0, 0, 1, 0)) == 1)


test_suite()