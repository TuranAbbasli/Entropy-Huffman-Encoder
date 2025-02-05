import numpy as np

class Entropy:

    def __init__(self, dictionary):
        self.counts = dictionary
        self.entropy_string = {}
        self.entropy_sentence = 0

    # function to get dictionary containing entropy of each element in the sentence
    def entropy_of_string(self):
        length = sum(self.counts.values())
        
        for key, value in self.counts.items():
            probobilty = value / length
            self.entropy_string[key] = -probobilty * np.log2(probobilty)  # entropy

        return self.entropy_string
    
    # function to get entropy of whole sentence
    def entropy_of_sentence(self):
        length = sum(self.counts.values())

        for value in self.counts.values():
            probobilty = value / length
            self.entropy_sentence += -probobilty * np.log2(probobilty)   # entropy

        return self.entropy_sentence
