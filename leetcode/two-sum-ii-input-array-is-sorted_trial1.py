class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0
        right = n - 1

        while numbers[left] + numbers[right] != target:
            current = numbers[left] + numbers[right]

            if current < target:
                left += 1
            
            if current > target:
                right -= 1
        
        return [left + 1, right + 1]
        
        