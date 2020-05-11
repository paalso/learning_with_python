'''
Exercise 13.2. Go to Project Gutenberg (http: // gutenberg. org ) and
download your favorite out-of-copyright book in plain text format.
Modify your program from the previous exercise to read the book you downloaded,
skip over the header information at the beginning of the file, and process
the rest of the words as before.
Then modify the program to count the total number of words in the book, and
the number of times each word is used.
Print the number of different words used in the book. Compare different books
by different authors, written in different eras. Which author uses the most
extensive vocabulary?

Exercise 13.3. Modify the program from the previous exercise to print
the 20 most frequently used words in the book.
'''


def load_words(book, stopwords = [], print_load_info = False):
    import string, requests

    FINAL_WORDS_MARKERS = ['End of Project Gutenberg',
                           'End of the Project Gutenberg' ]

    url = book['url']

    if print_load_info:
        print(f"Loading {book['title']} by {book['author']} from {url}...")

    text = requests.get(url).text
    transtab = str.maketrans(
        string.punctuation, ' ' * len(string.punctuation))
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

    all_frequent_words = set()

    for book in books_net.books_info:
        words = load_words(book)
        # print(words)
        freq_dict = dict_from_list(words)
        words_number = len(words)
        unique_words_number = len(freq_dict)
        words_frequencies = sort_dict_by_frequency(freq_dict)
        print('\'{}\' by {}, publication year: {}'.
            format(book['title'], book['author'], book['year']))
        print('Total number of words: {}'.format(words_number))
        print('Number of unique words : {}'.format(unique_words_number))
        print('Number of unique words per 10 000 words : {}'.
            format(round(unique_words_number / (words_number / 10000))))

        most_frequent_words = list(map(lambda t: t[0], words_frequencies[:20]))
        all_frequent_words |= set(most_frequent_words)

        print('Most frequent words: {}'.format(', '.join(most_frequent_words)))
        print()

    print(all_frequent_words)


if __name__ == '__main__':
    main()
