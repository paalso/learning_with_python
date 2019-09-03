# Chapter 13. Files
# http://openbookproject.net/thinkcs/python/english3e/files.html


# Exercise 4
# ===========
# Write a program that undoes the numbering of the previous exercise: it should
# read a file with numbered lines and produce another file without line numbers.

import sys

filename_in = "alice_numerated.txt"
filename_out = filename_in[:filename_in.find("_numerated.txt")] + \
                                                "_denumerated.txt"

file_in = open(filename_in, "r")
file_out = open(filename_out, "w")

SYMBOLS_TO_DELETE = 5
while True:
    s = file_in.readline()
    if len(s) == 0:
        break
    file_out.write(s[SYMBOLS_TO_DELETE:])

file_in.close()
file_out.close()
