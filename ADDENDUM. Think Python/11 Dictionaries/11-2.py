'''
Exercise 11.2. Read the documentation of the dictionary method setdefault and
use it to write a more concise version of invert_dict.
Solution: http://thinkpython2.com/code/invert_dict.py
'''


def invert_dict_old(d):
    reversed_d = {}
    for key, value in d.items():
        if value in reversed_d:
            reversed_d[value].append(key)
        else:
            reversed_d[value] = [key]
    return reversed_d

'''
def invert_dict(d):
    reversed_d = {}
    for key, value in d.items():
        reversed_d.setdefault(value, []).append(key)
    return reversed_d
'''

def invert_dict(d):
    def new_list(): return []

    from collections import defaultdict
    reversed_d = defaultdict(new_list)

    for key, value in d.items():
        reversed_d[value].append(key)
    return dict(reversed_d)


def main():
    d = {
        'a': 'B',
        'b': 'X',
        'c': 'B',
        'd': 'A',
        'e': 'B',
        'f': 'X',
        'g': 'C'
    }

    print(invert_dict_old(d))
    print(invert_dict_old({}))

    print(invert_dict(d))
    print(invert_dict({}))


if __name__ == '__main__':
    main()
