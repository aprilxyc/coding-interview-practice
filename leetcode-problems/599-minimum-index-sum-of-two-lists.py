"""
https://leetcode.com/problems/minimum-index-sum-of-two-lists/
"""

# this does not handle when there are two sum indexes that are equal

import math
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurant_dict = {}
        for index, item in enumerate(list1):
            restaurant_dict[item] = index
        
        min_value = math.inf
        for index, item in enumerate(list2):
            if item in restaurant_dict:
                sum_index = (index + restaurant_dict[item])
                if sum_index < min_value:
                    min_value = sum_index
                    result = item
                
        return [result]

# better solution
# time complexity is O(max(N,M)) where N is the num of elements in list1 and M is the number of elements in list2
import math
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurant_dict = {}
        
        if len(list1) < len(list2):
            l = list1
            for index, item in enumerate(list2):
                restaurant_dict[item] = index
        else:
            l = list2
            for index, item in enumerate(list1):
                restaurant_dict[item] = index

        min_sum = float('inf')
        output = []
        
        for i in range(len(l)):
            item = l[i]
            index = restaurant_dict.get(item, 10001)
            new_sum = index + i
            if new_sum < min_sum:
                min_sum = new_sum
                output = [item]
            elif new_sum == min_sum:
                output.append(item)
        
        return output