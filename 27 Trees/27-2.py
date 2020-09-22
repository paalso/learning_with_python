# Chapter 27. Trees
# http://openbookproject.net/thinkcs/python/english3e/trees.html

# Exercise 2
# ===========
# Write a function that takes an expression string and returns a token list.

def number(x):
    def try_number(x):
        try:
            f = float(x)
            return f
        except:
            return x

    result = try_number(x)
    if type(result) == float:
        if result == int(result):
            return int(result)
        return result

    return x


def parse_expr(expression):
    import re

    cleared = filter(lambda e: not (e == "" or e.isspace()),
                        re.split("([^0-9.])", expression))
    return list(map(lambda e: number(e), cleared))


expr = "(2 +  4.0001 * ( 1 - 2   / 5.0) + 7.125  % (4 - 2.00))"
print(parse_expr(expr))
