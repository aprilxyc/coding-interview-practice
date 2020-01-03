https://leetcode.com/problems/single-number/discuss/468420/Python3-Bitwise-and-Non-Bitwise-Solutions-(w-Explanation)

# study this
def singleNumber(self, nums: List[int]) -> int:
	sol = 0
	for n in nums:
		sol ^= n

	return sol