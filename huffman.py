import heapq
from node import Node

class HuffmanEncoder:
    def __init__(self, sentence):
        # Initialize the HuffmanEncoder with the input sentence.
        self.sentence = sentence
        self.char_freq = {}
        self.root = None
        self.codes = {}

    def build_frequency_dict(self):
        # Build a dictionary of character frequencies in the sentence.
        for char in self.sentence:
            if char in self.char_freq:
                self.char_freq[char] += 1
            else:
                self.char_freq[char] = 1

    def build_huffman_tree(self):
        # Build the Huffman tree using the character frequencies.
        heap = [Node(char, freq) for char, freq in self.char_freq.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            new_node = Node(None, left.freq + right.freq)
            new_node.left = left
            new_node.right = right
            heapq.heappush(heap, new_node)

        self.root = heap[0]

    def build_huffman_codes(self, node, prefix=""):
        # Build Huffman codes for each character in the tree.
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = prefix
            return

        self.build_huffman_codes(node.left, prefix + "0")
        self.build_huffman_codes(node.right, prefix + "1")

    def encode_sentence(self):
        # Encode the sentence using the Huffman codes.
        encoded_sentence = "".join([self.codes[char] for char in self.sentence])
        return encoded_sentence

    def encode(self):
        # Encode the sentence using Huffman coding.
        self.build_frequency_dict()
        self.build_huffman_tree()
        self.build_huffman_codes(self.root)
        return self.encode_sentence(), self.root
