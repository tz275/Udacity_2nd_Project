from Node import Node


class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        """
        using while loop to traverse all the nodes
        Big(0) = n
        :return: List
        """
        # only this method (O) = n
        to_print = []
        curr = self.head
        while curr:
            to_print.append(curr.value)
            curr = curr.next
        return str(to_print)

    def add(self, item):
        """
        take a value as an item and store this item into the Node.value attribute
        and link this node to the tail of the doubly-linked-list
        Big(O) = 1
        :param item: any
        :return: any
        """
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
        """
        delete the head of the doubly-linked-list and return the value of this head
        Big(O) = 1
        :return: any
        """
        ret = self.head
        self.head = self.head.next
        self.head.next.previous = None
        return ret.value

    def pop(self, node):
        """
        remove the node from the doubly-linked-list
        Big(O) = 1 (because the input "node" is a pointer directly to its position on the linked list,
        so we don't need to traverse the linked list to find the right node)
        :param node: Node
        :return: any
        """
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
