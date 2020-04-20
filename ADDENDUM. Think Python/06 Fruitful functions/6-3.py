'''
Exercise 6.3. A palindrome is a word that is spelled the same backward and
forward, like “noon” and “redivider”. Recursively, a word is a palindrome
if the first and last letters are the same and the middle is a palindrome.

    2. Write a function called is_palindrome that takes a string argument and
    returns True if it is a palindrome and False otherwise. Remember that you
    can use the built-in function len to check the length of a string.
'''

def is_palindrome(string):
    spec_symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
    s = ''.join(filter(lambda c: c not in spec_symbols, string.lower()))

    def is_palindrome_helper(string):
        if len(string) < 2:
            return True
        return string[0] == string[-1] and is_palindrome_helper(string[1:-1])

    return is_palindrome_helper(s)


print(is_palindrome(''))
print(is_palindrome('1'))
print(is_palindrome('ab'))
print(is_palindrome('abba'))
print(is_palindrome('I did, did I?'))
print(is_palindrome('Eva, can I see bees in a cave?'))
print(is_palindrome('Red rum, sir, is murder'))
