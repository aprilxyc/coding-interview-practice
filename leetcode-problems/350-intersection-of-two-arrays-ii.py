"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Good solution to look at:
https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82247/Three-Python-Solutions

What if the given array is already sorted? How would you optimize your algorithm? Use pointers
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

- Be careful of intersection of two arrays (whether they want all occurrences of duplicates or not) - a dictionary can only keep 1 id in it so you cannot use this if the question asks for all occurrences (icludig duplicates) - use pointers here
"""

# note this solution below is incorrect because I didn't read the question properly.
# It wants to show ALL occurrences of numbers including duplicates so you cannot just use set or a dictiomary that only stores it once
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
# possibilities once we have traversed the sections that concern our numbers. However, sorting takes up extra time with heapsort for NlogN.
# CORRECT SOLUTION HERE
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # Time complexity: O(m + n) where m is num of elements in nums1 and n is num of elements in nums2
    # O(max(m, n)) where it is the longest list that we have to go through 
    res = []
    
    # sort it first and it will be faster to get the result
    nums1.sort()
    nums2.sort()
    
    index_i, index_j = 0, 0
    while index_i < len(nums1) and index_j < len(nums2):
        if nums1[index_i] == nums2[index_j]:
            res.append(nums1[index_i])
            index_i += 1
            index_j += 1
        elif nums1[index_i] > nums2[index_j]:
            index_j += 1
        else:
            index_i += 1
    return res
    
class Solution(object):
def intersect(self, nums1, nums2):

    counts = {}
    res = []

    for num in nums1:
        counts[num] = counts.get(num, 0) + 1

    for num in nums2:
        if num in counts and counts[num] > 0:
            res.append(num)
            counts[num] -= 1

    return res