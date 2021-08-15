# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# 18. Recursion
# ==============

# Version 1

def r_max(nxs):
    """
      Find the maximum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    max_ = None
    for e in nxs:
        if type(e) != list:
            max_ = e if not max_ else max(max_, e)
        else:
            max_ = r_max([max_, *e])
    return max_


assert r_max([]) is None
assert r_max([2, 9, [1, 13], 8, [], 6]) == 13
assert r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100
assert r_max([2, 9, [1, 13], 8, 6]) == 13
assert r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100
assert r_max(["joe", ["sam", "ben"]]) == "sam"


# Version 2

def r_max(nxs):
    """
      Find the maximum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    max_ = None
    first_time = True
    for e in nxs:
        val = r_max(e)  if type(e) == list else e

        if first_time:
            max_ = val
            first_time = False

        if val > max_:
            max_ = val

    return max_


assert r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100
assert r_max([2, 9, [1, 13], 8, 6]) == 13
assert r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100
assert r_max(["joe", ["sam", "ben"]]) == "sam"
