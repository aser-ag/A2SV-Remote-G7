class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        nums = sorted(list(nums_set))
        n = len(nums)

        if n >= 3:
            return nums[-3]
        else:
            return nums[-1]
        