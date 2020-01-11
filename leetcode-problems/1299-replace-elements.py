"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
"""

# this solution times out :(
def replaceElements(self, arr: List[int]) -> List[int]:
for i in range(len(arr) - 1):
    max_num = max(arr[i + 1 :])
    arr[i] = max_num

arr[len(arr) - 1] = -1

return arr

# optimised solution
# study this one
[https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/discuss/463645/Python-3-(two-lines)-(72-ms)-(beats-100)-(With-Explanation)-(-O(n)-time-)-(-O(1)-space-)]

# my solution
def replaceElements(self, arr: List[int]) -> List[int]:
    max_num = -1
    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]
        arr[i] = max_num
        max_num = max(max_num, temp)
    return arr

# shorter solution 
def replaceElements(aList):
    max_num = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], max_num = max_num, max(arr[i], max_num)
    return arr
