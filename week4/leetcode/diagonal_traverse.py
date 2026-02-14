class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
        rows = len(mat)
        cols = len(mat[0])

        diagonals = {}

        for r in range(rows):
            for c in range(cols):
                d = r + c
                if d not in diagonals:
                    diagonals[d] = []
                diagonals[d].append(mat[r][c])

        result = []

    
        for d in range(rows + cols - 1):
            if d % 2 == 0:
                result.extend(diagonals[d][::-1])
            else:
                result.extend(diagonals[d])

        return result