##5. Conditionals
##http://openbookproject.net/thinkcs/python/english3e/conditionals.html

# 12. Extend the above program so that the sides can be given to the function in any order.

def find_hypot (a, b):
    return (a * a + b * b) ** 0.5


def is_rightangled(a, b, c):
    eps = 0.000001
    return abs(c - find_hypot(a, b)) < eps or \
        abs(a - find_hypot(b, c)) < eps or \
        abs(b - find_hypot(a, c)) < eps




## -----------------------------------------------------

[a, b, c] = [5, 5, 5]
print(is_rightangled(a, b, c))

[a, b, c] = [5.23927459, 1.2, 5.1]
print(is_rightangled(a, b, c))