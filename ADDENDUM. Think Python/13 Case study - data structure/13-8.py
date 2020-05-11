'''
Exercise 13.8. Markov analysis:
1. Write a program to read a text from a file and perform Markov analysis.
The result should be a dictionary that maps from prefixes to a collection of
possible suffixes. The collection might be a list, tuple, or dictionary; it is
up to you to make an appropriate choice. You can test your program with prefix
length two, but you should write the program in a way that makes it easy
to try other lengths.

2. Add a function to the previous program to generate random text based on
the Markov analysis.
Here is an example from Emma with prefix length 2:
    ...He was very clever, be it sweetness or be angry, ashamed or only amused,
    at such a stroke. She had never thought of Hannah till you were never meant
    for me?" "I cannot make speeches, Emma:" he soon cut it all himself...

For this example, I left the punctuation attached to the words. The result is
almost syntactically correct, but not quite. Semantically, it almost makes
sense, but not quite.
What happens if you increase the prefix length? Does the random text make
more sense?

3. Once your program is working, you might want to try a mash-up: if you
combine text from two or more books, the random text you generate will blend
the vocabulary and phrases from the sources in interesting ways.
Credit: This case study is based on an example
Solution: http://thinkpython2.com/code/markov.py.
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

##Замечание:
##надо бы заменить list -> set, а то получается нечто вроде:
##'it with': ['the', 'a', 'i', 'a', 'a', 'the', 'eager', 'what', 'pleasure',
##'her', 'a', 'the', 'a']. С другой стороны, именно в этом формате сохраняется
##информация о вероятности появления следующих за префиксом слов.
##Хотя это можно решить заменой на dict

def markov_processed_dict(wordslist, prefixlen=2):
    '''Reads a file and performs Markov analysis.

    wordslist: list
    prefixlen: integer number of words in the prefix

    returns: map from prefix to list of possible suffixes.
    import collections
    '''
    import collections
    suffix_map = collections.defaultdict(lambda : [])
    for i, word in enumerate(wordslist[:len(wordslist) - prefixlen]):
        key = ' '.join(wordslist[i: i + prefixlen])
        suffix_map[key].append(wordslist[i + prefixlen])

    return dict(suffix_map)


def random_text(suffix_map, n=100):
    '''Generates random wordsfrom the analyzed text.
    Starts with a random prefix from the dictionary.
    suffix_map: map from prefix to list of possible suffixes
    n: number of words to generate
    '''
    import random
    # choose a random prefix (not weighted by frequency)
    random_list = []
    start = random.choice(list(suffix_map.keys()))
    random_list.extend(start.split())

    for i in range(n - 2):
        next_key = ' '.join(random_list[-2:])
        if next_key not in suffix_map:
            break
        next_word = random.choice(suffix_map[next_key])
        random_list.append(next_word)

    return ' '.join(random_list)


def main():
    text_info = 'texts/emma.txt', '*END*THE SMALL PRINT!'
    filename, start_marker = text_info
    wordslist = process_text(filename, start_marker, True)
    print(wordslist)

##    L = ['nostrud', 'exercitation', 'ullamco', 'laboris', 'nisi', 'ut', 'asvsdav', 'ujnrrn']
##    markov_dict = markov_processed_dict(L)

    markov_dict = markov_processed_dict(wordslist, 2)
    print(random_text(markov_dict, 20))


if __name__ == '__main__':
    main()
