https://leetcode.com/problems/single-number/discuss/468420/Python3-Bitwise-and-Non-Bitwise-Solutions-(w-Explanation)

# study this using bitwise operators (the intended solution)
def singleNumber(self, nums: List[int]) -> int:
	result = 0
	for n in nums:
		result ^= n

	return result


# double the sum of the set and remove the sum of the original array
def singleNumber(self, nums: List[int]) -> int:
	# [1, 1, 2, 2, 3] -> [1, 2, 3]
	return 2 * sum(set(nums)) - sum(nums)

# can also do this using a dictionary (not shown)

