class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        frequency = Counter(arr1)
        res = []

        for num in arr2:
            for i in range(frequency[num]):
                res.append(num)
                frequency[num] -= 1
        
        intermediate = []
        for key in frequency:
            if frequency[key] > 0:
                for i in range(frequency[key]):
                    intermediate.append(key)
                    frequency[num] -= 1
        
        return res + sorted(intermediate)