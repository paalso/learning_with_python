# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 6
# ===========
# Write a function count that returns the number of occurrences of target
# in a nested list

from testtools import test


def count(target, nxs):
    """
    Returns the number of occurrences of target in a nested list
    """
    counter = 0
    for e in nxs:
        if type(e) == list:
            counter += count(target, e)
        else:
            if e == target:
                counter += 1
    return counter


def main():
    test(count(2, []) == 0)
    test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
    test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
    test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
    test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
    test(count("a",
     [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)


if __name__ == '__main__':
    main()