class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest = float('inf')
        result = 0

        for left in range(n):
            middle, right = left + 1, n - 1

            while middle < right:
                s = nums[left] + nums[middle] + nums[right]
                current = abs(s - target)
                if current < closest:
                    closest = current
                    result = s

                if s == target:
                    return target

                elif s < target:
                    middle += 1

                else:
                    right -= 1
        
        return result