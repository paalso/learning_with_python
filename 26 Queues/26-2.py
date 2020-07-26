# Chapter 26. Queues
# http://openbookproject.net/thinkcs/python/english3e/queues.html

# Exercise 1
# ===========
# Write an implementation of the Priority Queue ADT using a linked list.
# You should keep the list sorted so that removal is a constant time operation.
# ompare the performance of this implementation with the Python list
# implementation.

import Queue

class PriorityQueue(Queue.Queue):

    def find_max(self, comparator):
        if not self.head:
            return None
        current = self.head
        max_node = current
        while current:
            if comparator(current, max_node) == 1:
                max_node = current
            current = current.next
        return max_node

    def find(self, value):  # не понадобилось
        if not self.head:
            return None
        current = self.head
        while current:
            if current.cargo == value:
                return current
            current = current.next
        return current

    def remove(self, comparator):
        max_item = self.find_max(comparator)
        if self.head == max_item:
            item_to_remove = self.head
            self.head = self.head.next
            return item_to_remove

        current = self.head
        while current.next != max_item:
            current = current.next

        item_to_remove = current.next
        current.next = item_to_remove.next
        item_to_remove.next = None
        return item_to_remove.cargo


def main():

    def comp(node1, node2):
        if node1.cargo > node2.cargo: return 1
        if node1.cargo < node2.cargo: return -1
        return 0

    q = PriorityQueue()
    q.insert(10)
    q.insert(2)
    q.insert(12)
    q.insert(12)
    q.insert(33)
    q.print()
##    print('Max: ', q.find_max(comp))
    print(q.remove(comp))
    q.print()
    print(q.remove(comp))
    q.print()
    print(q.remove(comp))
    q.print()
    print(q.remove(comp))
    q.print()
    print(q.remove(comp))
    q.print()


if __name__ == '__main__':
    main()
