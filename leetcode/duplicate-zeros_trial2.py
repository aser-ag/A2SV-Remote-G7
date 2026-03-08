class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        result = []
        
        for num in arr:
            result.append(num)
            if num == 0:
                result.append(0)
        
        for i in range(n):
            arr[i] = result[i]