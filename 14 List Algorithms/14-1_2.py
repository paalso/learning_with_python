# Chapter 14. List Algorithms
# http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html

# Exercise 1
# ===========
# The section in this chapter called Alice in Wonderland, again! started with
# the observation that the merge algorithm uses a pattern that can be reused in
# other situations. Adapt the merge algorithm to write each of these functions,
# as was suggested there:

# Return only those items that are present in the first list, but not in the second.

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


xs = [1,3,3,3,5,7,9,11,12,12,13,15,17,19,20]
ys = [3,3,4,8,12,12,16,20,24]

test(substract(xs, []) == xs)
test(substract([], ys) == [])
test(substract([], []) == [])
test(substract(xs, xs) == [])
test(substract(xs, ys) == [1,5,7,9,11,13,15,17,19])
test(substract(ys, [12,16,20,24,25,25,25,100]) == [3,3,4,8])
test(substract([1,2,3], [3,4,5]) == [1,2])
test(substract([1,2,3], [4,5,6]) == [1,2,3])
test(substract([5,7,11,11,11,12,13], [7,8,11]) == [5,12,13])
test(substract(["a", "big", "cat"], ["big", "bite", "dog"]) == ["a", "cat"])
