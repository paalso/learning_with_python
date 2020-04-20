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

def interlock_two_words(word1, word2):
    L = [' '] * (len(word1) + len(word2))
    L[::2] = list(word1)
    L[1::2] = list(word2)
    return ''.join(L)


def main():

    dict_filename = 'words_3000.txt'
    words_list = load_words(dict_filename)

    print(interlock_two_words('shoe', 'cold'))


if __name__ == '__main__':
    main()
