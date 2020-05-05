'''
Exercise 13.1.
Write a program that reads a file, breaks each line into words, strips
whitespace and punctuation from the words, and converts them to lowercase.
'''


def load_words(dict_filename):
    import string
    transtab = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

    with open(dict_filename, 'r') as in_file:
        text = in_file.read().translate(transtab).lower()

    wordlist = text.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def dict_from_list(words_list):
    import collections
    return dict(collections.Counter(words_list))


def sort_dict(dictionary):
    sorted_keys = sorted(dictionary.keys())
    return list(zip(sorted_keys, map(lambda key: dictionary[key], sorted_keys)))


def main():
    filename = 'alice.txt'
    words = load_words(filename)
    d = dict_from_list(words)
    words_number = len(d)
    print(f'Total number of words in the book : {len(words)}')
    print(f'Number of different words in the book : {len(d)}')


if __name__ == '__main__':
    main()
