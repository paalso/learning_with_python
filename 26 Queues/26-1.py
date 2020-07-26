# Chapter 26. Queues
# http://openbookproject.net/thinkcs/python/english3e/queues.html

# Exercise 1
# ===========
# Write an implementation of the Queue ADT using a Python list. Compare
# the performance of this implementation to the ImprovedQueue for a range
# of queue lengths.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, cargo):    # O(1)
        self.items.append(cargo)

    def remove(self):   # O(n)
        return self.items.pop(0)

    def print(self):
        print(' <- '.join(map(str, self.items)) + ' <-')


def main():
    q = Queue()
    q.insert(1)
    q.print()

    q.insert(2)
    q.print()

    q.insert(3)
    q.print()

    print(q.remove())
    q.print()
    print(q.remove())
    q.print()
    print(q.remove())
    q.print()


if __name__ == '__main__':
    main()
