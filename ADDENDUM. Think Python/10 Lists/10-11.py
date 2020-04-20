'''
Exercise 10.11. Two words are a “reverse pair” if each is the reverse of
the other. Write a program that finds all the reverse pairs in the word list.
Solution: http://thinkpython2.com/code/reverse_pair.py
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
    dict_filename = 'words.txt'
    words_list = load_words(dict_filename)

    reversed_pairs = []
    for word in words_list:
        reversed_word = word[::-1]
        if in_bisect(reversed_word, words_list) > -1:
            reversed_pairs.append((word, reversed_word))

    print('\n'.join(map(lambda pair: ' '.join(pair),reversed_pairs)))

    print(f'\nTotal {len(reversed_pairs)} reversed pairs')


if __name__ == '__main__':
    main()
