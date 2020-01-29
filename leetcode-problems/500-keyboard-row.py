"""
https://leetcode.com/problems/keyboard-row/
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        if len(words) == 0:
            return None
        
        row1 ="qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        
        result = []
        for word in words:
            row1_counter = 0
            row2_counter = 0
            row3_counter = 0
            
            lowered_word = word.lower()
            i = 0
            while i < len(word):
                if lowered_word[i] in row1:
                    row1_counter += 1
                if lowered_word[i] in row2:
                    row2_counter += 1
                if lowered_word[i] in row3:
                    row3_counter += 1
                i += 1
            
            if row1_counter == len(word) or row2_counter == len(word) or row3_counter == len(word):
                result.append(word)
        return result

# revisit this solution - what's going on here?
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        
        for word in words:
            #set keyboard reference row based on first letter of word
            ref = [row for row in rows if word[0].lower() in row]
            #if there aren't any characters not in reference row, add word to result
            if len([char for char in word if char.lower() not in ref[0]]) == 0:
                result.append(word)
        
        return result
        