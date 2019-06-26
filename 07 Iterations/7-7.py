## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html


## Exercise 7
## ===========
## Add a print function to Newton’s sqrt function that prints out better
## each time it is calculated. Call your modified function with 25
## as an argument and record the results.


import sys

def sqrt(x):
    if x == 0:
        return 0.0

    eps = 0.000001
    estimate = 0.5 * x

    while True:
        next_estimate = 0.5 * (estimate + x / estimate)
        print(next_estimate)
        if abs(next_estimate - estimate) < eps:
            return next_estimate
        estimate = next_estimate


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    eps = 0.00001
    """ Run the suite of tests for code in this module (this file).
    """
    test(abs(sqrt(25) - 5.0) < eps)
    test(abs(sqrt(100) - 10.0) < eps)
    test(abs(sqrt(0) - 0.0) < eps)
    test(abs(sqrt(1) - 1.0) < eps)


##test_suite()

x = 3600
print(sqrt(x))
