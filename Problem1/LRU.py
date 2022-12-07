import DoubleLinkedList


class LRU(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.ll = DoubleLinkedList.DoubleLinkedList()
        self.map = {}
        self.capacity = capacity

    def get(self, key):
        if key not in self.map.keys():
            return -1
        node = self.map[key]
        self.ll.pop(node)
        del self.map[key]
        self.set(key, node.value)
        return node.value

    def remove(self):
        to_remove = self.ll.popHead()
        del self.map[to_remove]

    def put_(self, key, value):
        node = self.ll.add(value)
        self.map[key] = node

    def set(self, key=None, value=None):
        if not key:
            raise TypeError("Plz keep input not None")
        if len(self.map) < self.capacity:
            self.put_(key, value)
        else:
            self.remove()
            self.put_(key, value)



our_cache = LRU(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
our_cache.set(9, 999999)
assert our_cache.get(9) == 999999
print(our_cache.ll)
print(our_cache.map)

# Test Case 2
try:
    our_cache.set()
except:
    print("test pass if set empty")
# Test Case 3
try:
    our_cache.set(None, None)
except:
    print("test pass if set None")