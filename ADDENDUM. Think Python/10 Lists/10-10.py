'''
Exercise 10.10. To check whether a word is in the word list, you could use
the in operator, but it would be slow because it searches through the words
in order.
Because the words are in alphabetical order, we can speed things up with
a bisection search (also known as binary search), which is similar to what
you do when you look a word up in the dictionary (the book, not the data
structure). You start in the mid_iddle and check to see whether the word you are
looking for comes before the word in the mid_iddle of the list. If so, you search
the first half of the list the same way. Otherwise you search the second half.
Either way, you cut the remaining search space in half. If the word list has
113,809 words, it will take about 17 steps to find the word or conclude that
it’s not there.
Write a function called in_bisect that takes a sorted list and a target value
and returns True if the word is in the list and False if it’s not.
Solution: http://thinkpython2.com/code/inlist.py
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


def in_bisect(word, words_list):
    first_id = 0
    last_id = len(words_list) - 1

    while first_id <= last_id:
        mid_id = (first_id + last_id) // 2

        if words_list[mid_id] == word:
            return mid_id
        elif words_list[mid_id] < word:
            first_id = mid_id + 1
        else:
            last_id = mid_id - 1

    return -1


def main():
    dict_filename = 'words_3000.txt'
    words_list = load_words(dict_filename)
    words_list = load_words(dict_filename)

    test_words = (
        'a',
        'abandon',
        'youth',
        'zone',
        'war',
        'none',
        'moral',
        'morral',
        'aa',
        'zz',
        'kettle'
    )

    for word in test_words:
        print(f"Position of '{word}': {in_bisect(word, words_list)}")


if __name__ == '__main__':
    main()
