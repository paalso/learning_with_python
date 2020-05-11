# 13-2_3.py
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

Exercise 13.6. Python provides a data structure called set that provides many
common set operations. Write a program that uses set subtraction to find words
in the book that are not in the word list.
Solution: http://thinkpython2.com/code/analyze_book2.py

'''

def load_words(dict_filename):
    with open(dict_filename, 'r') as in_file:
        wordlist = in_file.read().split()
    return dict.fromkeys(wordlist, True)


def process_text(filename, start_marker='', print_load_info=False):
    import string

    FINAL_MARKERS = ['End of Project Gutenberg',
                     'End of the Project Gutenberg',
                     # 'ABOUT THE AUTHORS'
                    ]
    ADDITIONAL_SYMBOLS = '“”’—'

    histogram = dict()

    if print_load_info:
        print(f"Loading {filename}...")

    with open(filename, 'r') as finput:

        for line in finput:
            if line.startswith(start_marker):
                break

        for line in finput:
            for final_marker in FINAL_MARKERS:
                if line.startswith(final_marker):
                    break
#            print(line)
            for word in line.replace('-', ' ').split():
                word = word.lower().strip(string.punctuation)
                histogram[word] = histogram.get(word, 0) + 1

    if print_load_info:
        print(f'{sum(histogram.values())} words loaded')

    return histogram


def sort_dict_alphabetically(dictionary):
    sorted_keys = sorted(dictionary.keys())
    return list(zip(sorted_keys, map(lambda key: dictionary[key], sorted_keys)))


def sort_dict_by_frequency(dictionary):
    return sorted(dictionary.items(), key=lambda t: -t[1])


def print_most_common(hist, num=10):
    print('Most frequent words:')
    for value, key in sort_dict_by_frequency(hist)[:num]:
        print('{:<10}{:>5}'.format(value, key))


def subtract(dict1, dict2):
#    return {key : dict1[key] for key in dict1 if key not in dict2.keys()}
    return set(dict1) - set(dict2)


def main():
    import books_net

    vocabulary_filename = 'words.txt'
    vocabulary = load_words(vocabulary_filename)

    # Странный формат, много нестандарных символов - плохо парсится,в общем
    text_info = 'texts/Strugatsky Arkady. The Final Circle of Paradise - royallib.ru.txt', 'San Diego, California, 1977'
    text_info = 'texts/Strugatsky Arcady. Prisoners of Power - royallib.com.txt', 'San Diego, California, 1977'
    text_info = 'texts/Bulychev Kir. The Girl From Earth.txt', 'Copyright 2002 by Kir Bulychev'

    text_info = 'texts/grimm.txt', 'Marian Edwardes.'
    text_info = 'lorem.txt', ''
    text_info = 'texts/carroll.txt', 'THE MILLENNIUM FULCRUM EDITION 3.0'
    text_info = 'texts/alice_in_wonderland.txt', '                     (C)1991 Duncan Research'
    text_info = 'texts/emma.txt', '*END*THE SMALL PRINT!'

    filename, start_marker = text_info
    freq_dict = process_text(filename, start_marker, True)
#    print(freq_dict)

    words_number = sum(freq_dict.values())
    unique_words_number = len(freq_dict)

    print(f'\nFilename: {filename}')
    print('Total number of words: {}'.format(words_number))
    print('Number of unique words : {}'.format(unique_words_number))
    print('Number of unique words per 10 000 words : {}'.
        format(round(unique_words_number / (words_number / 10000))))
    print_most_common(freq_dict)
    print()
#    absent_word = subtract(freq_dict, vocabulary).keys()
    absent_word = subtract(freq_dict, vocabulary)
    print("Words in the book that aren't in the vocabulary {} ({} words):"
        .format(vocabulary_filename, len(absent_word)))
    print('  '.join(absent_word))


if __name__ == '__main__':
    main()
