"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
    if len(numbers) < 2:
        return False
    
    lo = 0
    hi = len(numbers) - 1
    while lo < hi:
        if numbers[lo] + numbers[hi] > target:
            hi -= 1
        elif numbers[lo] + numbers[hi] < target:
            lo += 1
        else:
            return lo + 1, hi + 1

# trying this with binary search
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/425994/Python-solution-(with-comments)-beat-99.95
def twoSum(self, numbers, target):
    for i in xrange(len(numbers)):
    l, r = i+1, len(numbers)-1
    tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1