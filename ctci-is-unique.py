# ctci q1.1 is-unique
""" Implement an algorithm to determine if a string has al unique characters. What if you cannot use
additional data structures?"""
# abcde --> True

# with data structure
def is_unique_with_ds(array):
    ht = {} # create hash table
    for i in range(len(array)): # put everything into the hash table [a, b, c, d] len = 4
        if array[i] in ht: #
            ht[array[i]] += 1
        else:
            ht[array[i]] = 1

    for j in ht: #{a:1, b:1, c:1, d:1} len = 4
        if ht[j] != 1:
            return False
    return True

def is_unique_without_ds(string): # create a boolean array
    arr = [False] * 128 # 128 elements of ASCII
    # go through all characters in string and flip the value in the array to true
    # if we encounter true, we know string is not unique
    for char in string:
        index = ord(char) # get ASCII value
        if arr[index]: # if True, then we know we have encountered it before
            return False
        arr[index] = True # first time we encounter it, it is true

    return True


if __name__ == "__main__":
    # print(is_unique_with_ds(["a", "b", "c", "d", "d", "e"]))
    print(is_unique_without_ds(["a", "b", "c", "a"]))



