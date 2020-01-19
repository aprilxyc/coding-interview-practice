"""
https://leetcode.com/problems/sort-array-by-parity/
"""

# odd must be on left and even MUST BE on right as we want even to be on the left
def sortArrayByParity(self, A: List[int]) -> List[int]:
    # pointer for odd
    # pointer for even
    # if the element is odd, keep it there
    # move even pointer until it reaches a number that is even
    # swap them then increment both pointers by 1
    
    odd = 0
    even = len(A) - 1
    
    while odd < even:
        if A[odd] % 2 != 0 and A[even] % 2 == 0:
            A[odd], A[even] = A[even], A[odd]
            odd += 1
            even -= 1
        if A[odd] % 2 == 0:
            odd += 1
        if A[even] % 2 != 0:
            even -= 1
    return A
        