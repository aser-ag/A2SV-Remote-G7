class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        original = len(nums)
        n = original * 2
        ans = [0] * n

        for i in range(n):
            if i < original:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i % original]
        
        return ans