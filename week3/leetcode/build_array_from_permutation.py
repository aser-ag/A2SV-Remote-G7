class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = []

        for num in nums:
            nums2.append(nums[num])
        
        return nums2