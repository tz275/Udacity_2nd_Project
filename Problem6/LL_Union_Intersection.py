class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def getAll(self):
        """
        get all value from the linked list
        Big(O) = n
        :return: list
        """
        curr = self.head
        ret = []
        while curr:
            ret.append(curr.value)
            curr = curr.next
        return ret


"""
Run Time Analysis:
Union:
    In this function we totally use 2 for loops (not nested), thus O = 2n. Moreover, it also uses getAll()
    2 times, which O = 2n. Add them up this function's O = 4n. After calculate the worst condition, O = n.
Intersection:
    In this function we also use 2 for loops and 2 times getAll() function and the loops are not nested.
    Big O of this function is n also.
"""


def union(llist_1, llist_2):
    """
    union two linked lists
    :param llist_1: linked list
    :param llist_2: linked list
    :return: set
    """
    # Your Solution Here
    ret = set()
    for element in llist_1.getAll():
        ret.add(element)
    for element in llist_2.getAll():
        ret.add(element)
    return ret


def intersection(llist_1, llist_2):
    """
    intersection two linked lists
    :param llist_1: linked list
    :param llist_2: linked list
    :return: set
    """
    have = set()
    ret = set()
    for element in llist_1.getAll():
        have.add(element)
    for element in llist_2.getAll():
        if element in have:
            ret.add(element)
    return ret


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
ll1 = LinkedList()
ll2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23] * 100
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    ll1.append(i)

for i in element_2:
    ll2.append(i)

assert union(linked_list_3, linked_list_4) == union(ll1, ll2)
assert intersection(linked_list_3, linked_list_4) == intersection(ll1, ll2)
# Test Case 2
ll1 = LinkedList()
ll2 = LinkedList()

element_1 = []
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    ll1.append(i)

for i in element_2:
    ll2.append(i)

assert list(union(ll1, ll2)) == element_2[:-1]
assert list(intersection(ll1, ll2)) == []

# Test Case 3
ll1 = LinkedList()
ll2 = LinkedList()

element_1 = [1, 2, 3, 4]
element_2 = [1, 2, 3, 4]

for i in element_1:
    ll1.append(i)

for i in element_2:
    ll2.append(i)

assert list(union(ll1, ll2)) == element_1
assert list(intersection(ll1, ll2)) == element_1
