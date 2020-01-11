class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        my_values = {}
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        # maps morse code to the letter
        letter_morse_dict = {}
        num = 0
        ascii_code = 97
        while num < 26: # less than alphabet size
            letter = alphabet[num]
            ascii_letter = chr(ascii_code)
            letter_morse_dict[chr(ascii_code)] = letter
            
            num += 1
            ascii_code += 1
            
        final_array = []
        
        for word in words:
            final_morsecode = ""
            for letter in word:
                if letter in letter_morse_dict:
                    final_morsecode += letter_morse_dict[letter]
            final_array.append(final_morsecode)
            
        return len(set(final_array))
        
        
                    
        
        
        
            
            
            