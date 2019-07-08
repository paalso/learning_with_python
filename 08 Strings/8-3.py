## Chapter 8. Strings
## http://openbookproject.net/thinkcs/python/english3e/strings.html


## Exercise 3
## ===========

# Encapsulate
# .... in a function named count_letters, and generalize it so that it accepts
# the string and the letter as arguments. Make the function return the number
# of characters, rather than print the answer. The caller should do the printing.

def count_letters(str, char):
    count = 0
    for c in str:
        if c == "a":
            count += 1
    return count

print(count_letters("banana", 'a'))
