# Chapter 14. List Algorithms
# http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html

# Exercise 5
# ===========
"""
Every week a computer scientist buys four lotto tickets. She always chooses
the same prime numbers, with the hope that if she ever hits the jackpot,
she will be able to go onto TV and Facebook and tell everyone her secret.
This will suddenly create widespread public interest in prime numbers,
and will be the trigger event that ushers in a new age of enlightenment.
She represents her weekly tickets in Python as a list of lists:

my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]
Complete these exercises.

Each lotto draw takes six random balls, numbered from 1 to 49. Write a function
to return a lotto draw.

Write a function that compares a single ticket and a draw, and returns
the number of correct picks on that ticket:

test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
Write a function that takes a list of tickets and a draw, and returns
a list telling how many picks were correct on each ticket:

test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])
Write a function that takes a list of integers, and returns the number
of primes in the list:

test(primes_in([42, 4, 7, 11, 1, 13]) == 3)
Write a function to discover whether the computer scientist has missed any
prime numbers in her selection of the four tickets. Return a list of all primes
that she has missed:

test(prime_misses(my_tickets) == [3, 29, 47])
Write a function that repeatedly makes a new draw, and compares the draw to
the four tickets.

Count how many draws are needed until one of the computer scientist’s tickets
has at least 3 correct picks. Try the experiment twenty times, and average out
the number of draws needed.
How many draws are needed, on average, before she gets at least 4 picks correct?
How many draws are needed, on average, before she gets at least 5 correct?
(Hint: this might take a while. It would be nice if you could print some dots,
like a progress bar, to show when each of the 20 experiments has completed.)
Notice that we have difficulty constructing test cases here, because our random
numbers are not deterministic. Automated testing only really works if you
already know what the answer should be!
"""

import random
from testtools import *


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
        if n % k == 0:
            return False
    return True


def generate_primes(n):
    result = []
    if n < 2:
        return result
    result.append(2)
    for p in range(3, n + 1, 2):
        if is_prime(p):
            result.append(p)
    return result


def get_lotto_draw(balls = 6, max_number = 49):
    draw = []
    rnd = random.Random()
    for i in range(balls):
        while True:
            r = rnd.randint(1, max_number)
            if r not in draw: break
        draw.append(r)

    return draw


def lotto_match(draw1, draw2):
    return len(set(draw1) & set(draw2))


def lotto_matches(draw, tickets):
    correct_picks = []
    for d in tickets:
        correct_picks.append(lotto_match(d, draw))
    return correct_picks


def primes_in(lst):
    primes = 0
    for el in lst:
        if is_prime(el): primes += 1
    return primes


def prime_misses(tickets, max_number = 49):
    all_numbers = generate_primes(max_number)
    selected = set()
    for ticket in tickets:
        selected |= set(ticket)
    return sorted(set(all_numbers) - selected)


MY_TICKETS = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

EXPERIMENTS = 20
MATCHES = 6

total_draw_number = 0
for i in range(EXPERIMENTS):
    draw_number = 0
    while True:
        draw = get_lotto_draw()
        draw_number += 1
        total_draw_number += 1

        flag = False
        for matches in range(MATCHES, 7):
            if matches in lotto_matches(draw, MY_TICKETS):
                flag = True
                break

        if flag: break

    print("Experiment # {0:2d}, number of draws: {1:4d}, draw: {2}".
        format(i + 1, draw_number, draw))

average = round(total_draw_number / EXPERIMENTS)
print("Needed {0} draws on average before got {1} correct picks".
    format(average, MATCHES))


