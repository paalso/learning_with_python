Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@paalso 
0
0 0 paalso/learning_with_python
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Security  Insights  Settings
learning_with_python/07 Iterations/7-6.py
@paalso paalso Chapter 7. Exercises 5, 6
d4335fd yesterday
Executable File  44 lines (32 sloc)  1.27 KB
    
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
