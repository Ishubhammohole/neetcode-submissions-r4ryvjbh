class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Columns = len(matrix), len(matrix[0])
        top, bottom = 0, Rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        if not (top <= bottom):
            return False
        
        l, r = 0, Columns - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1
        return False
        

        

        