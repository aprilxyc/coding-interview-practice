"""
Leetcode problem 832
"""

def flipInvertImage(A):
    for i in range(len(A)):
        pointerA = 0
        pointerB = len(A[i]) - 1
        while pointerA < pointerB:
            temp = A[i][pointerA]
            A[i][pointerA] = A[i][pointerB]
            A[i][pointerB] = temp
            pointerA += 1
            pointerB -= 1

        j = 0
        while j < len(A[i]):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0
            j += 1
    
    return A