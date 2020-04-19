'''
Exercise 10.9. Write a function that reads the file words.txt and builds
a list with one element per word. Write two versions of this function, one
using the append method and the other using the idiom t = t + [x]. Which one
takes longer to run? Why?
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


def count_time(func, *args):
    import time
    start_time = time.time()
    func(*args)
    return time.time() - start_time


def load_words1(dict_filename):
    """
    Returns a list of words from the file 'dict_filename' using
    the append method
    """
    print(f"Loading word list from file {dict_filename}...")
    # in_file: file
    in_file = open(dict_filename, 'r')
    wordlist = []   # wordlist: list of strings
    # line: string
    for line in in_file:
        wordlist.append(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def load_words2(dict_filename):
    """
    Returns a list of words from the file 'dict_filename'
    using the idiom t = t + [x]
    """
    print(f"Loading word list from file {dict_filename}...")
    # in_file: file
    in_file = open(dict_filename, 'r')
    wordlist = []   # wordlist: list of strings
    # line: string
    for line in in_file:
        wordlist += [line]
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def main():
    dict_filename = 'words.txt'
    t1 = count_time(load_words1, dict_filename)
    t2 = count_time(load_words2, dict_filename)
    t3 = count_time(load_words, dict_filename)
##    words = load_words2(dict_filename)
##    print(words)
    print(f'Time of loading the dictionary "{dict_filename}":')
    print(f'using the append method: {t1}')
    print(f'using the the idiom t = t + [x]: {t2}')
    print(f'using the the read().split() method: {t3}')

# https://towardsdatascience.com/3-techniques-to-make-your-python-code-faster-193ffab5eb36

if __name__ == '__main__':
    main()