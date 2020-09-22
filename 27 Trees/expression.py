# http://openbookproject.net/thinkcs/python/english3e/trees.html


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return f"{str(self.cargo)}, left: {self.left}, right: {self.right}"


def print_tree_postorder(tree):
    if tree is None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=" ")


def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.left, level + 1)
    print("{}{}".format("  " * level, tree.cargo))
    print_tree_indented(tree.right, level + 1)


def parse_expr(expression):
    import re

    def try_number(x):
        try:
            f = float(x)
            return f
        except:
            return x

    cleared = filter(lambda e: not (e == "" or e.isspace()),
                        re.split("([^0-9])", expression))
    return list(map(lambda e: try_number(e), cleared))


def tokenize(expession):
    tokens = parse_expr(expession)
    tokens.append("end")
    return tokens




def get_token(token_list, expected):
    """
    Takes a token list and an expected token as parameters.
    It compares the expected token to the first token on the list:
    if they match, it removes the token from the list and returns True;
    herwise, it returns False """
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False


def get_number(token_list):
    """
    If the next token in token_list is a number, removes it and
    returns a leaf node containing the number; otherwise, it returns None. """

    x = token_list[0]
    if type(x) in (int, float):
        del token_list[0]
        return Tree(x)


##x = get_number(token_list)
##print_tree_postorder(x)
##print(token_list)


def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_product(token_list)       # This line changed
        return Tree("*", a, b)
    return a


def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return Tree("+", a, b)
    return a


##expr = "( 3 +     7  ) *     9   "
##print(tokenize(expr))

token_list = [2, "*", 3, "*", 5 , "*", 7, "end"]
tree = get_product(token_list)
print_tree_indented(tree)

