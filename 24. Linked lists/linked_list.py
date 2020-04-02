# Chapter 24. Linked lists
# http://openbookproject.net/thinkcs/python/english3e/linked_lists.html


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")

    def print_list(self):
    # doesn't work with emty lists i.e self is None
        print('[',end='')
        node = self
        while node != None:
            print(f'{node}',end='')
            if node.next is None:
                break
            print(', ',end='')
            node = node.next
        print(']')


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_list(self):
        if self.head is not None:
            self.head.print_list()
        else:
            print('[]')

    def print_backward(self):
        if self.head is not None:
            print("[", end=" ")
            self.head.print_backward()

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1


llist = LinkedList()
llist.print_list()

llist.add_first(0)
llist.print_list()

llist.print_list()