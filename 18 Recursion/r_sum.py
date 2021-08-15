# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html


def r_sum(nested_num_list):
    total = 0
    for e in nested_num_list:
        total += r_sum(e) if type(e) == list else e
    return total


assert r_sum([]) == 0
assert r_sum([1, 2, 3]) == 6
assert r_sum([1, 2, [1, 2, 3]]) == 9
assert r_sum([[1, 2], [1, 2, 3]]) == 9
assert r_sum([-9, [1, 2], [1, 2, 3]]) == 0
assert r_sum([-9, [1, 2], [1, 2, 3, [1, 2]]]) == 3
