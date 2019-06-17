##5. Conditionals
##http://openbookproject.net/thinkcs/python/english3e/conditionals.html

# 11. Write a function is_rightangled which, given the length of three sides
##of a triangle, will determine whether the triangle is right-angled.
##Assume that the third argument to the function is always the longest side.
##It will return True if the triangle is right-angled, or False otherwise.

def find_hypot (a, b):
    return (a * a + b * b) ** 0.5


def is_rightangled(a, b, c):
    eps = 0.0000001
    return abs(c - find_hypot(a, b)) < eps



## -----------------------------------------------------

[a, b, c] = [3, 4, 4.5]
print(is_rightangled(a, b, c))