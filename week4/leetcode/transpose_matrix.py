class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(cols):
            t_row = []
            for j in range(rows):
                t_row.append(matrix[j][i])
            
            output.append(t_row)

        return output