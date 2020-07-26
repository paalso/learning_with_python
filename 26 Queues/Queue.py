# Chapter 26. Queues
# http://openbookproject.net/thinkcs/python/english3e/queues.html


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class Queue:
    def __init__(self):
        '''Initialize a new empty queue'''
        self.length = 0
        self.head = None

    def is_empty(self):
        '''Check whether the queue is empty'''
        return self.length == 0

    def insert(self, cargo):    # O(n)
        '''Add a new item to the queue'''
        if not self.head:   # If list is empty the new node goes first else
            self.head = Node(cargo)
        else:
            current = self.head
            while current.next:             # Find the last node in the list
                current = current.next
            current.next = Node(cargo)      # Append the new node
        self.length += 1

    def remove(self):       # O(1)
        '''Remove and return an item from the queue. The item that is returned
        is the first one that was added'''
        current = self.head
        if self.length:
            self.head = current.next
            self.length -= 1
        return current

    def print(self):
        current = self.head
        if not self.head:
            print('<empty>')
            return
        while current:
            print('{} <- '.format(current.cargo), end='')
            current = current.next
        print()
##        print(None)

    def remove(self):
        '''Remove and return an item from the queue. The item that is returned
        is the first one that was added'''
        current = self.head
        if self.length:
            self.head = current.next
            self.length -= 1
        return current.cargo


class ImprovedQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.last = None

    def insert(self, cargo):
        '''Add a new item to the queue'''
        node = Node(cargo)
        if not self.head:   # If list is empty the new node goes first else
            self.head = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        '''Remove and return an item from the queue. The item that is returned
        is the first one that was added'''
        if self.length:
            current = self.head
            self.head = current.next
            self.length -= 1
            if self.length == 0:
                self.last = None
            return current.cargo


def main():
    q = ImprovedQueue()
    q.insert(1)
    q.print()

    q.insert(2)
    q.print()

    q.insert(3)
    q.print()
    print('Head: {}, Last: {}'.format(q.head, q.last))

    print(q.remove())
    q.print()
    print('Head: {}, Last: {}'.format(q.head, q.last))

    print(q.remove())
    q.print()
    print('Head: {}, Last: {}'.format(q.head, q.last))

    print(q.remove())
    q.print()
    print('Head: {}, Last: {}'.format(q.head, q.last))

    print(q.remove())
    q.print()
    print('Head: {}, Last: {}'.format(q.head, q.last))

    print(q.remove())
    q.print()
    print('Head: {}, Last: {}'.format(q.head, q.last))


if __name__ == '__main__':
    main()
