from testtools import test


def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    ix = iy = 0

    while True:
        if ix == len(xs):
            result.extend(ys[iy:])
            return result

        if iy == len(ys):
            result.extend(xs[ix:])
            return result

        if xs[ix] <= ys[iy]:
            result.append(xs[ix])
            ix += 1
        else:
            result.append(ys[iy])
            iy += 1


xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
zs = xs+ys
zs.sort()

test(merge(xs, []) == xs)
test(merge([], ys) == ys)
test(merge([], []) == [])
test(merge(xs, ys) == zs)
test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
               ["a", "big", "big", "bite", "cat", "dog"])