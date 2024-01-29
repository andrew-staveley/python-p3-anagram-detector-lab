# your code goes here!
class Anagram:
    def __init__(self, origin):
        self.origin = origin
        print(f"Anagram Detector Initialized with {origin}")
    def match(self, word_list):
        final_word = []
        self.word_list = word_list
        origin_separate = list(self.origin)
        for word in word_list:
            if sorted(list(word)) == sorted(origin_separate):
                final_word.append(word)
            else:
                pass
        return final_word