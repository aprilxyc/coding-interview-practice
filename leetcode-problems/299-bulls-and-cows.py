class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = {}
        g = {}
        cow = 0
        bull = 0
        
        for i in range(0, len(secret)):
            if secret[i] == guess[i]: # checks if they are same letters in the same place
                bull += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1 # otherwise create a dictionary and count their occurrences
                g[guess[i]] = g.get(guess[i], 0) + 1
        
        for k in s:
            if k in g:
                cow += min(s[k], g[k])
        
        return '{0}A{1}B'.format(bull, cow)

"""
secret = "1123", guess = "0111"

sec_table = {1:[0, 1], 2: [2], 3: [3]}

0111


"""