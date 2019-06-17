##5. Conditionals
##http://openbookproject.net/thinkcs/python/english3e/conditionals.html

# 5. Complete this truth table:
##    p q r ->  (not (p and q)) or r


def logical_function(p, q, r):
    return (not (p and q)) or r


## -------------------------------------------------------------------------

lst = [False, True]
print("  p     q     r  (not (p and q)) or r")
print("-------------------------------------")

for p in lst:
    for q in lst:
        for r in lst:
            print(p, q, r, "  -> ", logical_function(p, q, r))