class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        width = len(image[0])
        for row in image:
            row.reverse()

            for i in range(width):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
        
        return image