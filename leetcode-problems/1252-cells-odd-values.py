# nested list comprehension example
# answer = [[i*j for i in range(1, j+1)] for j in range(1, 8)]
indices = [[0,1],[1,1]]
matrix = [[0 for a in range(3)] for b in range(2)]
print(matrix)

def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

    # O(N^2) because it has to go through the list of indices and when it goes through, it has to 
    # go through the number of numbers to change

    # create the matrix using a nested list comprehension
    matrix = [[0 for i in range(m)] for i in range(n)] # learn this properly and memorise!
    
    # loop through the indices list
    for i in indices:
        
        # go through the matrix and increment this row
        for j in range(m):
            matrix[i[0]][j] += 1
        
        # go through the matrix and increment the column
        for j in range(n):
            matrix[j][i[1]] += 1
    
    # then go through the matrix and count which numbers are odd
    odd_count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] % 2 != 0:
                odd_count += 1
    return odd_count

# my most recent attempt 11/01/ 2020
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        # create the matrix
        matrix = [[0 for i in range(m)] for j in range(n)] # [[1,3,1],[1,1,1]].

        for i in indices: #[[0,1],[1,1]]
            row = i[0] # 1
            col = i[1] # 1
        
            # now increment the col
            for j in range(0, len(matrix)):
               matrix[j][col] += 1
            
            # increment the entire row
            matrix[row]= [s + 1 for s in matrix[row]]
            
        # find the number of cells with odd values
        result = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 != 0:
                    result += 1
        return result
            