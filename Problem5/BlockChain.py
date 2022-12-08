import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        """
        calculate the hash value for each block
        Big(O) = 1 (if all functions we used from the hashlib O = 1)
        :return: string
        """
        sha = hashlib.sha256()
        hash_str = str(str(self.previous_hash) + str(self.timestamp) + str(self.data)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
b1 = Block("12/7/2022", "1", 0)
b2 = Block("12/17/2022", "2", b1.hash)
print(b1.hash)
print(b2.previous_hash)
print(b2.hash)
print('\n')

# Test Case 2
b1 = Block("", "", 0)
b2 = Block("12/17/2022", "2", b1.hash)
print(b1.hash)
print(b2.previous_hash)
print(b2.hash)
print('\n')

# Test Case 3
b1 = Block(None, None, 0)
b2 = Block("12/17/2022", "2", b1.hash)
print(b1.hash)
print(b2.previous_hash)
print(b2.hash)
print('\n')