'''
Exercise 10.5. Write a function called is_sorted that takes a list as
a parameter and returns True if the list is sorted in ascending order and
False otherwise.
'''

def is_sorted(L):
    for i in range(1, len(L)):
        if L[i] < L[i - 1]:
            return False
    return True


t1 = []
t2 = [1]
t3 = [1, 2, 3, 4, 5, 6, 7]
t4 = [10, 2, 3, 4, 5, 6, 7]

print(is_sorted(t1))    # True
print(is_sorted(t2))    # True
print(is_sorted(t3))    # True
print(is_sorted(t4))    # False
