## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html


## Exercise 4
## ===========
## Count how many words in a list have length 5.


import sys


def count_words(lst, length):
    counter = 0
    for word in lst:
        if len(word) == length:
            counter += 1
    return counter


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
    test(count_words([], 5) == 0)
    test(count_words(["bob", "table", "zebra", "paper"], 5) == 3)
    test(count_words(["book", "burrow", "swan"], 5) == 0)
    test(count_words(["exit", "program", "excel"], 5) == 1)


test_suite()
