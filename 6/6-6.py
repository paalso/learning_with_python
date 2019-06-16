##Chapter 6. Fruitful functions
##http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html

##Exercise 6
##===========
## Write a function days_in_month which takes the name of a month, 
## and returns the number of days in the month. Ignore leap years:

import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def days_in_month(month_name):

    months_list = ["January", "February", "March", "April",\
    "May", "June", "July", "August", \
    "September", "October", "November", "December"]
    
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isinstance(month_name, str) and month_name in months_list:
        return days_in_month_list[months_list.index(month_name)]
    return None


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("June") == 30)
    test(days_in_month("Fghtkm") == None)
    test(days_in_month(8.556) == None)



test_suite()
