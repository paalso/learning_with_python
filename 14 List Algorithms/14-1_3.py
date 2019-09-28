# Chapter 14. List Algorithms
# http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html

# Exercise 1
# ===========
# The section in this chapter called Alice in Wonderland, again! started with
# the observation that the merge algorithm uses a pattern that can be reused in
# other situations. Adapt the merge algorithm to write each of these functions,
# as was suggested there:

# Return only those items that are present in the second list, but not in the first.

from testtools import test


def substract(xs, ys):
    """ Return only those items that are present in the first list,
    but not in the second """
    result = []
    ix = iy = 0
    while True:
        if ix == len(xs):
            return result
        if iy == len(ys):
            result.extend(xs[ix:])
            return result

        if xs[ix] < ys[iy]:
            result.append(xs[ix])
            ix += 1
        elif ys[iy] < xs[ix]:
            iy += 1
        else:
            ix += 1
#            iy += 1       # differs from bigdiff() by this syting only


def remove(xs, ys):
    """ Return only those items that are present in the second list,
    but not in the first. """
    return substract(ys, xs)


xs = [1,3,3,3,5,7,9,11,12,12,13,15,17,19,20]
ys = [3,3,4,8,12,12,16,20,24]

test(remove(xs, []) == [])
test(remove([], ys) == ys)
test(remove([], []) == [])
test(remove(xs, xs) == [])
test(remove(xs, ys) == [4,8,16,24])
test(remove([1,2], [1,1,3]) == [3])
test(remove(ys, [12,12,16,20,24,25,25,25,100]) == [25,25,25,100])
test(remove([1,2,3], [3,4,5]) == [4,5])
test(remove([1,2,3], [4,5,6]) == [4,5,6])
test(remove(["a", "big", "cat"], ["big", "bite", "dog"]) == ["bite", "dog"])