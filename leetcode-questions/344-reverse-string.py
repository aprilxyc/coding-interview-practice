class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        
        for i in range(len(s) // 2):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1

# optimise this!