'''
This exercise pertains to the so-called Birthday Paradox.
If there are 23 students in your class, what are the chances that two of you
have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays
and checking for matches. Hint: you can generate random birthdays with
the randint function in the random module.
'''

def has_duplicates(L):
    return len(L) != len(set(L))


def random_list(size, bottom, upper):
    import random
    return [random.randrange(bottom, upper) for i in range(size)]

##birthdays_list = random_list(23, 1, 366)
##print(birthdays_list)
##print(has_duplicates(birthdays_list))

same_counter = 0
counter = 10000

for i in range(counter):
    if has_duplicates(random_list(23, 1, 366)):
        same_counter += 1

THEOR_PROB = 0.507297
probability = round(same_counter / counter, 3)
print(f'Probability estimation in {counter} experiments: {probability}')
print(f'Theoretical probability : {round(THEOR_PROB, 3)}')
