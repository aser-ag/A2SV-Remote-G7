class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # a ^ 2 + b ^ 2 = c implies that abs(a) < c and abs(b) < c
        # therefore if a and b exist, they are in the range [abs(a), c]
        # i don't have a, though, and I can disregard -ve numbers since they're equal to squared +ves
        # therefore if a and b exist, they are in the range [0, c]
        # colliding pointers?

        # also, 0 will make the property true as long as the other number is a perfect square
        # so if a and b exist, they are in the range [0, c ^ 0.5]
        bound = int(floor(c ** 0.5))
        # nums = [i for i in range(bound + 1)]
        left, right = 0, bound

        # print(nums)
        while left <= right:
            # print(nums[left], nums[right])
            if left ** 2 + right ** 2 == c:
                return True
            
            elif left ** 2 + right ** 2 < c:
                left += 1
            
            else:
                right -= 1
        
        return False