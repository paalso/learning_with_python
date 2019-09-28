from testtools import test

def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    if len(xs) == 0:
        return []

    adjacented = [xs[0]]
    for el in xs:
        if adjacented[-1] != el:
            adjacented.append(el)
    return adjacented

test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
test(remove_adjacent_dups([]) == [])
test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
                                   ["a", "big", "bite", "dog"])

