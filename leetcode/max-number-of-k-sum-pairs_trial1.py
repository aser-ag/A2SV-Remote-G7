class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] == k:
                count += 1
                left += 1
                right -= 1
            
            elif nums[left] + nums[right] < k:
                left += 1
            
            else:
                right -= 1
        
        return count