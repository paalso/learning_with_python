'''
Exercise 17.2. This exercise is a cautionary tale about one of the most common,
and difficult to find, errors in Python. Write a definition for a class named
Kangaroo with the following methods:
1. An __init__ method that initializes an attribute named pouch_contents
to an empty list.
2. A method named put_in_pouch that takes an object of any type and adds it to
pouch_contents.
3. A __str__ method that returns a string representation of the Kangaroo object
and the contents of the pouch.

Test your code by creating two Kangaroo objects, assigning them to variables
named kanga and roo, and then adding roo to the contents of kanga’s pouch.
Download http://thinkpython2.com/code/BadKangaroo.py
It contains a solution to the previous problem with one big, nasty bug.
Find and fix the bug.
If you get stuck, you can download
http://thinkpython2.com/code/GoodKangaroo.py
'''

class Kangaroo:

    def __init__(self, name, contents=[]):
        self.name = name
        self.pouch_contents = contents[:]

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        return '[{}]' \
            .format(self.name +
            ', contents: (' + ', '.join(map(str, self.pouch_contents)) + ')')


roo = Kangaroo('Roo')
roo.put_in_pouch('toy')
roo.put_in_pouch('candy')
print(roo)

kanga = Kangaroo('Kanga')
kanga.put_in_pouch('rabbit')
kanga.put_in_pouch('handkerchief')
kanga.put_in_pouch(roo)
print(kanga)
