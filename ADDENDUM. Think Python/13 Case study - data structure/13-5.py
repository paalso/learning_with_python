'''
Exercise 13.5. Write a function named choose_from_hist that takes a histogram
as defined in Section 11.2 and returns a random value from the histogram,
chosen with probability in proportion to frequency.
For example, for this histogram:
>>> t = ['a', 'a', 'b']
>>> hist = histogram(t) # {'a': 2, 'b': 1}
your function should return 'a' with probability 2/3 and
'b' with probability 1/3.
'''

def histogram(text):
    import collections
    return dict(collections.Counter(text))


def histo_probabilities(histogram):
    values_number = sum(histogram.values())
    probabilities = { key : histogram[key] / values_number
        for key in histogram }
    return probabilities


def choose_from_hist(histogram):
    import random

    start_num = 0
    partition = dict()
    for key in histogram:
        end_num = start_num + histogram[key]
        segment = start_num, end_num
        partition[key] = segment
        start_num = end_num

    random_num = random.randrange(sum(histogram.values()))
    for key, segment in partition.items():
        start, end = segment
        if start <= random_num < end:
            return key


def main():
    s = 'abracadabra'
    d = histogram(s)
    print(d)
    print(histo_probabilities(d))
    print(choose_from_hist(d))

    d1 = dict()
    for i in range(10000):
        c = choose_from_hist(d)
        d1[c] = d1.get(c, 0) + 1

    print(histo_probabilities(d1))


if __name__ == '__main__':
    main()
