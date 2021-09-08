# Chapter 26. Queues
# http://openbookproject.net/thinkcs/python/english3e/queues.html


class PriorityQueue:
    def __init__(self):
        """Initialize a new empty queue"""
        self.items = []

    def insert(self, item):
        """Add a new item to the queue"""
        self.items.append(item)

    def remove(self):
        """Remove and return an item from the queue. The item that is returned
        is the first one that was added"""
        if self.is_empty():
            return
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        return self.items.pop(maxi)

    def is_empty(self):
        """Check whether the queue is empty"""
        return self.items == []

    def __str__(self):
        return "[{}]".format("; ".join(str(e) for e in self.items))


def main():
    print("Creating Priority Queue:")
    q = PriorityQueue()
    print(q)
    print("\nFilling of the Queue:")
    for num in [11, 12, 14, 13]:
        q.insert(num)
    print(q)
    print("\nRemoving items from the Queue one by one:")
    q.remove()
    print(q)
    q.remove()
    print(q)
    q.remove()
    print(q)
    q.remove()
    print(q)
    q.remove()
    print(q)


if __name__ == "__main__":
    main()
