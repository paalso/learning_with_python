# Chapter 13. Files
# http://openbookproject.net/thinkcs/python/english3e/files.html

# Exercise 1
# ===========
# Write a program that reads a file and writes out a new file with the lines in
# reversed order (i.e. the first line in the old file becomes the last one
# in the new file.)

import sys

file_in = open("alice.txt", "r")
file_out = open("alice_stringinversed.txt", "w")

while True:
    s = file_in.readline()
    if len(s) == 0:
        break
    file_out.write(s[::-1])

file_in.close()
file_out.close()
