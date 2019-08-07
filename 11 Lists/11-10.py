# Chapter 11. Lists
# http://openbookproject.net/thinkcs/python/english3e/lists.html


# Exercise 10
# ===========
# Write a function replace(s, old, new) that replaces all occurrences
# of old with new in a string s

import sys


def replace(s, old, new):
    """ Replaces all occurrences of old with new in a string s """
    return new.join(s.split(old))


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") ==
        "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a") ==
        "I lave spam! Spam is my favarite faad. Spam, spam, yum!")


test_suite()
