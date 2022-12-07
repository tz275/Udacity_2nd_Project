import HuffmanTree
import Main


if __name__ == "__main__":
    # Huffman Tree test
    ht = HuffmanTree.HuffmanTree()
    to_add = [('d', 2), ('b', 3), ('e', 6), ('a', 7), ('c', 7)]
    ht.add(to_add)
    print(ht.pq)
    # huffman_encoding test
    code, ht = Main.huffman_encoding('AAAAAAABBBCCCCCCCDDEEEEEE')
    print(code)
    print(ht.pq)

    # huffman_encoding test
    decode = Main.huffman_decoding(code, ht)
    print(decode)
    assert 'AAAAAAABBBCCCCCCCDDEEEEEE' == decode
