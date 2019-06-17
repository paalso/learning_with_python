##Chapter 6. Fruitful functions
##http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html

##Exercise 4, 5
##===========
## Write a function that helps answer questions like ‘“Today is Wednesday. 
## I leave on holiday in 19 days time. What day will that be?”’ So
##  the function  must take a day name and a delta argument — the number
##  of days to add — and   should return the resulting day name

## Can your day_add function already work with negative deltas? For example,
##  -1 would be yesterday, or -7 would be a week ago:..


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
    """  Converts a day name to its number 0 to 6: “Sunday” -> 0 etc."""
    days = ["Sunday", "Monday", "Tuesday", "Wednesday",\
    "Thursday", "Friday", "Saturday"]
    if isinstance(day_number, int) and 0 <= day_number <= 6:
        return days[day_number]
    return None


def day_num(day_name):
    """  Converts an integer number 0 to 6 into the name of a day: 0 -> “Sunday” etc."""
    days = ["Sunday", "Monday", "Tuesday", "Wednesday",\
    "Thursday", "Friday", "Saturday"]
    if isinstance(day_name, str) and day_name in days:
        return days.index(day_name)
    return None


def day_add(day, delta):
    return day_name((day_num(day) + delta) % 7)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")


test_suite()
