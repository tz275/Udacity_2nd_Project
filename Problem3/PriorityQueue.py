from Node import Node


class PriorityQueue:
    def __init__(self):
        self.head = None

    def dfs(self):
        """
        traverse all nodes in the PriorityQueue from head
        Big(O) = 0
        :return: list
        """
        ret = []
        stack = [self.head]
        while stack:
            curr = stack.pop()
            ret.append((curr.value, curr.frequency, curr.code))
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return ret

    def __str__(self):
        lst = self.dfs()
        return str(lst)

    def addOne(self, element):
        """
        add one element to the priority queue
        Big(O) = 1
        :param element: any
        :return: None
        """
        node1 = Node(element[0], element[1])
        if not self.head:
            self.head = node1
            return
        node2 = self.head
        parent_node = Node(None, node1.frequency + node2.frequency)

        # always keep node1's freq less than node2's freq
        if node1.frequency > node2.frequency:
            temp = node1
            node1 = node2
            node2 = temp

        self.head = parent_node
        self.head.left = node1
        self.head.right = node2
        return

    def addTwo(self, element1, element2):
        """
        add 2 elements to the priority queue
        Big(O) = 1
        :param element1:
        :param element2:
        :return:
        """
        node1 = Node(element1[0], element1[1])
        node2 = Node(element2[0], element2[1])
        parent_node = Node(None, node1.frequency + node2.frequency)

        # always keep node1's freq less than node2's freq
        if node1.frequency > node2.frequency:
            temp = node1
            node1 = node2
            node2 = temp

        parent_node.left = node1
        parent_node.right = node2
        if not self.head:
            self.head = parent_node
            return

        old_head = self.head
        self.head = Node(None, old_head.frequency + parent_node.frequency)
        self.head.left = old_head
        self.head.right = parent_node

        return



