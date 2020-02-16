# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 5
# ===========
# Write a function, recursive_min, that returns the smallest value in
# a nested number list.

from testtools import test


def recursive_min(nxc):
    """
       Returns the smallest value in a nested number list
    """
    first_number = True
    minimum = None
    for e in nxc:
        if type(e) != type([]):
            if first_number or e < minimum:
                minimum = e
                first_number = False
        else:
            min_e = recursive_min(e)
            if first_number:
                minimum = min_e
                first_number = False
            else:
                if min_e and min_e < minimum:
                    minimum = min_e
    return minimum


def main():
    test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
    test(recursive_min([2, 9, [-1, 13], 8, [], 6]) == -1)
    test(recursive_min([]) == None)
    test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(recursive_min([[[-13, 7], 90], 2, [1, 100, [[]]], 8, 6]) == -13)


if __name__ == '__main__':
    main()