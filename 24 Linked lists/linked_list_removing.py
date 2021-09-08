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


def find_nth(node, pos):
    """
    Finds node in position pos in list node
    """
    if pos < 0:
        raise IndexError("IndexError: list index({}) out of range".format(pos))
    i = 0
    while node:
        if i == pos:
            return node
        node = node.next
        i += 1
    raise IndexError("IndexError: list index({}) out of range".format(pos))


def remove_nth(node, pos):
    """
    Removes node in position pos in list node
    """
    if pos <= 0:
        raise IndexError("IndexError: list index({}) out of range".format(pos))

    try:
        prev_node = find_nth(node, pos - 1)
        pos_node = prev_node.next
        prev_node.next = pos_node.next
        pos_node.next = None
        return pos_node
    except:
        raise IndexError("IndexError: list index({}) out of range".format(pos))


node5 = Node(5, None)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
node = node1


# Tests of find_nth for a long list
print(find_nth(node, 0))
print(find_nth(node, 1))
print(find_nth(node, 2))

assert find_nth(node, 0) == node1
assert find_nth(node, 1) == node2
assert find_nth(node, 4) == node5

try:
    find_nth(node, -1)
except IndexError as e:
    print(e)
try:
    find_nth(node, 5)
except IndexError as e:
    print(e)

# Tests of find_nth for a singleton list
node = node5
assert find_nth(node, 0) == node5
try:
    find_nth(node, -1)
except IndexError as e:
    print(e)
try:
    find_nth(node, 1)
except IndexError as e:
    print(e)

# Tests of find_nth for an empty list
node = Node()
try:
    assert find_nth(node, 0) == node
except IndexError as e:
    print(e)
try:
    find_nth(node, 1)
except IndexError as e:
    print(e)

print()
# Tests of remove_nth for a long lins
node = node1
pos = 2
print("Removing node {} in a long list".format(pos))
print("--------------------------------")
print("Original list:")
print_list(node)
print("Position to remove ({}) node:".format(pos))
print(find_nth(node, pos))
removed_node = remove_nth(node, pos)
print("List with removed node {}:".format(pos))
print_list(node)
print("Removed node:")
print(removed_node)

# Tests of remove_nth for a long lins
print()
node = node1
pos = 1
print("Removing node {} in a long list".format(pos))
print("--------------------------------")
print("Original list:")
print_list(node)
print("Position to remove ({}) node:".format(pos))
print(find_nth(node, pos))
removed_node = remove_nth(node, pos)
print("List with removed node {}:".format(pos))
print_list(node)
print("Removed node:")
print(removed_node)


# Test of remove_nth for the first node of a long list

node3 = Node(3, None)
node2 = Node(2, node3)
node1 = Node(1, node2)
node = node1
pos = 0
print("Removing node No {} in a long list".format(pos))
print("--------------------------------")
print("Original list:")
print_list(node)
print("Position to remove ({}) node:".format(pos))
print(find_nth(node, pos))
try:
    removed_node = remove_nth(node, pos)
    print("List with removed node {}:".format(pos))
    print_list(node)
    print("Removed node:")
    print(removed_node)
except IndexError as e:
    print(e)
    print("Impossible to remove node No {} in the list".format(pos))
