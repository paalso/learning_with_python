##Chapter 6. Fruitful functions
##http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html

##Exercise 3
##===========
## Write the inverse function day_num which is given a day name, 
## and returns its number:


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


def day_num(day_name):
    """  Converts a day name to its number 0 to 6: “Sunday” -> 0 etc."""
    days = ["Sunday", "Monday", "Tuesday", "Wednesday",\
    "Thursday", "Friday", "Saturday"]
    if isinstance(day_name, str) and day_name in days:
        return days.index(day_name)
    return None


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_name("sukabljat") == None)
    test(day_name(3.142) == None)


test_suite()
