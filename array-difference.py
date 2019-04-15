def find_difference(array, k):

    # finding something quickly in an unsorted array --> use a hash table
    # [ 1, 7, 5, 9, 12, 3]
    nums_table = {}
    for i in range(len(array)): # go through the array O(n)
        nums_table[array[i]] = 0 # initialise every value to 0

    # we have the hash table
    # go through the array again
    pairs_list = []
    for i in range(len(array)): #O(N)
        if array[i] + k in nums_table:
            pairs_list.append((array[i], array[i] + k))
        elif array[i] - k in nums_table:
            pairs_list.append((array[i] - k, array[i]))
    pairs_list = set(pairs_list)
    return pairs_list

print(find_difference([1, 7, 5, 9, 12, 3], 2))
