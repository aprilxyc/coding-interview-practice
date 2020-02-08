"""
https://leetcode.com/problems/maximum-product-of-three-numbers/
"""

def maximumProduct(nums):
    if len(nums) < 3:
        raise ValueError("We cannot have a maximum product when there are less than 3 numbers")

    highest = nums[0]
    lowest = nums[0]
    highest_product_of_2 = nums[0] * nums[1]
    lowest_product_of_2 = nums[0] * nums[1]
    #if you want the highest product of 3, then you will need to get the highest product of 2 or lowest proudt of 2 (due to negatives existing)
    # for example, you can have [1, 10, -5, 1, -100] and you could have [1, 10, 1] as the highest initially, then at the end you get -100, which means you can get 
    # 1 * -5 * -100 to be 500
    highest_product_of_3 = nums[0] * nums[1] * nums[2]

    for current in nums:
        # get the highest product of 3 by seeing what you get by multiplying the current with the highest product of 2
        highest_product_of_3 = max(highest_product_of_3, current * highest_product_of_2, current * lowest_product_of_2)

        # get the highest product of 2 by seeing what you get by multiplying the current with the highest and the lowest
        highest_product_of_2 = max(highest_product_of_2, current * highest, current * lowest)

        # get the lowest product of 2 by seeing what you get by multiplying the current with the lowest and the highest
        lowest_product_of_2 = min(lowest_product_of_2, current * lowest, current * highest)

        # get the highest by seeing whether there are anymore numbers that are higher than the highest
        highest = max(highest, current)
        # get the lowest by seeing whether there are anymore numbers that are lower than the lowest 
        lowest = min(lowest, current)
    return highest_product_of_3