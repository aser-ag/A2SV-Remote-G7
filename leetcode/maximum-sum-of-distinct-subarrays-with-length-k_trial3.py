class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # what do I need to do?
        # maintain a set to check, and also a sliding window sum
        # the sum will be valid if len(set) == k
        n = len(nums)
        max_sum = 0
        current_sum = 0

        window = {}

        for i in range(k):
            window[nums[i]] = window.get(nums[i], 0) + 1
            current_sum += nums[i]
        
        if len(window) == k:
            max_sum = max(current_sum, max_sum)
        
        # print(nums[:k])
        # print(window)

        left = 0
        for right in range(k, n):
            current_sum += nums[right]
            window[nums[right]] = window.get(nums[right], 0) + 1

            current_sum -= nums[left]
            window[nums[left]] -= 1
            if window[nums[left]] == 0:
                del window[nums[left]]
            left += 1

            if len(window) == k:
                max_sum = max(current_sum, max_sum)
            
            # print(nums[left:right + 1])
            # print(window)
        
        return max_sum