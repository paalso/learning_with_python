'''
Exercise 11.6. Here’s another Puzzler from Car Talk...
This was sent in by a fellow named Dan O’Leary. He came upon a common
one-syllable, five-letter word recently that has the following unique property.
When you remove the first letter, the remaining letters form a homophone of
the original word, that is a word that sounds exactly the same. Replace
the first letter, that is, put it back and remove the second letter and
the result is yet another homophone of the original word. And the
question is, what’s the word?
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


def load_pronouncings(dict_filename):
    print(f"Loading words pronounsings list from file {dict_filename}...")
    in_file = open(dict_filename, 'r')
    pronouncings = {}
    for line in in_file:
        tokens = line.lower().split()
        pronouncings[tokens[0]] = ' '.join(tokens[1:])
    print("  ", len(pronouncings), "words loaded.")
    return pronouncings


def main():
    import time

    dict_filename = 'words.txt'
    words = load_words(dict_filename)

    five_letters_words = filter(lambda word: len(word) == 5, words)

    def one_syllable(word):
        vowels = ('a', 'e', 'i', 'o', 'u')
        counter = 0
        for letter in vowels:
            counter += word.count(letter)
            if counter > 1:
                return False
        return counter == 1

    five_letters_one_syllable_words = filter(one_syllable, five_letters_words)

    # http://greenteapress.com/thinkpython2/code/c06d
    pronouncings_filename = 'c06d.txt'

    pronouncings = load_pronouncings(pronouncings_filename)

##    print(pronouncings)

    removed_first_homophones = []
    for word in five_letters_one_syllable_words:
        if word not in pronouncings:
            continue

        if pronouncings.get(word[1:], '') == pronouncings[word]:
            removed_first_homophones.append(word)

    removed_second_homophones = []
    for word in removed_first_homophones:
        if pronouncings.get(word[0] + word[2:], '') == pronouncings[word]:
            removed_second_homophones.append(word)

    print(*removed_second_homophones)


if __name__ == '__main__':
    main()
