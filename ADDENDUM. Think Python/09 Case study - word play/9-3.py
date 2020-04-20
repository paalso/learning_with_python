'''
Exercise 9.3. Write a function named avoids that takes a word and a string
of forbidden letters, and that returns True if the word doesn’t use any
of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters
and then prints the number of words that don’t contain any of them. Can you
ind a combination of 5 forbidden letters that excludes the smallest number
of words?
'''

def avoids(word, forbidden_letters):
    """
    Returns True if the word doesn’t use any of the forbidden letters
    """
    word_letters = set(word.lower())
    return word_letters - set(forbidden_letters.lower()) == word_letters


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
forbidden = "bjqxz"
# words = load_words("words_3000.txt")
words = load_words("words.txt")
words_qty = len(words)

avoided_words = list(filter(lambda word: avoids(word, forbidden), words))
avoided_words_qty = len(avoided_words)
# print(avoided_words)
print("Avoided words number: {}, {}%".
    format(avoided_words_qty, round(avoided_words_qty / words_qty * 100, 1)))


# jqvxz   84.4%
# jkqxz   84.2%
# bjqxz   78.4%
