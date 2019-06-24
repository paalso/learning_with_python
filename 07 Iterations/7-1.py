## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html


## Exercise 1
## ===========
## Write a function to count how many odd numbers are in a list.


import sys


def count_odds(lst):
    counter = 0
    for n in lst:
        if n % 2 == 1:
            counter += 1
    return counter


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
    test(count_odds([]) == 0)
    test(count_odds([1, 2, 4, 5]) == 2)
    test(count_odds([0, 2, 4, 6]) == 0)
    test(count_odds([1, 1, 1, 1, 1]) == 5)


test_suite()
