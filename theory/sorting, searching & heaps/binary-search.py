# divide and conquer strategy

# recursive solution
def binary_search(arr, lo, hi, target):
    if lo == hi: # edge case
        if arr[lo] == target:
            return lo
        else:
            return 0
    else:
        mid = (lo + hi) // 2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            return binary_search(lo, mid - 1, target)
        else:
            return binary_search(mid + 1, hi, target)

# iterative solution
def binary_search(arr, num_elements, key):
    low, hi = 0, num_elements

    mid = (lo + hi) // 2

    while lo <= hi:
        if key == arr[mid]:
            return mid
        if key < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

