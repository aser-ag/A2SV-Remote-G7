class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        
        i = 0
        while i < len(ranges):
            if left > right:
                return True

            if ranges[i][0] <= left and left <= ranges[i][1]:
                left += 1
                i = 0
            else:
                i += 1
        
        return False
        