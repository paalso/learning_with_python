'''
Exercise 12.2. More anagrams!
1. Write a program that reads a word list from a file (see Section 9.1) and
prints all the sets of words that are anagrams.
Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
2. Modify the previous program so that it prints the longest list of anagrams
first, followed by the second longest, and so on.
3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along
with a letter on the board, to form an eight-letter word. What collection of
8 letters forms the most possible bingos?
'''


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


def main():
    import collections

    dict_filename = 'words.txt'
    words_list = load_words(dict_filename)

    # !!! Использование collections.defaultdict
    def new_list(): return []
    anagrams = collections.defaultdict(new_list)

    for word in words_list:
        anagram = tuple(sorted(word))
        anagrams[anagram].append(word)

    true_anagrams = list(filter(lambda L: len(L) > 1, anagrams.values()))
    true_anagrams.sort(key = lambda L: -len(L))

##    for L in true_anagrams:
##        print(*L)

    print(f'\n{len(true_anagrams)} anagram series were found')

    print('\nNow let\'s find 8 letters anagrams:')
    anagrams8 = list(filter(lambda L: len(L[0]) == 8, true_anagrams))
    anagrams8.sort(key = lambda L: len(L))
    for L in anagrams8:
        print(*L)

    print(f'\n{len(anagrams8)} 8 letters anagram series were found')


if __name__ == '__main__':
    main()
