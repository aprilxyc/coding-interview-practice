"""
LeetCode Problem 942
Time Complexity: O(N) where N is the length of the string
Space Complexity: O(N) where N is the length of the string
"""
def diStringMatch(S):
    list_size = len(S)
    low = 0
    high = list_size

    output_array = []

    i = 0
    while i < list_size:
        if S[i] == 'I':
            output_array.append(low)
            low += 1
        else:
            output_array.append(high)
            high -= 1
        i += 1

    output_array.append(high)
    return output_array



