# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 9
# ===========
# Use help to find out what sys.getrecursionlimit() and sys.setrecursionlimit(n)
# do. Create several experiments similar to what was done in
# infinite_recursion.py to test your understanding of how these module
# functions work.

import sys


def infinite_recursion(n=0):
    print(n)
##    if n == 0:
##        return
    return infinite_recursion(n + 1)


def main():
    print(f'Current recursion limit: {sys.getrecursionlimit()}')
    sys.setrecursionlimit(50)
    print(f'Current recursion limit: {sys.getrecursionlimit()}')
    infinite_recursion()


if __name__ == '__main__':
    main()