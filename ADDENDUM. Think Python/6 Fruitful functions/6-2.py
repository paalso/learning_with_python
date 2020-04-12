'''
Exercise 6.2. The Ackermann function, A(m, n), is defined:

A(m, n) =
n + 1 if m = 0
A(m − 1, 1) if m > 0 and n = 0
A(m − 1, A(m, n − 1)) if m > 0 and n > 0.

Write a function named ack that evaluates the Ackermann function. Use your
function to evaluate ack(3, 4), which should be 125. What happens for larger
values of m and n?
'''


def A(m, n):
    if m == 0:
        return n + 1

    if n == 0 and m > 0:
        return A(m - 1, 1)

    return A(m - 1, A(m, n - 1))


acc_func_values = {
    (0, 0) : 1,
    (1, 0) : 2,
    (2, 0) : 3,
    (0, 1) : 2,
    (0, 2) : 3,
    (0, 3) : 5,
    (0, 4) : 13,
    (1, 3) : 13,
    (3, 3) : 61,
    (5, 3) : 253
}


for item in acc_func_values.keys():
    n, m = item
    value = A(m, n)
    print(f'A({m}, {n}) = {value}, {value == acc_func_values[item]}')
