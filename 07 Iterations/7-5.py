## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html


## Exercise 5
## ===========
## Sum all the elements in a list up to but not including the first even number.
## (Write your unit tests. What if there is no even number?)


import sys


def list_sum_up_to_first_even(lst):
    sum = 0
    for n in lst:
        if n % 2 == 0:
            break
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
    test(list_sum_up_to_first_even([]) == 0)
    test(list_sum_up_to_first_even([1, 2, 4, 5, 10]) == 1)
    test(list_sum_up_to_first_even([0, 2, 4, 6]) == 0)
    test(list_sum_up_to_first_even([2, 1, 3, 5]) == 0)
    test(list_sum_up_to_first_even([1, 1, 1, 1, 1]) == 5)
    test(list_sum_up_to_first_even([1, 3, 7, 9, 11, 2, 11, 13]) == 31)
    test(list_sum_up_to_first_even([2]) == 0)


test_suite()
