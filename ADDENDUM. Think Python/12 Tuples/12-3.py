'''
Exercise 12.3. Two words form a “metathesis pair” if you can transform one
into the other by swapping two letters; for example, “converse” and “conserve”.
Write a program that finds all of the metathesis pairs in the dictionary.
Hint: don’t test all pairs of words, and don’t test all possible
swaps. Solution: http://thinkpython2.com/code/metathesis.py
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


def dict_anagrams(dict_filename):
    import collections

    words_list = load_words(dict_filename)
    # !!! Использование collections.defaultdict
    def new_list(): return []
    anagrams = collections.defaultdict(new_list)

    for word in words_list:
        anagram = tuple(sorted(word))
        anagrams[anagram].append(word)

    true_anagrams = list(filter(lambda L: len(L) > 1, anagrams.values()))
    true_anagrams.sort(key = lambda L: -len(L))

    return true_anagrams


def words_difference(word1, word2):
    if len(word1) == len(word2):
        indices = []
        s = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                s += 1
                indices.append(i)

        return (s, indices)


def check_metathesis(word1, word2):
    dif, indices = words_difference(word1, word2)
    if  dif != 2:
        return False
    i, j = indices
    return (word1[i], word1[j]) == (word2[j], word2[i])


def main():

    dict_filename = 'words.txt'
    anagrams = dict_anagrams(dict_filename)

    metatheses = []

    for L in anagrams:
        if len(L) == 2:
            if check_metathesis(L[0], L[1]):
                metatheses.append(L)
        else:
            for word1 in L:
                for word2 in L:
                    if word1 != word2 and check_metathesis(word1, word2):
                        metatheses.append([word1, word2])

    for L in metatheses:
        print(*L)

    print(f'\n{len(anagrams)} metathesis pairs were found')


if __name__ == '__main__':
    main()
