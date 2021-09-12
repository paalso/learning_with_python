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


def print_tree_postorder(tree):
    if tree is None:
        return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=' ')


def tokenize_expression(expression):
    import re

    def numerize_item(token):
        try:
            return int(token)
        except:
            return token

    tokens = re.split("([^0-9])", expression)
    filtered_tokens = filter(
            lambda token: token and not token.isspace(), tokens)
    numerized_tokens = list(map(numerize_item, filtered_tokens))
    numerized_tokens.append("end")
    return numerized_tokens


def get_token(tokens, expected):
    """ Compares the expected token to the first token on the tokens list:
    if they match, it removes the token from the list and returns True;
    otherwise, it returns False """
    if tokens[0] == expected:
        tokens.pop(0)
        return True
    return False


def get_number(tokens):
    """ If the next token in token_list is a number, get_number removes it and
    returns a leaf node containing the number; otherwise, it returns None """
    token = tokens[0]
    if type(token) == int:
        tree = Tree(token)
        tokens.pop(0)
        return tree

def get_product(token):
    """ Builds and returns an expression tree for products
    Assuming that get_number succeeds and returns a singleton tree, we assign
    the first operand to a. If the next character is *, we get the second
    number and build an expression tree with a, b, and the operator.
    If the next character is anything else, then we just return the leaf node
    with a """
    pass



token_list = [9, "*", 11, "end"]
tree = get_product(token_list)
print_tree_postorder(tree)  # 9 11 *


token_list = [9, "+", 11, "end"]
tree = get_product(token_list)
print_tree_postorder(tree)   # 9
9

def f():
