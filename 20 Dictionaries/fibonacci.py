def fib_old(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# -----------------------------------------------------
evaluated = {0: 0, 1: 1}

def fib(n):
    if n not in evaluated:
        evaluated[n] = fib(n - 1) + fib(n - 2)

    return evaluated[n]


# -----------------------------------------------------
already_known = [0,1]

def f(n):
    if n >= len(already_known):
        already_known.append(f(n - 1) + f(n - 2))
    return already_known[n]


# -----------------------------------------------------
n = 500
print(f(n))