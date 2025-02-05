# Entropy-Huffman-Encoder
A Python implementation of Huffman encoding and entropy calculation for text compression, including character frequency analysis and entropy measurement.

## Features
- Calculate character frequencies in a sentence.
- Compute entropy of each character in the sentence.
- Calculate the total entropy of a sentence.
- Implement Huffman encoding to compress the sentence based on character frequencies.

## Files
- `entropy.py`: Contains the `Entropy` class for calculating entropy of characters and sentences.
- `huffman.py`: Implements the `HuffmanEncoder` class for building Huffman trees and encoding sentences.
- `node.py`: Contains the `Node` class, representing nodes in the Huffman tree.
- `occurences.py`: Implements the `LetterCounter` class for counting character frequencies in a sentence.
- `main.py`: The main file that ties together the functionality of the other files, processes the input sentences, and displays the results.
