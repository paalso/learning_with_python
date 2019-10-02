# Chapter 20. Dictionaries
# http://openbookproject.net/thinkcs/python/english3e/dictionaries.html

# Exercise 1
# ===========
# Write a program that reads a string and returns a table of the letters of
# the alphabet in alphabetical order which occur in the string together
# with the number of times each letter occurs. Case should be ignored.
# A sample output of the program when the user enters the data “ThiS is String
# with Upper and lower case Letters”, would look this this:
# a  2
# c  1
# d  1
# .....

def count_letters(text):
    result = {}
    for c in text:
        c = c.lower()
        if 'a' <= c <= 'z':
            result[c] = result.get(c,0) + 1
    return result


def dict_values_sum(dict):
    return sum(dict.values())


##s = input()

file_in = open("alice_in_wonderland.txt")
s = file_in.read()
file_in.close()

letters_freq_dict = count_letters(s)
letters_freq_sorted = sorted(list(letters_freq_dict.items()))
total_letters = dict_values_sum(letters_freq_dict)
for letter, freq in letters_freq_sorted:
    percent = round(freq / total_letters * 100, 1)
    print("{0:2}{1:6}{2:8}%".format(letter, freq, percent))
print("Total letters:\n  {0}".format(total_letters))
