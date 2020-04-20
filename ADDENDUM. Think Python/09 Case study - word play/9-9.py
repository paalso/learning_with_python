'''
Exercise 9.9.
“Recently I had a visit with my mom and we realized that the two digits that
make up my age when reversed resulted in her age. For example, if she’s 73,
I’m 37. We wondered how often this has happened over the years but we got
sidetracked with other topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been
reversible six times so far. I also figured out that if we’re lucky it would
happen again in a few years, and if we’re really lucky it would happen one
more time after that. In other words, it would have happened 8 times over all.
So the question is, how old am I now?”
'''

def reverse_number(n):
    return (n  % 10) * 10 + n // 10


for age_diff in range(11, 50):
    counter = 0
    magic_ages = [None]
    for my_age in range(1, 100):
        mothers_age = my_age + age_diff
        if mothers_age == reverse_number(my_age):
            counter += 1
            print(f'Child: {my_age}, mother: {mothers_age}, defference: {age_diff}')
            magic_ages.append(my_age)
    if counter == 8:
        print("Suitable age difference is {}, my age is {}, mother's age is {}"
            .format(age_diff, magic_ages[6], reverse_number(magic_ages[6])))
        print('Live long life, Mom!')
        break
