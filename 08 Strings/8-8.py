## Chapter 8. Strings
## http://openbookproject.net/thinkcs/python/english3e/strings.html

## Exercise 8
## ===========
# Write a function that mirrors its argument:..

import sys


def reverse(s):
    tmp_list = list(s)
    tmp_list.reverse()
    return ''.join(tmp_list)
    ##    return ''.join(list(s).reverse())


def mirror(string):
    return string + reverse(string)


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
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")


test_suite()