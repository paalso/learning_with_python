known = {0: 0, 1: 1}


def memo_fib(n):
    if n in known:
        return known[n]

    result = memo_fib(n - 2) + memo_fib(n - 1)
    known[n] = result
    return result


def fib(n):
    if n < 2: return n
    return fib(n - 2) + fib(n - 1)


def main():
    import time

    n = 35

    start_time = time.time()
    print(f'Plain fibonacci:\nfib({n}) = {fib(n)}')
    duration = time.time() - start_time
    print(f'Time: {duration}')

    start_time = time.time()
    print(f'\nMemorized fibonacci:\nfib({n}) = {memo_fib(n)}')
    duration = time.time() - start_time
    print(f'Time: {duration}')


if __name__ == '__main__':
    main()
