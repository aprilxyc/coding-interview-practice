"""
Problem 905
"""

def sortArrayByParity(A):
    # similar to quicksort partitioning with LBAD and RBAD
    left_even = 0
    right_odd = len(A) - 1
    while left_even <= right_odd:
        while left_even <= right_odd and A[left_even] % 2 == 0:
            left_even += 1
        while left_even <= right_odd and A[right_odd] % 2 != 0:
            right_odd -= 1
        if left_even <= right_odd:
            A[left_even], A[right_odd] = A[right_odd], A[left_even]
    return A

    # practise https://www.youtube.com/watch?v=LsDeiI3yhG0 for
    # more optimal solutions