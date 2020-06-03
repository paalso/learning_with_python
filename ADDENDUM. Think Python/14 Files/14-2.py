'''
Exercise 14.2. If you download my solution to Exercise 12.2 from
http://thinkpython2.com/code/anagram_sets.py , you’ll see that it creates
a dictionary that maps from a sorted string of letters to the list of words
that can be spelled with those letters. For example, 'opst' maps to the list
['opts', 'post', 'pots', 'spot', 'stop', 'tops'].
Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf”; read_anagrams
should look up a word and return a list of its anagrams.
Solution: http://thinkpython2.com/code/anagram_db.py .
'''

import load_words, anagram_sets


def main():

##    dict_filename = '../words.txt'
##    words_list = load_words.load_words(dict_filename)
##    # Generating anagrams dictionary
##    anagrams_dict = anagram_sets.all_anagrams_dict(words_list)
##
##    # Saving the anagrams dictionary as a pickle db
##    anagram_sets.store_anagrams(anagrams_dict)

    word = 'wasted'
    key = ''.join(sorted(word))
    print(f'word: {word}, key: {key}')

    # Reading the anagrams dictionary from the pickle db
    anagrams_dict_from_db = anagram_sets.read_anagrams()

    # Searching for the given word in the anagrams dictionary
    if key in anagrams_dict_from_db:
        print(anagrams_dict_from_db[key])
    else:
        print(f'No anagrams for the word {word}')


if __name__ == '__main__':
    main()
