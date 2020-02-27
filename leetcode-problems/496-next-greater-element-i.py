"""
https://leetcode.com/problems/next-greater-element-i/
"""

def nextGreaterElement(nums1, num2):
    greater_map = {}
    stack = []

    # preprocess and create the map that helps to get the next larger number
    for i in nums2:
        # while stack exists and the popped stack item is < i
        while stack and stack[-1] < i:
            j = stack.pop()
            greater_map[j] = in
        stack.append(i) # otherwise, just push it because it is not larger
    return [greater_map.get(i, -1) for i in nums1]