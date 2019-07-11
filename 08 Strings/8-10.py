## Chapter 8. Strings
## http://openbookproject.net/thinkcs/python/english3e/strings.html

## Exercise 10
## ===========
# Write a function that removes all occurrences of a given letter from a string:

import sys


def reverse(s):
    tmp_list = list(s)
    tmp_list.reverse()
    return ''.join(tmp_list)


def is_palindrome(s):
    """ Recognizes palindromes """
    return s == reverse(s)


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
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))    # Is an empty string a palindrome?


test_suite()