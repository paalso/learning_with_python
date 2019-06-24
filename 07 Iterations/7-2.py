## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html


## Exercise 2
## ===========
## Sum up all the even numbers in a list.


import sys


def sum_even(lst):
    sum = 0
    for n in lst:
        if n % 2 == 0:
            sum += n
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
    test(sum_even([]) == 0)
    test(sum_even([1, 2, 4, 5, 10]) == 16)
    test(sum_even([0, 2, 4, 6]) == 12)
    test(sum_even([1, 1, 1, 1, 1]) == 0)


test_suite()
