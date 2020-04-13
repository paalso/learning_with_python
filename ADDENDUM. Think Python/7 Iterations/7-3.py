'''
Exercise 7.3. The mathematician Srinivasa Ramanujan found an infinite series
that can be used to generate a numerical approximation of 1/π:
    https://en.wikipedia.org/wiki/Srinivasa_Ramanujan#Mathematical_achievements

Write a function called estimate_pi that uses this formula to compute and
return an estimate of π. It should use a while loop to compute terms of
the summation until the last term is smaller than 1e-15 (which is Python
notation for 10−15). You can check the result by comparing it to math.pi.
'''

import math


def estimate_pi():
    eps = 1e-15
    k = 0
    a = 1103
    s = a

    while a > eps:
        a = a * \
            (4 * k + 1) * (4 * k + 2) * (4 * k + 3) * (4 * k + 4) * \
            (1103 + 26390 * (k + 1)) / ((k + 1) ** 4 * 24591257856 * \
            (1103 + 26390 * k))
        s += a
        k += 1

    return 9801 / (2 * 2 ** 0.5 * s)


print(estimate_pi())
print(math.pi)
print(math.pi - estimate_pi())
