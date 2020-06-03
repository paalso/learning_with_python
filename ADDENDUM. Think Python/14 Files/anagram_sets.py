import collections, pickle


def all_anagrams_dict(words_list):
    """
    Returns a dict of the format
    {
        (sorted tuple of letters) :
            [list of all possible anagrams composed of these letters],
    }
    of all the sets of words from the given words_list
    that are anagrams
    """
    anagrams_dict = collections.defaultdict(lambda :[])

    for word in words_list:
        if len(word) == 1:
            continue
        anagram_key = ''.join(sorted(word))
        anagrams_dict[anagram_key].append(word)

    true_anagrams_dict = \
        {key : value for key, value in anagrams_dict.items() if len(value) > 1}

    return true_anagrams_dict


def all_anagrams_list(words_list):
    """
    Returns a list of all the sets of words from the given words_list
    that are anagrams
    """
    anagrams_dict = all_anagrams_dict(words_list)
    anagrams_list = list(anagrams_dict.values())
    anagrams_list.sort(key = lambda L: -len(L))
    return anagrams_list


def store_anagrams(anagrams_dict, filename='anagrams.pickle'):
    """
    Stores the anagram dictionary in a “shelf”
    """
    try:
        with open(filename, 'wb') as f:
            pickle.dump(anagrams_dict, f)
    except:
        print(f'{filename} writing error')


def read_anagrams(filename='anagrams.pickle'):
    """
    Stores the anagram dictionary in a “shelf”
    """
    try:
        with open(filename, 'rb') as f:
            anagrams_dict = pickle.load(f)
    except:
        print(f'{filename} open error')
    return anagrams_dict
