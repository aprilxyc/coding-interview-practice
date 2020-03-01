"""
https://leetcode.com/problems/group-anagrams/
"""
# my solution after a while
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or strs is None:
            return []
        
        sorted_list = []
        result = []
        
        for index, items in enumerate(strs):
            sorted_list.append(("".join(sorted(items)), strs[index]))
        
        word_table = collections.defaultdict(list)

        for item, index in sorted_list:
            word_table[item].append(index)

        for i in word_table.values():
            result.append(i)
        return result