## Chapter 8. Strings
## http://openbookproject.net/thinkcs/python/english3e/strings.html

## Exercise 12
## ===========
# Write a function that removes all occurrences of a given letter from a string:

import sys


def remove(substring, string):
    """ Removes the first occurrence of a string from another string """
    index = string.find(substring)
    if index == -1:
        return string
    return string[:index] + string[index + len(substring):]


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
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")


test_suite()