class Solution:
    def uniqueMorseRepresentations(self, words):
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        final_trans = {"".join(alphabet[ord(letter) - ord('a')] for letter in word) for word in words}
        print(final_trans)
        return final_trans
