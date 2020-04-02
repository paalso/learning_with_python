# Chapter 25. Stacks
# http://openbookproject.net/thinkcs/python/english3e/stacks.html

class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def __str__(self):
        return str(self.items)


    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        if self.size > 0: self.size -= 1
        return self.items.pop()

    def is_empty(self):
        return self.size == 0


def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)


def main():
    pass

if __name__ == "__main__":
    main()




