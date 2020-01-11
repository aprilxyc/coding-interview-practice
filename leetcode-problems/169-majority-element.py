"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
"""
# brute force solution that is O(N) space complexity where N is the number of elements in the nums list
def majorityElement(self, nums: List[int]) -> int:
    num_dict = {}
    for i in range(len(nums)):
        if nums[i] in num_dict:
            num_dict[nums[i]] += 1
        else:
            num_dict[nums[i]] = 1
    
    # go through the dictionary
    for i in num_dict.keys():
        if num_dict[i] > (len(nums) // 2):
            return i

# how would you optimise this so that you don't have to go through it twice? 
# think about how you can get the frequency of something without having to use a hash table?

# we can do the checking condition within th ebody of the function and not do another loop
num_dict = {}
for i in nums: 
    if i not in num_dict:
        num_dict[i] = 1
    if num_dict[i] > (len(nums) // 2):
        return i
    else:
        num_dict[i] += 1

# you can also simply sort it
def majorityElement4(self, nums):
    nums.sort()
    return nums[len(nums)//2]
   