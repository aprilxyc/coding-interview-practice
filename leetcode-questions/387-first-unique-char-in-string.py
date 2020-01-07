"""
https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""

import collections

# my solution below is slow with 200ms 
# O(2N) time complexity where N is the number of elements in the string s
# O(1) space
def firstUniqChar(self, s: str) -> int:
    
    if len(s) == 1:
        return 0
    
    our_chars = [0] * 27 # create an array that will hold all the letters (27 to account for 1 indexing)
    for char in s:
        our_chars[ord(char) - ord('a') + 1] += 1
    
    # go through the array again and look it up
    for char in range(len(s)):
        if our_chars[ord(s[char]) - ord('a') + 1] == 1:
            return s.index(s[char])
    return -1
    
# some better solutions to study here with list comprehensions:
# https://leetcode.com/problems/first-unique-character-in-a-string/discuss/86351/Python-3-lines-beats-100-(~-60ms)-!

# this is extremely clean but uses in-built functions:
s = 'hello'
# build the hash map using in-built function
count = collections.Counter(s)

for index, ch in enumerate(s):
    if count[ch] == 1:
        return index
return -1
