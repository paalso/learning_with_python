## Chapter 9. Tuples
## http://openbookproject.net/thinkcs/python/english3e/tuples.html

## Exercise 1
## ===========
# We’ve said nothing in this chapter about whether you can pass tuples as
# arguments to a function. Construct a small Python example to test whether this
# is possible, and write up your findings.

import sys

()

def get_birth_info_string(person):
    """ Generates string like '<NAME> was born in <YEAR>' """
    name = person[0][0] + " " + person[0][1]
    born_year = person[1][2]
    return "{0} was born in {1}".format(name, born_year)


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
    test(distance_to_center((3, 4)) == 5)
    test(distance_to_center((3, 4, 0)) == 5)
    test(distance_to_center((1, 1, 1)) == 1.7320508075688772)
    test(distance_to_center((0, 0, 1, 0)) == 1)


##test_suite()
julia = ( ("Julia", "Roberts"), (8, "October", 1967),
                     "Actress", ("Atlanta", "Georgia"),
                     [ ("Duplicity", 2009),
                       ("Notting Hill", 1999),
                       ("Pretty Woman", 1990),
                       ("Erin Brockovich", 2000),
                       ("Eat Pray Love", 2010),
                       ("Mona Lisa Smile", 2003),
                       ("Oceans Twelve", 2004) ])

print(get_birth_info_string(julia))