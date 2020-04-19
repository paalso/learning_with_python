'''
Exercise 10.6. Two words are anagrams if you can rearrange the letters from one
to spell the other. Write a function called is_anagram that takes two strings
and returns True if they are anagrams
'''

import random


def is_anagram(text1, text2):
##    return sorted(text1) == sorted(text2)
    L1 = list(text1)
    L1_copy = list(text1)
    L2 = list(text2)
    for c in L1:
        L1.remove(c)
        try:
            L2.remove(c)
        except:
            return False
    if L2 == '':
        return False
    return True


print(is_anagram('bamboo', 'amboob'))    # True
print(is_anagram('bambook', 'amboob'))    # False

s = 'aliasdhbfiusabvdcvui'
L = list('aliasdhbfiusabvdcvui')

for i in range(5):
    L_copy = L[:]
    random.shuffle(L_copy)
    shuffled_s = ''.join(L_copy)
    print(is_anagram(s, shuffled_s))
