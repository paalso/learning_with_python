'''
Exercise 13.4. Modify the previous program to read a word list
(see Section 9.1) and then print all the words in the book that are not in
the word list. How many of them are typos? How many of them are common words
that should be in the word list, and how many of them are really obscure?
'''


def load_words(dict_filename):
    """
    Returns a dict of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print(f"Loading word list from file {dict_filename}...")
    with open(dict_filename, 'r') as in_file:
        wordlist = in_file.read().split()
    print("  ", len(wordlist), "words loaded.")
    return dict.fromkeys(wordlist, True)


def load_book(book, stopwords = [], print_load_info = False):
    import string, requests

    FINAL_WORDS_MARKERS = ['End of Project Gutenberg',
                           'End of the Project Gutenberg' ]

    url = book['url']

    if print_load_info:
        print(f"Loading {book['title']} by {book['author']} from {url}...")

    text = requests.get(url).text
    transtab = str.maketrans(string.punctuation + string.digits,
        ' ' * len(string.punctuation + string.digits))
    # Надо бы как-нибудь правильно слова с апострофом обработать!!!

    start_pos = text.find(book['start'])

    for marker in FINAL_WORDS_MARKERS:
        end_pos = text.find(marker)
        if end_pos > 0:
            break

    # print(text[start_pos:end_pos])

    refined_text = text[start_pos:end_pos].translate(transtab).lower()

    wordlist = list(
        filter(lambda w: w not in set(stopwords), refined_text.split()))
    return wordlist


def dict_from_list(words_list):
    import collections
    return dict(collections.Counter(words_list))


def sort_dict_alphabetically(dictionary):
    sorted_keys = sorted(dictionary.keys())
    return list(zip(sorted_keys, map(lambda key: dictionary[key], sorted_keys)))


def sort_dict_by_frequency(dictionary):
    return sorted(dictionary.items(), key=lambda t: -t[1])


def main():
    import books_net

    STOP_LIST = [
        'in', 'on', 'and', 'that', 'my', 'me', 'for', 'the', 'as', 'to', 'i',
        'but', 'a', 'all', 'up', 'is', 'was', 'with', 'he', 'had', 'at', 'him',
        'her', 'which', 's', 'she', 'said', 't', 'it', 'mr', 'we', 'of', 'you',
        'so', 'alice', 'his' ]

    dict_filename = 'words.txt'
    dict_filename = 'dictionaries/large'
    dictionary = load_words(dict_filename)

    book = books_net.books_info[1]
    book_words = load_book(book)

    uniq_words = dict.fromkeys(book_words, True)

    words_number = len(book_words)
    unique_words_number = len(uniq_words)

    non_dict_book_words = list(
        filter(lambda word: word not in dictionary, uniq_words.keys()))

    print('\'{}\' by {}, publication year: {}'.
        format(book['title'], book['author'], book['year']))
    print('Total number of words: {}'.format(words_number))
    print('Number of unique words : {}'.format(unique_words_number))
    print('Number of unique words per 10 000 words : {}'.
        format(round(unique_words_number / (words_number / 10000))))
    print('Words absent in the dictionary {}:\n {}'.
        format(dict_filename, ' '.join(non_dict_book_words)))


if __name__ == '__main__':
    main()
