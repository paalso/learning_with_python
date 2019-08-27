# Chapter 12. Modules
# http://openbookproject.net/thinkcs/python/english3e/modules.html


# Exercise 7
# ===========
# ...Then apply what you have learned to fill in the body of the function below
# using the split and join methods of str objects:
#
#test(myreplace(",", ";", "this, that, and some other thing") ==
#                        "this; that; and some other thing")
#test(myreplace(" ", "**",
#                 "Words will now      be  separated by stars.") ==
#                 "Words**will**now**be**separated**by**stars.")

from testtools import test


def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    if old == " ":
        old = None
    return new.join(s.split(old))


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(myreplace(",", ";", "this, that, and some other thing") ==
                             "this; that; and some other thing")
    test(myreplace(" ", "**",
                     "Words will now      be  separated by stars.") ==
                     "Words**will**now**be**separated**by**stars.")

test_suite()
