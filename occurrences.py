class LetterCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.counter_dict = {}

    def count_letters(self):
        # all signs
        signs = [',', '.', '!', '?', ';', ':', '-', '_', '/', '\\', '|', '@', '#', '$', '%', 
                 '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '=', '+', '"', "'"]
        
        for char in self.sentence:
            if char.isalnum() or char.isspace() or char in signs:  # Include letters, numbers, and spaces
                # if character is already in dictionary, add 1 to corresponding value
                if char.lower() in self.counter_dict:
                    self.counter_dict[char.lower()] += 1
                # if character is not in dictionary, add and set value equal to 1
                else:
                    self.counter_dict[char.lower()] = 1

        # Sort the dictionary by values
        self.counter_dict = dict(sorted(self.counter_dict.items(), key=lambda x: x[1]))

        # return dictionary of character occurrences
        return self.counter_dict
    