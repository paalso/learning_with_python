'''
Exercise 9.4. Write a function named uses_only that takes a word and
a string of letters, and that returns True if the word contains only letters
in the list. Can you make a sentence using only the letters acefhlo?
Other than “Hoe alfalfa”?
'''

def uses_only(word, letters):
    """
    Returns True if the word contains only letters in the list
    """

    return set(word.lower()).issubset(set(letters.lower()))


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
allowed = "acefhlo"

# words = load_words("words_3000.txt")
words = load_words("words.txt")
words_qty = len(words)

allowed_words = list(filter(lambda word: uses_only(word, allowed), words))
allowed_words_qty = len(allowed_words)
print(allowed_words)
print("Allowed words number: {}, {}%".
    format(allowed_words_qty, round(allowed_words_qty / words_qty * 100, 1)))

