# Chapter 14. List Algorithms
# http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html

# Exercise 1
# ===========
# The section in this chapter called Alice in Wonderland, again! started with
# the observation that the merge algorithm uses a pattern that can be reused in
# other situations. Adapt the merge algorithm to write each of these functions,
# as was suggested there:

# Return only those items that are present in both lists.

from testtools import test


def intersect(xs, ys):
    """ Return only those items that are present in both lists """
    result = []
    ix = iy = 0
    while True:
        if ix == len(xs) or iy == len(ys):
            return result

        if xs[ix] < ys[iy]:
            ix += 1
        elif ys[iy] < xs[ix]:
            iy += 1
        else:
            result.append(xs[ix])
            ix += 1
            iy += 1


xs = [1,3,3,3,5,7,9,11,12,12,13,15,17,19,20]
ys = [3,3,4,8,12,12,16,20,24]

test(intersect(xs, []) == [])
test(intersect([], ys) == [])
test(intersect([], []) == [])
test(intersect(xs, xs) == xs)
test(intersect(xs, ys) == [3, 3, 12, 12, 20])
test(intersect(ys, [12,12,16,20,24,25,25,25,100]) == [12,12,16,20,24])
test(intersect([1,2,3], [3,4,5]) == [3])
test(intersect([1,2,3], [4,5,6]) == [])
test(intersect(["a", "big", "cat"], ["big", "bite", "dog"]) == ["big"])