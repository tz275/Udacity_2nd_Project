import sys
import HuffmanTree


def getPriorityList(data):
    """
    calculate the frequency of each element in the data
    key = element, value = frequency and return it in the format of list of tuples after sort it
    :param data: list
    :return: list of tuples e.g.[(x1, x2), (y1, y2)]
    """
    dic = {}
    for element in data:
        if element not in dic:
            dic[element] = 1
        else:
            dic[element] += 1
    return sorted(dic.items(), key=lambda x: x[1])


def encoding(data, ht):
    """
    loop through all the element in the data and return the huffman code of the whole data
    Big(O) = n
    :param data: string
    :param ht: HuffmanTree
    :return: string
    """

    ret = ""
    for x in data:
        ret = ret + ht.search(x).code
    return ret


def huffman_encoding(data = None):
    """
    use the helper functions "getPriorityList" change the format of the input, and use this as the input of the
    "huffmantree.add", add all the element to the tree. Lastly, use the "encoding" method to get all the huffman code
    Big(O) = 3n which Big(O) = n
    :param data: string
    :return: string, HuffmanTree
    """
    if not data:
        print("please enter something")
        return
    priority_lst = getPriorityList(data)
    ht = HuffmanTree.HuffmanTree()
    ht.add(priority_lst)
    code = encoding(data, ht)
    return code, ht


def huffman_decoding(data, ht):
    """
    traverse all the code from the data and find the origin value from ht
    Big(O) = n (n is the length of the data)
    :param data: binary string
    :param ht: Huffman Tree
    :return: string
    """
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
