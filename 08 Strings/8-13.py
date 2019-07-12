## Chapter 8. Strings
## http://openbookproject.net/thinkcs/python/english3e/strings.html

## Exercise 13
## ===========
# Write a function that removes all occurrences of a given letter from a string:

import sys


def remove_all(substring, string):
    """ Removes all occurrences of a string from another string """
    result_str = ""
    index = 0
    sub_len = len(substring)
    while True:
        next_index = string.find(substring, index)
        if next_index == -1:
            return result_str + string[index:]
        result_str += string[index:next_index]
        index = next_index + sub_len


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
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")
    test(remove_all("eggs", "eggs") == "")
    test(remove_all("x", "xxxxx") == "")
    test(remove_all("x", "xxxax") == "a")
    test(remove_all("ke", "kekeke") == "")


test_suite()