class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #let's reason. How do i know a point's in between? Not by y, but by x axis
        #so, sort by x axis, to have smallest differences, then it's a s;iding window

        points.sort()
        holder = 0
        widest = 0

        for i in range(1, len(points)):
            distance = points[i][0] - points[i - 1][0]
            widest = max(widest, distance)
        
        return widest