class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = 0, n - 1
        maximum = 0

        while left < right:
            lesser = min(height[left], height[right])
            volume = (right - left) * lesser

            maximum = max(maximum, volume)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maximum