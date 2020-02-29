# my very bad python solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if not numRows or numRows is None:
            return []
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        result = [[1], [1,1]]
        
        curr_row = [1,1]
        counter = 0
        while counter < numRows - 2:
            new_row = [1]
            for i in range(len(curr_row) - 1):
                total_sum = curr_row[i] + curr_row[i + 1]
                new_row.append(total_sum)
            new_row.append(1)
            curr_row = new_row
            result.append(new_row)
            counter += 1
        return result 