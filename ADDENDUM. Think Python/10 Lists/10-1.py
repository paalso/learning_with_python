'''
Exercise 10.1. Write a function called nested_sum that takes a list of lists
of integers and adds up the elements from all of the nested lists.
'''

def nested_sum(L):
    s = 0
    for el in L:
        if type(el) == int:
            s += el
        else:
            s += nested_sum(el)
    return s


print(nested_sum([]))             # 0
print(nested_sum([1, 2, 3, 4, 5, 6]))             # 21
print(nested_sum([[1, 2], [3], [4, 5, 6]]))             # 21
print(nested_sum([[1, 2], [3], [[4], [5, [6]]]]))       # 21
