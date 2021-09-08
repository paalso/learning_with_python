# Chapter 26. Queues
# http://openbookproject.net/thinkcs/python/english3e/queues.html


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class ImprovedQueue:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    def remove(self):
        if not self.is_empty():
            self.size -= 1
            cargo = self.head.cargo
            # * чтобы отцепить ссылку next удаляемого node от queue - нужно ли?
            current_head = self.head    # *
            self.head = self.head.next
            current_head.next = None    # *
            if self.is_empty():
                self.tail = None

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        tokens = []
        current = self.head
        while current:
            tokens.append(str(current))
            current = current.next
        return "[{}]".format(", ".join(tokens))

    def print_info(self):
        print("queue: {}, head: {}, tail: {}, len: {}"
            .format(self, self.head, self.tail, self.size))


def main():

    print("Creating new Queue:")
    q = ImprovedQueue()
    q.print_info()

    print("\nAdding new nodes (1, 2, 3) to the Queue:")
    q.insert(1)
    q.print_info()
    q.insert(2)
    q.print_info()
    q.insert(3)
    q.print_info()

    print("\nRemoving nodes from the Queue:")
    print("removed node: {}".format(q.remove()))
    q.print_info()
    print("removed node: {}".format(q.remove()))
    q.print_info()
    print("removed node: {}".format(q.remove()))
    q.print_info()
    print("removed node: {}".format(q.remove()))
    q.print_info()

    print("\nAdding new nodes (999, 66, 'xxx', (1, 'z')) to the Queue:")
    q.insert(999)
    q.insert(66)
    q.insert('xxx')
    q.insert((1, 'z'))
    q.print_info()


if __name__ == "__main__":
    main()
