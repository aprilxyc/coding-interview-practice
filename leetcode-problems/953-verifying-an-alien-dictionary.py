class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # O(26) + O(N + M )
        
        if len(words) == 0:
            return None
        
        if len(words) == 1:
            return True
        
        
        alphabet_index = {}
        
        # create the dictioneary that maps the alphabet to its corresponding indices
        for index, letter in enumerate(order):
            alphabet_index[letter] = index
        
        new_words = []
        for word in words:
            new = []
            for letter in word:
                new.append(alphabet_index[letter])
            new_words.append(new)
        
        # go through and compare them
        for i in range(0, len(words) - 1):
            if new_words[i] > new_words[i + 1]:
                return False
        return True

"""





"""
