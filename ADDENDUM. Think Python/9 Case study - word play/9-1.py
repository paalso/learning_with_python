'''
Exercise 9.1. Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

with open('words.txt', 'r') as f:
    words_longer20 = [line.rstrip() for line in f if len(line) > 21]

print(words_longer20)
