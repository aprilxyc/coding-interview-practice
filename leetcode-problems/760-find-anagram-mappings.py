# my initial slower solution
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        # this is O(N) where N is the number of elements

        output_list = [] # initialise the output list
        matching_indexes = {} # initalise the dictionary to hold the final indices

        for i in range(len(B)): # loop through the elements in B
            matching_indexes[B[i]] = i # set up the dictionary where it is {element : index}

        for i in A: # go through the elements in A
            output_list.append(matching_indexes[i]) # get the element's index in B

        return output_list

# optimised solution
# REVISE THIS ONE
B = [23, 5, 3, 6]
matching_indexes = {}
for i, j in enumerate(B):
    if j not in matching_indexes:
        matching_indexes[j] = []
    matching_indexes[j].append(i)
return [matching_indexes[a].pop() for a in A]

# 11/01 solution
def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
    values_dict = {}
    for i, b in enumerate(B):  # get the index, value of list B e.g. d = {50: 0, 12: 1, 32: 2, 46: 3, 28: 4}
        if b not in values_dict:
            values_dict[b] = [] # d = {50: [], 12: []}
        values_dict[b].append(i) # add the value into the dictionary value d = {50: [0],  12: [1], 32: [2], 46: [3], 28: [4]}
    
    result = []
    for i in A: # iterate through the A values
        value_taken = values_dict[i].pop()
        result.append(value_taken)
    return result
            