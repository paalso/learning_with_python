class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


def print_list(node):
    print("[", end="")
    while node:
        end_ = ", " if (next_ := node.next) else ""
        print(node, end=end_)
        node = next_
    print("]")


def print_backward(node):
    if node is None:
        return
    head, tail = node, node.next
    print_backward(tail)
    print(head, end = " ")


def print_backward_nicely(node):
    print("[ ", end="")
    print_backward(node)
    print("]", end="\n")


# What happens if you invoke this method and pass a list with only one
# element (a singleton)? What happens if you pass the empty list as
# an argument? Is there a precondition for this method? If so, fix
# the method to handle a violation of the precondition in a reasonable way
def remove_second(node):
    if list is None or node.next is None:
        return
    second = node.next
    node.next = second.next
    second.next = None
    return second


node3 = Node(3, None)
node2 = Node(2, node3)
node1 = Node(1, node2)

print()
node = node1
print("Removing the second node in a long list")
print("----------------------------------------")
print("Original list:")
print_list(node)
removed_node = remove_second(node1)
print("List with removed 2nd node:")
print_list(node)
print("Removed node:")
print(removed_node)

print()
node = node1
print("Removing the second node in a 2-nodes list")
print("--------------------------------------------")
print("Original list:")
print_list(node)
removed_node = remove_second(node)
print("List with removed 2nd node:")
print_list(node)
print("Removed node:")
print(removed_node)

print()
node = node1
print("Removing the second node in a singleton list")
print("---------------------------------------------")
print("Original list:")
print_list(node)
removed_node = remove_second(node)
print("List with removed 2nd node:")
print_list(node)
print("Removed node:")
print(removed_node)

print()
node = Node()
print("Removing the second node in an empty list")
print("------------------------------------------")
print("Original list:")
print_list(node)
removed_node = remove_second(node)
print("List with removed 2nd node:")
print_list(node)
print("Removed node:")
print(removed_node)
