"""
https://leetcode.com/problems/island-perimeter/
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        if grid == []:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    count += 4
                    # add the constraint j > 0 and i >0 to avoid out of index errors
                    if j > 0 and grid[i][j - 1]:
                        count -= 2
                    if i > 0 and grid[i - 1][j]:
                        count -= 2
        return count
        
        