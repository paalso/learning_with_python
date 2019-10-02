# Chapter 20. Dictionaries
# http://openbookproject.net/thinkcs/python/english3e/dictionaries.html

# Exercises 3, 4
# ===========
# Write a program called alice_words.py that creates a text file named
# alice_words.txt containing an alphabetical listing of all the words,
# and the number of times each occurs, in the text version of Alice’s Adventures
# in Wonderland. The first 10 lines of your
# output file should look something like this:
# Word              Count
# =======================
# a                 631
# a-piece           1
# abide             1
# ....


def text_to_words(text):
    translator = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'-!\"#$%&()*+,./:;<=>?@[]^_`{|}~\\",
        "abcdefghijklmnopqrstuvwxyz                                          ")

# Здесь попытка оставить слова, включающие в себя дефис, типа a-piece
# Но выходят баги: остаются слова с кусками переносов и какие то двойные дефисы:
# --did, a--i, again-- etc
# Нужно очисить - вручную или с помощью регулярных выражений.
# Пока остается вариант без дефисов
#   "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'!\"#$%&()*+,./:;<=>?@[]^_`{|}~\\",
#   "abcdefghijklmnopqrstuvwxyz                                         ")
    cleared_text = text.translate(translator)
    return cleared_text.split()


def get_words_in_book(filename):
    file = open(filename, 'r')
    file_content = file.read()
    file.close()
    return text_to_words(file_content)


def get_longest_word_length(dictionary):
    max_word_len = 0
    for word in dictionary.keys():
        if len(word) > max_word_len:
            max_word_len = len(word)
    return max_word_len


def get_longest_words(dictionary):
    max_word_len = max(map(lambda w: len(w), list(dictionary.keys())))
    longest_words = list(filter(lambda w: len(w) == max_word_len, \
                                            list(dictionary.keys())))
    return longest_words


all_words = get_words_in_book("alice_in_wonderland.txt")
##print(all_words[:50])

##all_words = ['and', 'alice', 'dick', 'alice']

words_frequency = {}
for word in all_words:
    words_frequency[word] = words_frequency.get(word, 0) + 1

# Sorting by frequency
# words_frequency_list = list(words_frequency.items())
# words_frequency_list.sort(reverse=True,key=lambda item: item[1])

# Sorting alphabetically
words_frequency_list = list(words_frequency.items())
words_frequency_list.sort(key=lambda item: item[0])

out_file_name = "alice_words.txt"
out_file = open(out_file_name,"w")
out_file.writelines(" Num      Word       Count\n")
out_file.writelines("==========================\n")
num = 1
for word, freq in words_frequency_list:
    out_file.write("{0:4d}  {1:15s}{2:3d}\n".format(num,word,freq))
    num += 1
out_file.close()

print("The listing of all the words was succesfully exported into:", \
                                                                out_file_name)
words_to_print = 10
print("\nFirst {0} words:".format(words_to_print))
for el in words_frequency_list[:words_to_print]:
    print(el[0])

longest_words = get_longest_words(words_frequency)
print("\nLongest words: ", ", ".join(longest_words))
print("Their length: ", len(longest_words[0]))
