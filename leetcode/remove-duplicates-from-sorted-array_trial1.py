class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        holder = 0
        unique = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[holder]:
                nums[holder + 1] = nums[i]
                holder += 1
                unique += 1
        
        return unique
            