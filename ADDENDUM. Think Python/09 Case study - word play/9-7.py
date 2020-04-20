'''
Exercise 9.7.
Give me a word with three consecutive double letters. I’ll give you a couple
of words that almost qualify, but don’t. For example, the word committee,
c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there.
Or Mississippi: M-i-s-s-i-s-s-i-p-p-i...
Of course there are probably 500 more but I can only think of one. What is the word?
'''


def check_three_consecutive_double_letters(word):
    """
    Returns True if the word includes three consecutive double letters
    """
    for i in range(len(word) - 5):
        if      word[i] == word[i + 1] \
            and word[i + 2] == word[i + 3] \
            and word[i + 4] == word[i + 5] \
            and len({word[i], word[i + 2], word[i + 4]}) == 3:
                return True
    return False


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

# All the words with three consecutive double letters
required_words = list(filter(check_three_consecutive_double_letters, words))

print("All the words with three consecutive double letters: {}"
    .format(required_words))
