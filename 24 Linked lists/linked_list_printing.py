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


node3 = Node(3, None)
node2 = Node(2, node3)
node1 = Node(1, node2)

node = Node(1, None)
empty_node = Node()

# Printing forward
print("Printing forward:")
print_list(node1)
print("empty list:")
print_list(empty_node)
print("singleton:")
print_list(node3)

# Printing backward
print()
print("Printing backward:")
print_backward(node1)
print("empty list:")
print_backward(empty_node)
print("singleton:")
print_backward(node3)

# Printing backward nicely
print("\n")
print("Printing backward nicely:")
print_backward_nicely(node1)
print("empty list:")
print_backward_nicely(empty_node)
print("singleton:")
print_backward_nicely(node3)
