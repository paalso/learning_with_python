# http://openbookproject.net/thinkcs/python/english3e/trees.html


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def get_children(self):
        return self.left, self.right


def total(tree):
    """ Sum of all the numeric cargos in the tree"""
    if tree is None:
        return 0
    value = tree.cargo if type(tree.cargo) in (int, float) else 0
    return value + total(tree.left) + total(tree.right)


def print_tree_preorder(tree):
    if tree is None:
        return
    print(tree.cargo, end=' ')
    print_tree_preorder(tree.left)
    print_tree_preorder(tree.right)


def print_tree_postorder(tree):
    if tree is None:
        return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=' ')


def print_tree_inorder(tree):
    if tree is None:
        return
    print_tree_inorder(tree.left)
    print(tree.cargo, end=' ')
    print_tree_inorder(tree.right)


# 3 * 2 + (5 + (4 - 1) * 2)
expr_tree = \
    Tree('+', Tree('*', Tree(3), Tree(2)), Tree('+', Tree(5), Tree('*', Tree('-', Tree(4), Tree(1)), Tree(2))))

# 1 + 2 * 3
expr_tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))

print()
print("Preorder printing of the tree:")
print_tree_preorder(expr_tree)

print()
print("Postorder printing of the tree")
print_tree_postorder(expr_tree)

print()
print("Inorder printing of the tree")
print_tree_inorder(expr_tree)


def print_tree_indented(tree, level=0):
    if tree is None:
        return
    print_tree_indented(tree.left, level + 1)
    print('  ' * level + str(tree.cargo))
    print_tree_indented(tree.right, level + 1)

print()
print("Indented inorder printing of the tree")
print_tree_indented(expr_tree)
