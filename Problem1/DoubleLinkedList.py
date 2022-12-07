from Node import Node


class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        # only this method (O) = n
        to_print = []
        curr = self.head
        while curr:
            to_print.append(curr.value)
            curr = curr.next
        return str(to_print)

    def add(self, item):
        self.size += 1
        item = Node(item)
        if not self.head:
            self.head = item
            self.tail = item
            return item
        self.tail.next = item
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return item

    def popHead(self):
        ret = self.head
        self.head = self.head.next
        self.head.next.previous = None
        return ret.value

    def pop(self, node):
        prev = node.previous
        nxt = node.next
        if not prev:
            value = node.value
            node = nxt
            self.head = node
            node.previous = None
            return value
        prev.next = nxt
        if not nxt:
            self.tail = prev
        return node.value
