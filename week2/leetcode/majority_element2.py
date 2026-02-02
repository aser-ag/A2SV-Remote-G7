class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        dictionary = {}

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        
        for key in dictionary:
            if dictionary[key] > len(nums)/3:
                result.append(key)
        
        return result