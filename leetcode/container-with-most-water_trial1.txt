class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        n = len(height)
        left, right = 0, n - 1

        while left < right:
            if height[left] < height[right]:
                current = height[left] * (right - left)
                max_vol = max(current, max_vol)
                left += 1
            else:
                current = height[right] * (right - left)
                max_vol = max(current, max_vol)
                right -= 1
        
        return max_vol