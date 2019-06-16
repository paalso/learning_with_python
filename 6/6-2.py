##Chapter 6. Fruitful functions
##http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html

##Exercise 2
##===========
## Write a function day_name that converts an integer number 0 to 6 
## into the name of a day. Assume day 0 is “Sunday”. Once again, return 
## None if the arguments to the function are not valid. 


import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def day_name(day_number):
    """  Converts an integer number 0 to 6 into the name of a day: 0 -> “Sunday” etc."""
    days = ["Sunday", "Monday", "Tuesday", "Wednesday",\
    "Thursday", "Friday", "Saturday"]
    if isinstance(day_number, int) and 0 <= day_number <= 6:
        return days[day_number]
    return None


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(day_name(0) == "Sunday")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_name("abc") == None)
    test(day_name(3.142) == None)


test_suite()
