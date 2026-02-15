class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        cols = len(matrix[0])
        rows = len(matrix)

        columns = []
        for i in range(cols):
            col = []
            for j in range(rows):
                col.append(matrix[j][i])
            col.reverse()
            columns.append(col)
        
        for i in range(rows):
            matrix[i] = columns[i]     

