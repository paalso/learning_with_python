from string import punctuation


def cleanword(word):
##    symbols_to_clear = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'
    return ''.join([c for c in word if c not in punctuation])


def has_dashdash(word):
    return "--" in word


def extract_words(text):
##    wordslist = [cleanword(word.lower()) for word in text.split()]
    wordslist = []
    for word in text.split():
        if has_dashdash(word):
            wordslist.extend(word.split("--"))
        else:
            wordslist.append(word)
    return [cleanword(word.lower()) for word in wordslist]


def wordcount(word, wordslist):
    return wordslist.count(word)


def wordset(wordslist):
##    return list(set(wordslist))
    uniq_words = []
    for word in wordslist:
        if word not in uniq_words:
            uniq_words.append(word)
    uniq_words.sort()
    return uniq_words


def longestword(wordslist):
    longest_len = 0
    longest_word = ''
    for word in wordslist:
        length = len(word)
        if length > longest_len:
            longest_word = word
            longest_len = length
    return longest_len
