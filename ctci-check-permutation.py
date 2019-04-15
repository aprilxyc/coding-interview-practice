""" Given two strings, write a method to decide if one is a permutation of the other."""
def check_permutation(A, B):
    # permutation means e.g. abcd is a permutation of badc
    # time complexity:
    # O(N) where N is the length of the string
    # space complexity
    # O(N) where N is the length of the string

    if len(A) != len(B):
        return False

    ht1 = {} #O(N)
    for i in A:
        if i in ht1:
            ht1[i] += 1
        else:
            ht1[i] = 1

    ht2 = {} #O(N)
    for j in B:
        if j in ht2:
            ht2[j] += 1
        else:
            ht2[j] = 1

    for i in A: #O(N)
        if i not in ht2:
            return False
        if ht1[i] != ht2[i]:
            return False
    return True

def check_permutation_optimised(A, B):
    """
    :space complexity: O(1)
    :time complexity: O(A) + O(B)
    """

    if len(A) != len(B):
        return False

    arr = [0] * 128 # initialise 128 ascii value array
    for i in A:
        index = ord(i)
        arr[index] += 1 # increment by 1

    for j in B:
        index = ord(j)
        arr[index] -= 1 # minus the count
        if arr[index] < 0:
            return False
    return True


if __name__ == "__main__":
    # print(check_permutation("april", "prial"))
    print(check_permutation_optimised("yameb", "maybe"))

