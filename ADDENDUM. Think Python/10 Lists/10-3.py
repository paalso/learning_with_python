'''
Exercise 10.3. Write a function called middle that takes a list and returns
a new list that contains all but the first and last elements.
'''

def middle(L):
    return L[1:-1]


t = [1, 2, 3, 4]
print(middle(t))    # [2, 3]
