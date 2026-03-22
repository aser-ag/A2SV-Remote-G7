class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = []

        for i in range(len(nums)):
            if i == 0:
                self.prefix.append(nums[i])
            else:
                self.prefix.append(nums[i] + self.prefix[i - 1])
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        #- 2, 0, 3, -5, 2, -1
        # -2, -2, 1, -4, -2, -3

        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)