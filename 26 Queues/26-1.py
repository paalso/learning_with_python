# Chapter 26. Queues
# http://openbookproject.net/thinkcs/python/english3e/queues.html

# Exercise 1
# ===========
# Write an implementation of the Queue ADT using a Python list. Compare
# the performance of this implementation to the ImprovedQueue for a range
# of queue lengths.


class Queue:
    def __init__(self):
        """Initialize a new empty queue"""
        self.items = []

    def insert(self, item):
        """Add a new item to the queue"""
        self.items.append(item)

    def remove(self):
        """Remove and return an item from the queue. The item that is returned
        is the first one that was added"""
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        """Check whether the queue is empty"""
        return self.items == []

    def __str__(self):
        return "[{}]".format(", ".join(str(e) for e in self.items))


def main():
    print("Creating new Queue:")
    q = Queue()
    print(q)

    print("\nAdding new nodes (1, 2, 3) to the Queue:")
    q.insert(1)
    print(q)
    q.insert(2)
    print(q)
    q.insert(3)
    print(q)

    print("\nRemoving nodes from the Queue:")
    print("removed node: {}".format(q.remove()))
    print(q)
    print("removed node: {}".format(q.remove()))
    print(q)
    print("removed node: {}".format(q.remove()))
    print(q)
    print("removed node: {}".format(q.remove()))
    print(q)

    print("\nAdding new nodes (999, 66, 'xxx', (1, 'z')) to the Queue:")
    q.insert(999)
    q.insert(66)
    q.insert('xxx')
    q.insert((1, 'z'))
    print(q)


if __name__ == "__main__":
    main()
