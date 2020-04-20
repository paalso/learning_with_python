'''
Exercise 10.12. Two words “interlock” if taking alternating letters from each
forms a new word. For example, “shoe” and “cold” interlock to form “schooled”.
Solution: http://thinkpython2.com/code/interlock.py

1. Write a program that finds all pairs of words that interlock. Hint: don’t
enumerate all pairs!
2. Can you find any words that are three-way interlocked; that is, every third
letter forms a word, starting from the first, second or third?
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

    dict_filename = 'words_3000.txt'
    words_list = load_words(dict_filename)

    lengths_dict = dict(collections.Counter(map(len, words_list)))
    maximum_words = max(lengths_dict.values())
    max_word_len = max(lengths_dict.keys())
    total_words = len(words_list)

    max_gistogram_row = 60

    print('\nEnglish most common words lengths distribution gistogram')
    for i in range(1, max_word_len + 1):
        words_qty = lengths_dict.get(i, 0)
        row_len = int((words_qty / maximum_words) * max_gistogram_row)
        print('{0:2}|{1} {2}'.format(i, "#" * row_len, words_qty if words_qty > 0 else ''))


if __name__ == '__main__':
    main()
