class Node():
    def __init__(self, value, freq):
        self.value = value
        self.frequency = freq
        self.left = None
        self.right = None
        self.code = None

    def __str__(self):
        return str([self.value, self.frequency, self.code])