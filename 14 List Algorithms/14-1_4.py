# Chapter 14. List Algorithms
# http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html

# Exercise 1
# ===========
# The section in this chapter called Alice in Wonderland, again! started with
# the observation that the merge algorithm uses a pattern that can be reused in
# other situations. Adapt the merge algorithm to write each of these functions,
# as was suggested there:

# Return items that are present in either the first or the second list.

from testtools import test


def remove_adjacent_dups(xs):
    result = []
    last_unique = None
    for el in xs:
        if el != last_unique:
            result.append(el)
            last_unique = el
    return result


def union(xs, ys):
    """ Return items that are present in either the first or the second list."""
    result = []
    ix = iy = 0
    last_unique = None
    while True:
        if iy == len(ys):
            for i in range(ix, len(xs)):
                if xs[i] != last_unique:
                    result.append(xs[i])
                    last_unique = xs[i]
            return result
        if ix == len(xs):
            for i in range(iy, len(ys)):
                if ys[i] != last_unique:
                    result.append(ys[i])
                    last_unique = ys[i]
            return result

        if xs[ix] < ys[iy]:
            if xs[ix] != last_unique:
                result.append(xs[ix])
                last_unique = xs[ix]
            ix += 1
        else:
            if ys[iy] != last_unique:
                result.append(ys[iy])
                last_unique = ys[iy]
            iy += 1


test(union(xs, []) == [1,3,5,7,9,11,12,13,15,17,19,20])
test(union([], ys) == [3,4,8,12,16,20,24])
test(union([], []) == [])
test(union(xs, xs) == [1,3,5,7,9,11,12,13,15,17,19,20])
test(union(xs, ys) == [1,3,4,5,7,8,9,11,12,13,15,16,17,19,20,24])
test(union([1,2], [1,1,3]) == [1,2,3])
test(union([1,2,3], [3,4,5]) == [1,2,3,4,5])
test(union([1,2,3], [4,5,6]) == [1,2,3,4,5,6])
test(union(["a", "big", "cat"], ["big", "bite", "dog"]) == ["a","big","bite","cat","dog"])