## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html

## Exercise 14
## ===========
## What will num_digits(0) return? Modify it to return 1 for this case.
## Why does a call to num_digits(-24) result in an infinite loop?
## (hint: -1//10 evaluates to -1) Modify num_digits so that it works
## correctly with any integer value.


import sys, math

def num_digits(n):
    if n == 0:
        return 1

    if n < 0:
        n = -n

    digits = 0
    while n > 0:
        digits += 1
        n //= 10

    return digits


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
    test(num_digits(123456) == 6)
    test(num_digits(9) == 1)
    test(num_digits(28) == 2)
    test(num_digits(-1) == 1)
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)

test_suite()