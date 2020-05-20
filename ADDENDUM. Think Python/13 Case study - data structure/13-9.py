'''
Exercise 13.9. The “rank” of a word is its position in a list of words sorted
by frequency: the most common word has rank 1, the second most common has
rank 2, etc.

Zipf’s law describes a relationship between the ranks and frequencies of words
in natural languages (http://en.wikipedia.org/wiki/Zipf's_law ).
Specifically, it predicts that the frequency, f, of the word with rank r is:

f = c * pow(p, -s)

where s and c are parameters that depend on the language and the text.
If you take the logarithm of both sides of this equation, you get:

log f = log c − s * log r

So if you plot log f versus log r, you should get a straight line with slope −s
and intercept log c. Write a program that reads a text from a file, counts word
frequencies, and prints one line for each word, in descending order
of frequency, with log f and log r. Use the graphing program of your choice
to plot the results and check whether they form a straight line.
Can you estimate the value of s?

Solution: http://thinkpython2.com/code/zipf.py
To run my solution, you need the plotting module matplotlib.
'''

def process_text(filename, start_marker='', print_load_info=False):
    import string

    FINAL_MARKERS = ['End of Project Gutenberg',
                     'End of the Project Gutenberg',
                     # 'ABOUT THE AUTHORS'
                    ]
    ADDITIONAL_SYMBOLS = '“”’—'

    wordslist = []

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
                wordslist.append(word)

    if print_load_info:
        print(f'{len(wordslist)} words loaded')

    return wordslist


def dict_from_list(words_list):
    import collections
    return dict(collections.Counter(words_list))


def sort_dict_by_frequency_decreasing(histogram):
    return sorted(histogram.items(), key=lambda t: -t[1])


def invert_dict(d):
    from collections import defaultdict
    reversed_d = defaultdict(lambda : [])

    for key, value in d.items():
        reversed_d[value].append(key)
    return dict(reversed_d)


def get_Zipf_ranks(histogram):
    inverted_histogram = invert_dict(histogram)
    zipf_ranks = dict()
    for i, freq in enumerate(sorted(inverted_histogram.keys(), reverse=True), start=1):
        words = inverted_histogram[freq]
        for word in words:
            zipf_ranks[word] = i
    return zipf_ranks


def print_most_common(hist, num=10):
    print('Most frequent words:')
    for value, key in sort_dict_by_frequency_decreasing(hist)[:num]:
        print('{:<10}{:>5}'.format(value, key))


def main():
    text_info = 'texts/wordsworth.txt', ''
    text_info = 'texts/carroll.txt', 'THE MILLENNIUM FULCRUM EDITION 3.0'
    text_info = 'texts/emma.txt', '*END*THE SMALL PRINT!'
    filename, start_marker = text_info
    words_list = process_text(filename, start_marker, True)
    freq_dict = dict_from_list(words_list)
    zipf_ranks = get_Zipf_ranks(freq_dict)

    sorted_words = list(map(
        lambda t: t[0], sort_dict_by_frequency_decreasing(freq_dict)))

    import math, matplotlib.pyplot as plt
    ranks       = [zipf_ranks[word] for word in sorted_words]
    frequencies = [freq_dict[word] for word in sorted_words]
    args_list = list(map(math.log,  ranks))
    vals_list = list(map(math.log,  frequencies))
    plot_line = plt.plot(args_list, vals_list, marker='.')
    plt.title('ln(frequency) as a function of ln(rank)')
    plt.show()


if __name__ == '__main__':
    main()
