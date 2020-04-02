# Chapter 24. Linked lists
# http://openbookproject.net/thinkcs/python/english3e/linked_lists.html


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

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


# You might wonder why print_list and print_backward are functions and
# not methods in the Node class. The reason is that we want to use None
# to represent the empty list and it is not legal to invoke a method on None.
# This limitation makes it awkward to write list – manipulating code in a clean
# object-oriented style.

def print_backward(list):
    if list is None:
        return
    print_backward(list.next)
    print(list, end=' ')


def print_backward_nicely(list):
    print("[", end=" ")
    print_backward(list)
    print("]")


'''
Exercise 1
===========

By convention, lists are often printed in brackets with commas between
the elements, as in [1, 2, 3]. Modify print_list so that it generates
output in this format.
'''

def print_list(list):
    print('[',end='')
    node = list
    while node != None:
        print(f'{node}',end='')
        if node.next is None:
            break
        print(', ',end='')
        node = node.next
    print(']')


def find_nth(node, n):
    for i in range(n):
        if node is None:
            return None
        node = node.next
    return node


def remove_nth(node, n):
    '''
    Removes the nth node (except the 0th) in the list and returns
    a reference to the removed node
    '''
    prev_node = find_nth(node, n - 1)
    if not prev_node:
        return
    nth_node = prev_node.next
    if not nth_node:
        return
    prev_node.next = nth_node.next
    nth_node.next = None
    return nth_node


node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
node0 = Node(0, node1)


print_list(node0)
##print(find_nth(node1, 1))
print(remove_nth(node0, 1))
print_list(node0)
