# Chapter 26. Queues
# http://openbookproject.net/thinkcs/python/english3e/queues.html


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class Queue:
    def __init__(self):
        """Initialize a new empty queue"""
        self.head = None
        self.size = 0

    def insert(self, cargo):
        """Add a new item to the queue"""
        node = Node(cargo)
        if self.is_empty():     # If list is empty the new node goes first else
            self.head = node
        else:
            current = self.head
            while current.next:         # Find the last node in the list
                current = current.next
            current.next = node         # Append the new node
        self.size += 1

    def remove(self):
        """Remove and return an item from the queue. The item that is returned
        is the first one that was added"""
        if not self.is_empty():
            self.size -= 1
            cargo = self.head.cargo
            # * чтобы отцепить ссылку next удаляемого node от queue - нужно ли?
            current_head = self.head    # *
            self.head = self.head.next
            current_head.next = None    # *
            return cargo

    def is_empty(self):
        """Check whether the queue is empty"""
        return self.size == 0

    def __str__(self):
        tokens = []
        current = self.head
        while current:
            tokens.append(str(current))
            current = current.next
        return "[{}]".format(", ".join(tokens))

    def print_info(self):
        print("queue: {}, head: {}, len: {}"
            .format(self, self.head, self.size))

def main():
    print("Creating new Queue:")
    q = Queue()
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
