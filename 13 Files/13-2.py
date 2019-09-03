# Chapter 13. Files
# http://openbookproject.net/thinkcs/python/english3e/files.html

# Exercise 2
# ===========
# Write a program that reads a file and prints only those lines that
# contain the substring snake

import sys

file_in = open("alice.txt", "r")
file_out = open("alice_filtered.txt", "w")

substring = "Alice"

while True:
    s = file_in.readline()
    if len(s) == 0:
        break
    if substring in s:
        file_out.write(s)

file_in.close()
file_out.close()
