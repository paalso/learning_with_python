# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 7
# ===========
# Write a function flatten that returns a simple list containing all the values
# in a nested list

from testtools import test


def flatten(nxs):
    """
    Returns a simple list containing all the values in a nested list
    """
    flattened = []
    for e in nxs:
        if type(e) == list:
            flattened.extend(flatten(e))
        else:
            flattened.append(e)
    return flattened


def main():
    test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
    test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
    test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
    test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
                  ["this","a","thing","a","is","a","easy"])
    test(flatten([]) == [])


if __name__ == '__main__':
    main()
