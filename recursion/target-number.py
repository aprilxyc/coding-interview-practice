"""
Write a function that is passed an array of integers and a “target” number
and that returns the number of occurrences of the target in the array. Solve
the problem first using iteration, then recursion.

Question: 6-3 https://nostarch.com/download/samples/TLAP_ch6.pdf
"""
def targetRecursive(array, target, size):
    if size == 0:
        return 0
    else:
        lastElem = array[size - 1]
        if lastElem == target:
            return targetRecursive(array, target, size -1) + 1
        return targetRecursive(array, target, size - 1)

print(targetRecursive([1, 2, 2, 0, 2], 1, 5))