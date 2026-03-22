class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_sum = nums

        for i in range(1, n):
            prefix_sum[i] = (nums[i] + nums[i  - 1])
        
        # print(prefix_sum)

        if prefix_sum[-1] - prefix_sum[0] == 0:
            return 0

        for i in range(1, n):
            if prefix_sum[-1] - prefix_sum[i] == prefix_sum[i - 1]:
                return i  
        
        return -1