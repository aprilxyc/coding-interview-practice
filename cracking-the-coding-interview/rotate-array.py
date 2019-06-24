def rotate_array(nums, k):
	while k > 0:
		temp = nums[0]
		for i in range(len(nums) - 1):
			nums[i] = nums[i + 1]
		nums[-1] = temp
		k -= 1
		print(nums)
	print(nums)

rotate_array([1, 2, 3, 4, 5, 6, 7], 4)
