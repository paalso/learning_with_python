## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html

## Exercise 15
## ===========
## Write a function num_even_digits(n) that counts the number of
## even digits in n.


import sys, math


def is_even_digit(digit):
    return digit & 1 == 0


def num_even_digits(n):
    if n == 0:
        return 1

    if n < 0:
        n = -n

    digits = 0
    while n > 0:
        if (n % 10) & 1 == 0:
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
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)


test_suite()