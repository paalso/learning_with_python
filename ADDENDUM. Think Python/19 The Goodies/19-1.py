"""
Exercise 19.1. The following is a function computes the binomial coefficient
recursively.
Rewrite the body of the function using nested conditional expressions. """

import time


def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".
    n: number of trials
    k: number of successes
    returns: int
    """
    return 1 if k == 0 else 0 if n == 0 else \
            binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1)


"""
One note: this function is not very efficient because it ends up computing
the same values over and over. You could make it more efficient by memoizing
(see Section 11.6). But you will find that it’s harder to memoize if you write
it using conditional expressions. """


def binomial_coeff_generator1():
    memo = {}
    def inner(n, k):
        if (n, k) not in memo:
            result = 1 if k == 0 else 0 if n == 0 \
                    else inner(n - 1, k) + inner(n - 1, k - 1)
            memo[(n, k)] = result
        return memo[(n, k)]
    return inner


binomial_coeff1 = binomial_coeff_generator1()
assert binomial_coeff1(1, 1) == 1
assert binomial_coeff1(2, 1) == 2
assert binomial_coeff1(4, 1) == 4
assert binomial_coeff1(4, 2) == 6
assert binomial_coeff1(9, 6) == 84
assert binomial_coeff1(10, 0) == 1
assert binomial_coeff1(10, 3) == 120

# --- Computing time comparing ---

args = (28, 13)

t0 = time.time()
result = binomial_coeff(*args)
print("result: {}, time: {}".format(result, time.time() - t0))
# result: 37442160, time: 51.20153188705444

t0 = time.time()
result = binomial_coeff1(*args)
print("result: {}, time: {}".format(result, time.time() - t0))
# result: 37442160, time: 0.0
