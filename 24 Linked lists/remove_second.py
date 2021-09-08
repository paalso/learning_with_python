class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


def print_list(node):
    print("[", end="")
    while node.cargo:
        print(node, end="")
        if (next_node := node.next):
            print(", ", end="")
        node = next_node
    print("]")


# What happens if you invoke this method and pass a list with only one
# element (a singleton)? What happens if you pass the empty list as
# an argument? Is there a precondition for this method? If so, fix
# the method to handle a violation of the precondition in a reasonable way

def remove_second(node):
    if not node is None:
        return
    second = node.next
    node.next = second.next
    second.next = None
    return node


node1 = Node()
node3 = Node(3, None)
node2 = Node(2, node3)
node1 = Node(1, node2)
node = node1

print("Original list:")
print_list(node)
##print("Remove the second item:")
##node = remove_second(node)
##print_list(node)
##
##node = Node()
##print("Original list:")
##print_list(node)
##print("Remove the second item:")
##node = remove_second(node)
##print_list(node)


##def print_list(node):
##    while node is not None:
##        print(node, end=" ")
##        node = node.next
##    print()
##
##node = Node()
##print_list(node)