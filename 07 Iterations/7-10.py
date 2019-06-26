## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html


## Exercise 10
## ===========
## Write a function, is_prime, which takes a single integer argument
##and returns True when the argument is a prime number and False otherwise.


import sys, math

def is_prime(n):
    if n == 2:
        return True

    if n < 2 or n & 1 == 0:
        return False

    for k in range(3, int(math.sqrt(n)) + 1, 2):
        if n % k == 0:
            return False

    return True

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
    primes_lst = [2, 3, 5, 7, 13, 23, 37, 41, 83, 19911121]
    not_primes_lst = [1, 4, 6, 9, 15, 21, 39, 45, 99, 1000]
    for n in primes_lst:
        test(is_prime(n))
    for n in not_primes_lst:
        test(not is_prime(n))


test_suite()