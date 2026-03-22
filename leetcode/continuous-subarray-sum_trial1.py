class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_map = {0: -1}
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k
            
            if remainder in prefix_map:
                if i - prefix_map[remainder] >= 2:
                    return True
            else:
                prefix_map[remainder] = i
        
        return False

            