## Chapter 8. Strings
## http://openbookproject.net/thinkcs/python/english3e/strings.html


## Exercise 5
## ===========

# Assign to a variable in your program a triple-quoted string that contains
# your favourite paragraph of text — perhaps a poem, a speech, instructions
# to bake a cake, some inspirational verses, etc.
# Write a function which removes all punctuation from the string,
# breaks the string into a list of words, and counts the number of words in
# your text that contain the letter “e”. Your program should print an analysis
# of the text like this:
# "Your text contains 243 words, of which 109 (44.8%) contain an "e"."

import string

def count_words(s):
    str_sans_punctuation = ''
    for c in s:
        if not c in string.punctuation:
            str_sans_punctuation += c
    return len(str_sans_punctuation.split())

def count_words_with_substr(s, substr):
    counter = 0
    str_sans_punctuation = ''
    for c in s:
        if not c in string.punctuation:
            str_sans_punctuation += c
    for word in str_sans_punctuation.split():
        if substr in word:
            counter += 1
    return counter


s = '''To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;..'''

sub = "in"

total_words = count_words(s)
filteed_words = count_words_with_substr(s, sub)

output = \
"Your text contains {0} words, of which {1} ({2:.1f}%) \
contain substring '{3}'."\
.format(total_words, filteed_words, total_words / filteed_words, sub)

print(output)
