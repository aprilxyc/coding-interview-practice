"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
# my first instant was to just keep the frequencies
# of the letters BUT we acutally need to keep track of when
# the character last occurred
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or s is None:
            return 0
        
        if len(s) == 1:
            return 1
        
        freq_table = collections.defaultdict(int)  # {}
        i = 0
        j = 0
        max_res = 0
        freq_table[s[i]] += 1 # {a: 1, b: 1, c: }
        while j < len(s) - 1:
            j += 1
            if freq_table[s[j]] < 1:
                freq_table[s[j]] += 1
                if len(freq_table) > max_res:
                    max_res = len(freq_table)
            else:
                # already exists there
                while freq_table[s[j]] >= 1:
                    freq_table[s[i]] -= 1
                    freq_table.pop(s[i])
                    if len(freq_table) > max_res:
                        max_res = len(freq_table)
                    i += 1
                    
        return max_res
    
# this was v hard what

import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0 or s is None:
            return 0
        
        seen = {}
        left = 0
        max_res = 0
        
        for r in range(0, len(s)):
            if s[r] not in seen:
                max_res = max(max_res, r - left + 1)
            else:
                if seen[s[r]] < left:
                    max_res = max(max_res, r - left + 1)
                else:
                    left = seen[s[r]] + 1
            seen[s[r]] = r
        return max_res