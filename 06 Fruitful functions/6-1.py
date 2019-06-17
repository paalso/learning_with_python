##Chapter 6. Fruitful functions
##http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html

##Exercise 1.
##===========
##The four compass points can be abbreviated by single-letter strings as “N”,
##“E”, “S”, and “W”. Write a function turn_clockwise that takes one of these
##four compass points as its parameter, and returns the next compass point in
##the clockwise direction. Here are some tests that should pass:
##
##test(turn_clockwise("N") == "E")
##test(turn_clockwise("W") == "N")
##You might ask “What if the argument to the function is some other value?”
##For all other cases, the function should return the value None:
##
##test(turn_clockwise(42) == None)
##test(turn_clockwise("rubbish") == None)

import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def turn_clockwise(compass_point):
    compass_points = ["N", "E", "S", "W"]
    if compass_point in compass_points:
        index = compass_points.index(compass_point)
        return compass_points[(index + 1) % 4]

    return None


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise("S") == "W")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)


test_suite()
