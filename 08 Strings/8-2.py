## Chapter 8. Strings
## http://openbookproject.net/thinkcs/python/english3e/strings.html


## Exercise 2
## ===========

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)