'''
Exercise 11.1. Write a function that reads the words in words.txt and stores
them as keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
If you did Exercise 10.10, you can compare the speed of this implementation
with the list in operator
and the bisection search.
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

    words_dict = {word : "" for word in words_list}

    test_words = \
        ['chimed', 'homogenizes', 'rooms', 'outcaste',
        'knowledgeable', 'belladonnas', 'lignitic', 'chair', 'inventions',
        'spicules', 'grigris', 'myology', 'cuckoos', 'manlier', 'foredone',
        'software', 'dwell', 'hematine', 'would', 'ensnared','noncorrosive',
        'ordines', 'lifebloods', 'mellifluous', 'ship',
        'xnq', 'hxmapoogpwhcwpuyo', 'enzwfoem', 'yjamzjzkwdnwcvilof', 'nwe',
        'hpqhoetgvgnjcqjelim', 'oo', '', 'uicruitrokp', 'xiwwhfc', 'lsqyqzox',
        'hwiovqfqnimf', 'wvlkazopswqpjiybauz', 'bukukvwtadcea', 'lzdkfvkjvkn'
        'pihcftuukjwwbvhd', 'cejqipfiajcrzoch', '', 'gvohh', 'dvov', 'gkz',
        'ggkddmdzfaeijsj', 'cnazoykevoabqp', 'ywun', 'ygukfnw', 'jjpnhngwhei']


    repeat_times = 10000

    import time

    start_time = time.time()
    for i in range(repeat_times):
        for word in test_words:
            in_bisect(word, words_list)
    t1 = time.time() - start_time

    start_time = time.time()
    for i in range(repeat_times):
        for word in test_words:
            word in words_dict
    t2 = time.time() - start_time

    print(t1)
    print(t2)


if __name__ == '__main__':
    main()
