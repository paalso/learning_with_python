# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 8
# ===========
# Rewrite the fibonacci algorithm without using recursion. Can you find
# bigger terms of the sequence? Can you find fib(200)?


def fib(n):
    if n < 2:
        return n
    f_prev_prev, f_prev = 0, 1

    for _ in range(1, n):
        f = f_prev_prev + f_prev
        f_prev_prev, f_prev = f_prev, f

    return f


def main():
    for n in 2, 3, 10, 35, 200:
        print("fib({}) = {}".format(n, fib(n)))


if __name__ == '__main__':
    main()