import sys
import HuffmanTree


def getPriorityList(data):
    dic = {}
    for element in data:
        if element not in dic:
            dic[element] = 1
        else:
            dic[element] += 1
    return sorted(dic.items(), key=lambda x: x[1])


def encoding(data, ht):
    ret = ""
    for x in data:
        ret = ret + ht.search(x).code
    return ret


def huffman_encoding(data = None):
    if not data:
        print("please enter something")
        return
    priority_lst = getPriorityList(data)
    ht = HuffmanTree.HuffmanTree()
    ht.add(priority_lst)
    code = encoding(data, ht)
    return code, ht


def huffman_decoding(data, ht):
    data = [int(i) for i in data]
    curr = ht.pq.head
    ret = ""
    for i in data:
        if i == 0:
            curr = curr.left
        else:
            curr = curr.right

        if curr.value:
            ret = ret + curr.value
            curr = ht.pq.head
    return ret


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
huffman_encoding(None)
# Test Case 2
huffman_encoding()
# Test Case 3
code, tree = huffman_encoding('我想测试一下中文是否可以通过')
chinese = huffman_decoding(code, tree)
print(chinese)
