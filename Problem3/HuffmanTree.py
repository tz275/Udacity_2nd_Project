from PriorityQueue import PriorityQueue


class HuffmanTree:
    def __init__(self):
        self.pq = PriorityQueue()

    def add_(self, lst):
        if not lst:
            return
        this = lst.pop(0)
        if not lst or max([i[1] for i in lst]) > self.pq.head.frequency:
            self.pq.addOne(this)
        else:
            nxt = lst.pop(0)
            self.pq.addTwo(this, nxt)
        self.add_(lst)

    def add(self, lst):
        if len(lst) == 1:
            self.pq.addOne()
            return
        temp1 = lst.pop(0)
        temp2 = lst.pop(0)
        self.pq.addTwo(temp1, temp2)
        self.add_(lst)
        HuffmanTree.codeAll(self.pq.head, '')

    def search(self, value):
        stack = [self.pq.head]
        while stack:
            curr = stack.pop()
            if curr.value == value:
                return curr
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        else:
            raise ValueError("change a search number")

    @staticmethod
    def codeAll(curr, code):
        if not curr:
            return
        curr.code = code
        HuffmanTree.codeAll(curr.left, curr.code + str(0))
        HuffmanTree.codeAll(curr.right, curr.code + str(1))