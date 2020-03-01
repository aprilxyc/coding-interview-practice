"""
https://leetcode.com/problems/top-k-frequent-elements/
"""

# this took like an hour or so of broken implementation times 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums or nums is None:
            return []
        
        heap = []
        freq_table = {}
        
        for i in nums:
            freq_table[i] = freq_table.get(i, 0) + 1
        
        for item, value in freq_table.items(): 
            if len(heap) != k:
                heapq.heappush(heap, (value, item))
            else:
                if freq_table[item] >= freq_table[heap[0][1]]: 
                    removed = heapq.heappop(heap)
                    heapq.heappush(heap, (value, item))
        result = []
        for value, item in heap:
            result.append(item)
        return result
            
        