'''
Exercise 12.1. Write a function called most_frequent that takes a string and
prints the letters in decreasing order of frequency. Find text samples from
several different languages and see how letter frequency varies between
languages.
Compare your results with the tables at
http://en.wikipedia.org/wiki/Letter_frequencies
Solution: http://thinkpython2.com/code/most_frequent.py
'''

def letters_frequencies(text_filename):
    import string, collections

    special_letters = \
        'àâáåäãąæœçĉćčďðèéêëęěĝğĥîìíïıĵłñńňòöôóõøřŝşśšßťþùúûŭüůýźżž'
    all_letters = string.ascii_lowercase + special_letters

    with open(text_filename, 'r', encoding='utf8') as in_file:
        letters_list = map(lambda c: c.lower(), list(in_file.read()))

    text_letters = list(filter(lambda c: c in all_letters, letters_list))

    counted_letters = dict(collections.Counter(text_letters))

    all_letters_number = sum(counted_letters.values())

    return {c : counted_letters[c] / all_letters_number for c in text_letters}


def most_frequent(text_filename):
    frequencies = letters_frequencies(text_filename)
    return sorted(frequencies.keys(), key = lambda c: -frequencies[c])


def main():
    text_filename = 'alice.txt'
    print('English:\n', *most_frequent(text_filename))
    print()
    text_filename = 'france.txt'
    print('French:\n', *most_frequent(text_filename))
    print()
    text_filename = 'deutschland.txt'
    print('German:\n', *most_frequent(text_filename))


if __name__ == '__main__':
    main()
