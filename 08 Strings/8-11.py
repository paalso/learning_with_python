## Chapter 8. Strings
## http://openbookproject.net/thinkcs/python/english3e/strings.html

## Exercise 11
## ===========
# Write a function that removes all occurrences of a given letter from a string:

import sys


def count(substring, string):
    """ Counts how many times a substring occurs in a string """
    counter = 0
    index = -1
    while True:
        index = string.find(substring, index + 1)
        if index < 0:
            return counter
        counter += 1


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
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)
    test(count("a", "aaaaa") == 5)


test_suite()