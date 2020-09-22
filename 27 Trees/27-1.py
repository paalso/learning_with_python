# Chapter 27. Trees
# http://openbookproject.net/thinkcs/python/english3e/trees.html

# Exercise 1
# ===========
# Modify print_tree_inorder so that it puts parentheses around every operator
# and pair of operands. Is the output correct and unambiguous?
# Are the parentheses always necessary?


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def print_tree_inorder(tree):
    OPERATORS = ["*", "+", "-", "/", "%"]
    MULT_OPERATORS = ["*", "/", "%"]
    ADD_OPERATORS = ["+", "-"]
    FORMAT = "({})"
    if tree is None: return
    if tree.cargo in ADD_OPERATORS:
        print("(", end=" ")
        print_tree_inorder(tree.left)
        print(tree.cargo, end=" ")
        print_tree_inorder(tree.right)
        print(")", end=" ")
    elif tree.cargo in MULT_OPERATORS:
        print_tree_inorder(tree.left)
        print(tree.cargo, end=" ")
        print_tree_inorder(tree.right)
    else:
        print(tree.cargo, end=" ")



t1 = Tree("*", Tree("+", Tree(2), Tree(3)), Tree("-", Tree(7), Tree(3)))
t2 = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))
t = Tree ("/", t1, t2)
print_tree_inorder(t)
