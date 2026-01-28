class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}


        for i in range(len(nums)):
            lookfor = target - nums[i]

            if lookfor in hashmap:
                return [hashmap[lookfor], i]
                
            hashmap[nums[i]] = i

        return []

        