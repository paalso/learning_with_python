# http://openbookproject.net/thinkcs/python/english3e/trees.html


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return f"{str(self.cargo)}, left: {self.left}, right: {self.right}"
