# http://openbookproject.net/thinkcs/python/english3e/trees.html


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return f"{str(self.cargo)}, left: {self.left}, right: {self.right}"


def total(tree):
    """ Sum of all the numeric cargos in the tree"""
    if tree is None: return 0
    cargo = float(tree.cargo) if type(tree.cargo) in (int, float) else 0
    return cargo + total(tree.left) + total(tree.right)


def print_tree(tree):
    if tree is None: return
    print(tree.cargo, end=" ")
    print_tree(tree.left)
    print_tree(tree.right)


def print_tree_postorder(tree):
    if tree is None: return
    print_tree(tree.left)
    print_tree(tree.right)
    print(tree.cargo, end=" ")


def print_tree_inorder(tree):
    if tree is None: return
    print_tree(tree.left)
    print(tree.cargo, end=" ")
    print_tree(tree.right)


def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.left, level + 1)
    print("{}{}".format("  " * level, tree.cargo))
    print_tree_indented(tree.right, level + 1)


tree = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))
print_tree(tree)    # + 1 * 2 3
print()
print_tree_postorder(tree)  # 1 2 3 * +
print()
print_tree_inorder(tree)  # 1 + 2 * 3
print()
print_tree_indented(tree)
"""
    3
  *
    2
+
  1
"""