# Chapter 13. Files
# http://openbookproject.net/thinkcs/python/english3e/files.html


# Exercise 3
# ===========
# Write a program that reads a text file and produces an output file
# which is a copy of the file, except the first five columns of each line
# contain a four digit line number, followed by a space. Start numbering
# the first line in the output file at 1. Ensure that every line
# number is formatted to the same width in the output file. Use one of your
# Python programs as test data for this exercise: your output should be
# a printed and numbered listing of the Python program.

import sys

filename_in = "alice.txt"
filename_out = filename_in[:filename_in.find(".txt")] + "_numerated.txt"

file_in = open(filename_in, "r")
file_out = open(filename_out, "w")

numstr = 1
while True:
    s = file_in.readline()
    if len(s) == 0:
        break
    file_out.write("{0:4d} {1}".format(numstr, s))
    numstr += 1

file_in.close()
file_out.close()
