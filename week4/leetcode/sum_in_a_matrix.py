class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        rows = len(nums)
        cols = len(nums[0])
        times = cols

        result = []
        for row in nums:
            row.sort()
        
        while times > 0:
            intermediate = []

            for row in nums:
                intermediate.append(row.pop())

            result.append(max(intermediate))
            times -= 1

        return(sum(result))