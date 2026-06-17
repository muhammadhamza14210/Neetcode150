class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        if not(top <= bottom):
            return False
        
        row = (top + bottom) // 2
        l, r = 0, columns - 1

        while l <= r:
            middle = (l + r) // 2
            if target == matrix[row][middle]:
                return True
            elif target > matrix[row][middle]:
                l = middle + 1
            else: 
                r = middle - 1
        
        return False

