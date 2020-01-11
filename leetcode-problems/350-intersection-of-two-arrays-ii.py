"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

What if the given array is already sorted? How would you optimize your algorithm? Use pointers
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        num_dict = {}
        for i in nums1:
            if i not in num_dict:
                num_dict[i] = 0 # add it to dictionary
                
        result = []
        for i in nums2:
            if i in num_dict:
                result.append(i)
        
        return result

    
# optimise algorithm if sorted
# you can simply use pointers to find your algorithm
# this may be faster because in the other one, the number could be anyway. Here, we know where it is already and can quicly eliminate other 
# possibilities once we have traversed the sections that concern our numbers
    
    