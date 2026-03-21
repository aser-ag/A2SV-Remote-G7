class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        indices = {}
        
        for i in range(n):
            indices[i] = nums[i]

        for i in range(n):
            index = (i + k) % n
            nums[index] = indices[i]
