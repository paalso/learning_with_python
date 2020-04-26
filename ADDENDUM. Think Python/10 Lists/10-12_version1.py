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
# Плохая, негодная, тупая, медленная версия
# Bad, inadequate, stupid, slow version.
    dict_filename = 'words.txt'
    words_list = load_words(dict_filename)

    interlocked_words = []

    for size in range(2, 10):
        size_words = list(filter(lambda w: len(w) == size, words_list))
        size_interlocked_words = []
        print(f'Size = {size}, words: {len(size_words)}')
        for word1 in size_words:
            for word2 in size_words:
                if in_bisect(interlock_two_words(word1, word2), words_list) > -1:
                    size_interlocked_words.append((word1, word2, interlock_two_words(word1, word2)))
        interlocked_words.extend(size_interlocked_words)
        print(size_interlocked_words)

    print(interlocked_words)


if __name__ == '__main__':
    main()
