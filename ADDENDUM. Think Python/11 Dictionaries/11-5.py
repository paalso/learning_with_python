'''
Exercise 11.5. Two words are “rotate pairs” if you can rotate one of them and
get the other (see rotate_word in Exercise 8.5).
Write a program that reads a wordlist and finds all the rotate pairs.
Solution: http://thinkpython2.com/code/rotate_pairs.py
'''


def load_words_to_list(dict_filename):
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


def load_words_to_dict(dict_filename):
    """
    Returns a dict of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print(f"Loading word list from file {dict_filename}...")
    # in_file: file
    in_file = open(dict_filename, 'r')
    # line: string
    # wordlist: list of strings
    wordlist = in_file.read().split()
    worddict = {}
    for word in wordlist:
        worddict[word] = 0
    print("  ", len(wordlist), "words loaded.")
    return worddict


def rotate(text, shift):
    shift %= 26

    result_letters = []
    for c in text:
        if not c.isalpha():
            result_letters.append(c)
        elif c.isupper():
            result_letters.append(chr(ord('A') + (ord(c) - ord('A') + shift) % 26))
        else:
            result_letters.append(chr(ord('a') + (ord(c) - ord('a') + shift) % 26))

    return ''.join(result_letters)


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
    import time

    dict_filename = 'words.txt'

##    start_time = time.time()
##    rotate_pairs = []
##    words_list = load_words_to_list(dict_filename)
##    for word in words_list:
##        for i in range(1, 26):
##            new_word = rotate(word, i)
##            if in_bisect(new_word, words_list) > -1:
##                rotate_pairs.append((word, new_word, i))
##    rotate_pairs_number  = len(rotate_pairs)
##    end_time = time.time()
##    print('Method # 1 - binary search in a list')
##    print(f'{rotate_pairs_number} rotated pairs were found')
##    print(f'Time: {end_time - start_time}')

    start_time = time.time()
    rotate_pairs = []
    words_dict = load_words_to_dict(dict_filename)
    for word in words_dict:
        for i in range(1, 26):
            new_word = rotate(word, i)
            if new_word in words_dict:
                rotate_pairs.append((word, new_word, i))
    rotate_pairs_number  = len(rotate_pairs)
    end_time = time.time()
    print('\nMethod # 2 - search in a dict')
    print(f'{rotate_pairs_number} rotated pairs were found')
    print(f'Time: {end_time - start_time}')

##    for word, rotated_word, i in rotate_pairs:
##        print(word, rotated_word, i)


if __name__ == '__main__':
    main()
