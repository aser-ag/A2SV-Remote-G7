class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort()
        current_interval = intervals[0]
        
        for i in range(1, len(intervals)):
            if current_interval[1] >= intervals[i][0]:
                current_interval[1] = max(current_interval[1], intervals[i][1])
            else:
                res.append(current_interval)
                current_interval = intervals[i]
        
        res.append(current_interval)
        
        return res