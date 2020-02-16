# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 8
# ===========
# Rewrite the fibonacci algorithm without using recursion. Can you find
# bigger terms of the sequence? Can you find fib(200)?


def fib(n):
    if n < 2:
        return n
    f_prev_prev = 0
    f_prev = 1
    for k in range(1, n):
        f = f_prev_prev + f_prev
        f_prev_prev, f_prev = f_prev, f

    return f


def main():
    print(fib(2))
    print(fib(3))
    print(fib(10))
    print(fib(200))


if __name__ == '__main__':
    main()