'''
Exercise 10.7. Write a function called has_duplicates that takes a list and
returns True if there is any element that appears more than once. It should
not modify the original list.
'''

def has_duplicates(L):
    """Returns True if any element appears more than once in a sequence.
    t: list
    returns: bool
    """
    unique = []
    for e in L:
        if e in unique:
            return True
        unique.append(e)
    return False


def has_duplicates_native(L):
    """Returns True if any element appears more than once in a sequence.
    t: list
    returns: bool
    """
    return len(L) != len(set(L))


def has_duplicates_authors(L):
    """Returns True if any element appears more than once in a sequence.
    t: list
    returns: bool
    http://greenteapress.com/thinkpython2/code/birthday.py
    """
    # make a copy of t to avoid modifying the parameter
    s = L[:]
    s.sort()

    # check for adjacent elements that are equal
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def random_list(size, bottom, upper):
    import random
    return [random.randrange(bottom, upper) for i in range(size)]


def count_time(func, data_collection, times = 1000000):
    import time
    start_time = time.time()
    for i in range(times):
        for data in data_collection:
            func(data)
    return time.time() - start_time


data_col = []
for i in range(10):
    data_col.append(random_list(23, 1, 366))

##for data in data_col:
##    results = (has_duplicates(data),
##                has_duplicates_native(data),
##                has_duplicates_authors(data))
##    print(results)


t1 = count_time(has_duplicates, data_col, 10000)
t2 = count_time(has_duplicates_native, data_col, 10000)
t3 = count_time(has_duplicates_authors, data_col, 10000)

print(f'My function time: {t1}')
print(f'Native function time: {t2}')
print(f'Author\'s function time: {t3}')
# Кстати разные степени эффективности функций при разных наборах данных получаются
