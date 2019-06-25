## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html


## Exercise 6
## ===========
## Count how many words occur in a list up to and including
##the first occurrence of the word “sam”.


import sys


def count_words_up_to_given(lst, check_word):
    counter = 0
    for word in lst:
        counter += 1
        if word == check_word:
            break
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
    test(count_words_up_to_given([], "sam") == 0)
    test(count_words_up_to_given(["bob", "table", "sam", "paper"], "sam") == 3)
    test(count_words_up_to_given(["book", "burrow", "swan", "sam"], "sam") == 4)
    test(count_words_up_to_given(["exit", "program", "excel"], "sam") == 3)
    test(count_words_up_to_given(["sam", "program", "excel"], "sam") == 1)
    test(count_words_up_to_given(["exit", "sam", "excel"], "sam") == 2)

test_suite()
