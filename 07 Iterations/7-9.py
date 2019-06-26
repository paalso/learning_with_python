## Chapter 7. Iteration
## http://openbookproject.net/thinkcs/python/english3e/iteration.html


## Exercise 9
## ===========
## Write a function print_triangular_numbers(n) that prints out the first
## n triangular numbers. A call to print_triangular_numbers(5) would produce
## the following output:
##
## 1       1
## 2       3
## 3       6
## 4       10
## 5       15


import sys

def print_triangular_numbers(n):
    triangular = 1
    delta = 1
    for k in range(1, n + 1):
        print(k,"\t",triangular)
        delta += 1
        triangular += delta


n = 20
print_triangular_numbers(n)