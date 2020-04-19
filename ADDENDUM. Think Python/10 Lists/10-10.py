'''
Exercise 10.9. Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?
'''

def has_duplicates(L):
    return len(L) != len(set(L))


def random_list(size, bottom, upper):
    import random
    return [random.randint(bottom, upper) for i in range(size)]

##birthdays_list = random_list(23, 1, 365)
##print(birthdays_list)
##print(has_duplicates(birthdays_list))

same_counter = 0
counter = 10000

for i in range(counter):
    if has_duplicates(random_list(23, 1, 366)):
        same_counter += 1

THEOR_PROB = 0.507297
probability = round(same_counter / counter, 3)
print(f'Probability estimation in {counter} simulations: {probability}')
print(f'Theoretical probability : {round(THEOR_PROB, 3)}')
