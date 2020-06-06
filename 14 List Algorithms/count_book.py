from testtools import test
import time


def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for index, item in enumerate(xs):
        if item == target:
            return index
    return -1


def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lower = 0
    upper = len(xs)

    while lower < upper:
        mid = (lower + upper) // 2
        if xs[mid] == target:
            return mid
        if xs[mid] < target:
            lower = mid + 1
        else:
            upper = mid
    return -1


def find_unknown_words(vocab, book_words):
    """ Return a list of words in wds that do not occur in vocab """
    unknown_words = []
    for word in book_words:
        if (search_binary(vocab, word) < 0):
            unknown_words.append(word)
    return unknown_words


def load_words_from_file(filename):
    file = open(filename, 'r')
    file_content = file.read()
    file.close()
    return file_content.split()


def text_to_words(text):
    translator = str.maketrans(
##  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'-!\"#$%&()*+,./:;<=>?@[]^_`{|}~\\",
        "abcdefghijklmnopqrstuvwxyz                                          ")
    cleared_text = text.translate(translator)
    return cleared_text.split()


def get_words_in_book(filename):
    file = open(filename, 'r')
    file_content = file.read()
    file.close()
    return text_to_words(file_content)


def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    if len(xs) == 0:
        return []
    adjacented = [xs[0]]
    for el in xs:
        if adjacented[-1] != el:
            adjacented.append(el)
    return adjacented


all_words = get_words_in_book("alice_in_wonderland.txt")
all_words.sort()
book_words = remove_adjacent_dups(all_words)
print("There are {0} words in the book, the first 100 are\n{1}".
           format(len(book_words), book_words[:100]))

dict = load_words_from_file('vocab.txt')

t0 = time.time()
missing_words = find_unknown_words(dict, book_words)
t1 = time.time()

print("There are {0} words in the book. Only {1} are unique.".
                      format(len(all_words), len(book_words)))
print("The first 100 words are\n{0}".
           format(book_words[:100]))