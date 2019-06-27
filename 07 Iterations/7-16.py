## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html

## Exercise 16
## ===========
## Write a function sum_of_squares(xs) that computes the sum
## of the squares of the numbers in the list xs.
## For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:


import sys, math


def sum_of_squares(xs):
    sum = 0
    for n in xs:
        sum += n * n
    return sum


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
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)
    test(sum_of_squares([1, 1, 1, 1, 1]) == 5)


test_suite()