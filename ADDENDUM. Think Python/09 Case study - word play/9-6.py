'''
Exercise 9.6. Write a function called is_abecedarian that returns True if
the letters in a word appear in alphabetical order (double letters are ok).
How many abecedarian words are there?
'''

def is_abecedarian(word):
    """
    Returns True if the letters in a word appear in alphabetical order
    (double letters are ok)
    """
    word = word.lower()
    for i in range(1, len(word)):
        if word[i] < word[i - 1]:
            return False
    return True


def load_words(dict_filename):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print(f"Loading word list from file {dict_filename}...")
    # in_file: file
    in_file = open(dict_filename, 'r')
    # line: string
    # wordlist: list of strings
    wordlist = in_file.read().split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


print()
# words = load_words("words_3000.txt")
words = load_words("words.txt")
words_qty = len(words)

abecedarian_words = list(filter(is_abecedarian, words))
abecedarian_words_qty = len(abecedarian_words)
print(abecedarian_words)
print("Abecedarian words number: {}, {}%".
    format(abecedarian_words_qty, round(abecedarian_words_qty / words_qty * 100, 1)))
