## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html

## Exercise 8
## ===========
## Trace the execution of the last version of print_mult_table
##and figure out how it works.


import sys, math

def print_multiples(n, high):
    for k in range(1, high + 1):
        print(n * k, "\t", end = "")
    print()

def print_mult_table(high):

    for k in range(1, high + 1):
##        print(k,":\t\t", end = "")
        print_multiples(k, k)



print_mult_table(10)