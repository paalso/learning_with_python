'''
Exercise 10.4. Write a function called chop that takes a list, modifies it
by removing the first and last elements, and returns None.
'''

def middle(L):
    L.pop()
    L.pop(0)


t = [1, 2, 3, 4]
print(middle(t))    # None
print(t)            # [2, 3]
