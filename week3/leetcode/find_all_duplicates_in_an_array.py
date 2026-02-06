class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
        
        return ans