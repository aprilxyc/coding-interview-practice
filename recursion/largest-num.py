"""
Find the largest number in the array
"""
def largestNum(array, size):
    if size == 0:
        return 0
    else:
        lastElem = array[size-1]
        return max(largestNum(array, size - 1), lastElem)

print(largestNum([1,2,1,5,3,4], 6))

[https://stackoverflow.com/questions/19590242/finding-max-value-in-an-array-using-recursion]