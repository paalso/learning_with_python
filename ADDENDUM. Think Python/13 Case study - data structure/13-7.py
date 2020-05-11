'''
Exercise 13.7.
Write a program that use this algorithm:

1. Use keys to get a list of the words in the book.
2. Build a list that contains the cumulative sum of the word frequencies
(see Exercise 10.2). The last item in this list is the total number of words
in the book, n.
3. Choose a random number from 1 to n. Use a bisection search
(See Exercise 10.10) to find the index where the random number would be
inserted in the cumulative sum.
4. Use the index to find the corresponding word in the word list.

to choose a random word
from the book. Solution: http: //thinkpython2.com/code/analyze_book3.py
'''

def histogram(text):
    import collections
    return dict(collections.Counter(text))


def histo_probabilities(histogram):
    values_number = sum(histogram.values())
    probabilities = { key : histogram[key] / values_number
        for key in histogram }
    return probabilities


def invert_dict(d):
    def new_list(): return []

    from collections import defaultdict
    reversed_d = defaultdict(new_list)

    for key, value in d.items():
        reversed_d[value].append(key)
    return dict(reversed_d)


import itertools, bisect, random
class ChooseFromHist:
    def __init__(self, histogram):
        self.accumulated_values = list(itertools.accumulate(histogram.values()))
        self.reversed_pairs = sorted(
            zip(self.accumulated_values, histogram.keys()))
        self.size = self.accumulated_values[-1]

    def choose(self):
        random_value = random.randrange(self.size)
        index = bisect.bisect_right(self.accumulated_values, random_value)
        return self.reversed_pairs[index][1]


def main():
    s = 'aaabbcdddddddd'
    s = 'abc'
    hist = histogram(s)

    acc_hist = ChooseFromHist(hist)
    print(histo_probabilities(hist))

    print(acc_hist.choose())

    hist1 = dict()
    for i in range(100000):
        c = acc_hist.choose()
        hist1[c] = hist1.get(c, 0) + 1

    print(histo_probabilities(hist1))

if __name__ == '__main__':
    main()
