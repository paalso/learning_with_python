'''
Exercise 9.2. In 1939 Ernest Vincent Wright published a 50,000 word novel
called Gadsby that does not contain the letter “e”. Since “e” is the most
common letter in English, that’s not easy to do...
Write a function called has_no_e that returns True if the given word doesn’t
have the letter “e” in it.
Write a program that reads words.txt and prints only the words that have no “e”.
Compute the percentage of words in the list that have no “e”.
'''

def has_no_e(text):
    return 'e' not in text


words_qty = 0
words_without_e_qty = 0
with open('words.txt', 'r') as f:
    for line in f:
        words_qty += 1
        if has_no_e(line):
            print(line.rstrip())
            words_without_e_qty += 1

print()
share = round(words_without_e_qty / words_qty * 100, 1)
print(f"Total words quantity: {words_qty}")
print(f"Words without 'e' quantity: {words_without_e_qty}")
print(f"Words without 'e': {share}%")