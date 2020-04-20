'''
Exercise 7.2. The built-in function eval takes a string and evaluates it using
the Python interpreter. For example:
>>> eval('1 + 2 * 3')   # 7
Write a function called eval_loop that iteratively prompts the user, takes
the resulting input and evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of
the last expression it evaluated.
'''


def eval_loop():
    import math

    result = None
    while True:
        s = input('>> ')
        if s == 'done':
            return result
        result = eval(s)
        print(result)


print(eval_loop())
