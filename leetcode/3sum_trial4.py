class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        left = 0
        res = []

        while left < n:
            if left > 0 and nums[left] == nums[left - 1]:
                left += 1
                continue

            middle, right = left + 1, n - 1

            while middle < right:
                if nums[middle] + nums[right] == -1 * nums[left]:                    
                    res.append([nums[left], nums[middle], nums[right]])

                    middle += 1
                    while middle < n and nums[middle] == nums[middle - 1]:
                        middle += 1
                    
                    while right > -1 and nums[right] == nums[right - 1]:
                        right -= 1

                elif nums[left] + nums[middle] + nums[right] < 0:
                    middle += 1

                else:
                    right -= 1
            
            left += 1

        return res
        