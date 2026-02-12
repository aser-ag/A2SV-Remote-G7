class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        smaller_count = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in smaller_count:
                smaller_count[sorted_nums[i]] = i
        
        return [smaller_count[num] for num in nums]