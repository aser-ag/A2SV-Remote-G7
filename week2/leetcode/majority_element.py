class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
            if dictionary[num] > len(nums)/2:
                return num
        
