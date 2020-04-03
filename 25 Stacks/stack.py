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
        if self.size > 0:
            self.size -= 1
            return self.items.pop()

    def is_empty(self):
        return self.size == 0


def eval_postfix(expr):
    import re, operator

    bin_operations = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv
    }

    token_list = re.split("([^0-9])", expr)
    expr_stack = Stack()
    print(token_list)
    for token in token_list:
        if token == '' or token == ' ':
            continue
        elif token in bin_operations:
                operand2 = expr_stack.pop()
                operand1 = expr_stack.pop()
                expr_stack.push(bin_operations[token](operand1, operand2))
        else:       # token is a number
            expr_stack.push(int(token))

    return expr_stack.pop()


def main():
    expr = '5 4 2 1 / + *'
    expr = '1 2 + 3 *'
    print(eval_postfix(expr))


if __name__ == "__main__":
    main()
