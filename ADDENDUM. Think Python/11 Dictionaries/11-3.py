'''
Exercise 11.3. Memoize the Ackermann function from Exercise 6.2 and see if
memoization makes it possible to evaluate the function with bigger arguments.

A(m, n) =
    n + 1 if m = 0
    A(m − 1, 1) if m > 0 and n = 0
    A(m − 1, A(m, n − 1)) if m > 0 and n > 0.

Hint: no. Solution: http://thinkpython2.com/code/ackermann_memo.py
'''


# -----------------------------------------------------
def A_plain(m, n):
    if m == 0:
        return n + 1

    if n == 0 and m > 0:
        return A(m - 1, 1)

    return A(m - 1, A(m, n - 1))


# -----------------------------------------------------
A_memo = {(0, 0): 1}

def A(m, n):

##    print(m, n)

    if (m, n) in A_memo:
        return A_memo[(m, n)]

    if m == 0:
        A_memo[(m, n)] = n + 1
        return n + 1

    if n == 0 and m > 0:
        A_memo[(m, n)] = A(m - 1, 1)
        return A(m - 1, 1)

    result = A(m - 1, A(m, n - 1))
    A_memo[(m, n)] = result
    return result

# -----------------------------------------------------
cache = {}

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    See http://greenteapress.com/thinkpython2/code/ackermann_memo.py
    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]


def main():
    import time

    acc_func_values = {
        (0, 0) : 1,
        (0, 1) : 2,
        (0, 2) : 3,
        (0, 3) : 5,
        (0, 4) : 13,
##        (0, 5) : 65533,
        (1, 0) : 2,
        (2, 0) : 3,
        (1, 3) : 13,
        (3, 3) : 61,
        (5, 3) : 253,
        (6, 3) : 509,
    }

##    m = 3
##    n = 6
##    print(f'A({m}, {n}) = {A(m, n)}')
##    print(f'A({m}, {n}) = {ackermann(m, n)}')

    start_time = time.time()
    print('\nPlain Ackermann\'s function calculation')

    for item in acc_func_values.keys():
        n, m = item
##        value = ackermann(m, n)
##        value = A(m, n)
        value = A_plain(m, n)
        print(f'A({m}, {n}) = {value}, {value == acc_func_values[item]}')

    duration = time.time() - start_time
    print(f'Time: {duration}')

    start_time = time.time()

    print('\nAckermann\'s function calculation with memorization')

    for item in acc_func_values.keys():
        n, m = item
##        value = ackermann(m, n)
        value = A(m, n)
##        value = A_plain(m, n)
        print(f'A({m}, {n}) = {value}, {value == acc_func_values[item]}')

    duration = time.time() - start_time
    print(f'Time: {duration}')



if __name__ == '__main__':
    main()
