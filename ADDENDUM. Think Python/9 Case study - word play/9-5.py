'''
Exercise 9.5. Write a function named uses_all that takes a word and a string
of required letters, and that returns True if the word uses all the required
letters at least once. How many words are there that use all the vowels aeiou?
How about aeiouy?
'''


def uses_all(word, required_letters):
    """
    Returns True if the word uses all the required letters at least once
    """
    return set(required_letters.lower()).issubset(set(word.lower()))



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

used_letters = 'aeiou'

all_vowels_words = list(filter(lambda w: uses_all(w, used_letters), words))
##print(all_vowels_words)
print("All the vowels words number: {}".format(len(all_vowels_words)))
print('They are: {}...'.format(all_vowels_words[:10]))

min_len = min(map(len, all_vowels_words))
shortes_all_vowels_words = filter(lambda w: len(w) == min_len, all_vowels_words)
print("The shortest words containing all the vowels: {}"
    .format(list(shortes_all_vowels_words)))
