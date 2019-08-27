# Chapter 12. Modules
# http://openbookproject.net/thinkcs/python/english3e/modules.html

# Exercise 8
# ===========

from testtools import test
from wordtools import *


def test_suite():
    print("\n'cleanword' testing...")
    test(cleanword("what?") == "what")
    test(cleanword("'now!'") == "now")
    test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

    print("\n'has_dashdash' testing...")
    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))

    print("\n'extract_words' testing...")
    test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
          ['now','is','the','time','now','is','the','time','yes','now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") ==
          ['she','tried','to','curtsey','as','she','spoke','fancy'])

    print("\n'wordcount' testing...")
    test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
    test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
    test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
    test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

    print("\n'wordset' testing...")
    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
          ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
          ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
          ["a", "am", "are", "be", "but", "is", "or"])

    print("\n'longestword' testing...")
    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    test(longestword([ ]) == 0)


test_suite()
