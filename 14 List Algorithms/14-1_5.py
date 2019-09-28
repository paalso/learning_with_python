# Chapter 14. List Algorithms
# http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html

# Exercise 1
# ===========
# The section in this chapter called Alice in Wonderland, again! started with
# the observation that the merge algorithm uses a pattern that can be reused in
# other situations. Adapt the merge algorithm to write each of these functions,
# as was suggested there:

# Return items from the first list that are not eliminated by a matching
# element in the second list. In this case, an item in the second list
# “knocks out” just one matching item in the first list. This operation is
# sometimes called bagdiff. For example bagdiff([5,7,11,11,11,12,13], [7,8,11])
#  would return [5,11,11,12,13]

from testtools import test


def bagdiff(xs, ys):
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
            iy += 1   # differs from substract() by this syting only


xs = [1,3,3,3,5,7,9,11,12,12,13,15,17,19,20]
ys = [3,3,4,8,12,12,16,20,24]

test(bagdiff(xs, []) == xs)
test(bagdiff([], ys) == [])
test(bagdiff([], []) == [])
test(bagdiff(xs, xs) == [])
test(bagdiff(xs, ys) == [1,3,5,7,9,11,13,15,17,19])
test(bagdiff(ys, [12,12,16,20,24,25,25,25,100]) == [3,3,4,8])
test(bagdiff([1,2,3], [3,4,5]) == [1,2])
test(bagdiff([1,2,3], [4,5,6]) == [1,2,3])
test(bagdiff([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])
test(bagdiff(["a", "big", "cat"], ["big", "bite", "dog"]) == ["a", "cat"])
