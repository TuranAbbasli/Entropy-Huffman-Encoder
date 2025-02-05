from occurrences import LetterCounter
from entropy import Entropy
from huffman import HuffmanEncoder

# sentences
sentence_1 = 'peter piper picked a peck of pickled peppers'
sentence_2 = 'she sells seashells by the seashore'

# Get the dictionary of letter occurrences
count_1 = LetterCounter(sentence_1).count_letters()
count_2 = LetterCounter(sentence_2).count_letters()

print(f'\nOccurences of strings in sentence 1:\n{count_1}')
print(f'\nOccurences of strings in sentence 2:\n{count_2}')

# Get entropy of each element by dictionary of their occurrences
entropy_strings_1 = Entropy(count_1).entropy_of_string()
entropy_strings_2 = Entropy(count_2).entropy_of_string()

print(f'\nEntropy of each string in sentence 1:\n{entropy_strings_1}')
print(f'\nEntropy of each string in sentence 2:\n{entropy_strings_2}')

# Get total entropy by dictionary of occurrences of elements in them
entropy_sentence_1 = Entropy(count_1).entropy_of_sentence()
entropy_sentence_2 = Entropy(count_2).entropy_of_sentence()

print(f'\nTotal entropy in sentence 1:\n{entropy_sentence_1}')
print(f'\nTotal entropy in sentence 2:\n{entropy_sentence_2}')

# Create HuffmanEncoder instances
encoder_1 = HuffmanEncoder(sentence_1)
encoder_2 = HuffmanEncoder(sentence_2)

# Encode the sentences using Huffman coding
encoded_sentence_1, root_1 = encoder_1.encode()
encoded_sentence_2, root_2 = encoder_2.encode()

print(f'\nEncoded sentence 1:\n{encoded_sentence_1}')
print(f'\nEncoded sentence 2:\n{encoded_sentence_2}')
