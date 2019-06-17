##Chapter 6. Fruitful functions
##http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html


## Exercise 9
## ===========
##Write three functions that are the “inverses” of to_secs:

##hours_in returns the whole integer number of hours represented
##by a total number of seconds.
##minutes_in returns the whole integer number of left over minutes
##in a total number of seconds, once the hours have been taken out.
##seconds_in returns the left over seconds represented
##by a total number of seconds.
##You may assume that the total number of seconds passed
##to these functions is an integer...

import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def hours_in(time_in_seconds):
    """ returns the whole integer number of hours represented
    by a total number of seconds."""
    return time_in_seconds // 3600


def minutes_in(time_in_seconds):
    """ returns the whole integer number of left over minutes
    in a total number of seconds, once the hours have been taken out."""
    return (time_in_seconds - hours_in(time_in_seconds) * 3600) // 60


def seconds_in(time_in_seconds):
    """ returns the left over seconds represented
    by a total number of seconds."""
    return time_in_seconds % 60


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    test(hours_in(43499) == 12)
    test(minutes_in(43499) == 4)
    test(seconds_in(43499) == 59)

test_suite()
