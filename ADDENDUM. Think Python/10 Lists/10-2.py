'''
Exercise 10.2. Write a function called cumsum that takes a list of numbers and
returns the cumulative sum; that is, a new list where the ith element is
the sum of the first i + 1 elements from the original list.
'''

def cumsum(L):
    s = 0
    result = []
    for el in L:
        s += el
        result.append(s)
    return result


print(cumsum([]))                   # [0]
print(cumsum([1, 2, 3, 4, 5, 6]))   # [1, 3, 6, 10, 15, 21]
