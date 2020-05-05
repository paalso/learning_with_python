'''
Exercise 12.4. What is the longest English word, that remains a valid English
word, as you remove its letters one at a time?
Now, letters can be removed from either end, or the middle, but you can’t
rearrange any of the letters. Every time you drop a letter, you wind up with
another English word. If you do that, you’re eventually going to wind up with
one letter and that too is going to be an English word—one that’s found in
the dictionary. What’s the longest word and how many letters does it have?
'''
'''
Версия, к-я загружает пользуется словарем с диска
'''

def load_words(dict_filename, dict_value = True):
    import time
    """
    Returns a dictionary of valid words. Words are strings of lowercase letters.
    """
    start_time = time.time()
    print(f"Loading dictionary from file {dict_filename}...")
    # in_file: file
    with open(dict_filename, 'r') as in_file:
        wordsdict = dict.fromkeys(in_file.read().split(), dict_value)
    passed_time = time.time() - start_time
    print(f"{len(wordsdict)} words loaded, {passed_time} seconds passed")
    return wordsdict


def word_reduction_chains(word, wordsdict):

    L = []

    def helper(w, words_chain):
        for i in range(len(w)):
            shortened_word = w[:i] + w[i + 1:]
            if shortened_word in wordsdict:
                words_chain_copy = words_chain[:]
                words_chain_copy.append(shortened_word)
                L.append(words_chain_copy)
                helper(shortened_word, words_chain_copy)

    helper(word, [word])

    if L:
        max_chain_len = max(map(len, L))
        longest_chains = filter(lambda chain: len(chain) == max_chain_len, L)
        return list(longest_chains)


def main():

    dict_filename = 'words_3000.txt'
    wordsdict = load_words(dict_filename)

    chains = []
    reductible_words = set()

    for word in sorted(wordsdict.keys(), key=(lambda w: - len(w))):
        if word in reductible_words:
            continue
        word_chains = word_reduction_chains(word, wordsdict)
        if word_chains:
            chains.extend(word_chains)
            reductible_words = reductible_words.union(*word_chains)

    max_chain_len = max(map(len, chains))
    longest_chains = filter(lambda chain: len(chain) == max_chain_len, chains)

    max_reductible_word_len = max(map(len, reductible_words))
    longest_reductible_words = list(filter(
        lambda w: len(w) == max_reductible_word_len, reductible_words))

    print('Longest chains:')
    for chain in longest_chains:
        print(*chain)

    print()
    print('Longest reductible_words:')
    print('\n'.join(longest_reductible_words))


if __name__ == '__main__':
    main()
