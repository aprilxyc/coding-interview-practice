"""
https://leetcode.com/problems/flipping-an-image/
"""
# my solution
class Solution:
    # Time complexity: O(NM) where N is the number of elements in A and M is the length of each element
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for i in A:
            start = 0
            end = len(i) - 1
            
            for j in range(0, len(i) // 2):
                i[start], i[end] = i[end], i[start]
                end -= 1
                start += 1
            
            for k in range(0, len(i)):
                if i[k] == 1:
                    i[k] = 0
                else:
                    i[k] = 1
        return A

# better solution with explanation
# https://leetcode.com/problems/flipping-an-image/discuss/208739/Python-3-Clean-and-Correct
class Solution:

    def flipAndInvertImage(self, A):
        """
        Time:  O(mn)  [m = len(A), n = len(A[0])]
        Space: O(1)
        """
        if not A or not A[0]:
            return None

        middle = (len(A[0]) + 1) // 2
        for row in A:
            for left in range(middle):
                right = len(row) - 1 - left
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
        return A