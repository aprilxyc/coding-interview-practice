"""
https://leetcode.com/problems/combination-sum-ii/
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates or candidates is None:
            return []
        
        path = []
        result = []
        index = 0
        candidates.sort()
        self.comboSumHelper(candidates, target, index, path, result)
        return result
    
    def comboSumHelper(self, candidates, target, index, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        
        for i in range(index, len(candidates)):
            if candidates[i] == candidates[i - 1] and i > index:
                continue
            self.comboSumHelper(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)
        
            