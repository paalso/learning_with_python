## Chapter 8. Strings
## http://openbookproject.net/thinkcs/python/english3e/strings.html


## Exercise 4
## ===========

# Now rewrite the count_letters function so that instead of traversing
# the string, it repeatedly calls the find method, with the optional third
# parameter to locate new occurrences of the letter being counted.

def count_letters(str, char):
    count = 0
    next_find = -1
    while True:
        next_find = str.find(char, next_find + 1)
        if next_find < 0:
            break
        count += 1
    return count

print(count_letters("banana", 'na'))
