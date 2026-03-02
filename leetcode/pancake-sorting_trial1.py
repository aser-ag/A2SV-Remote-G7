class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # 0 -> 3, 2, 4, 1
        # 3 -> 4, 2, 3, 1
        # 4 -> 1, 3, 2, 4
        # 2 -> 3, 1, 2, 4
        # 3 -> 2, 1, 3, 4
        # 2 -> 1, 2, 3, 4
        result = []

        # register indices to flip around
        n = len(arr)
        indices = {}
        for i in range(n):
            indices[arr[i]] = i

        # math
        for num in range(n, 0, -1):
            index = indices[num]
            result.append(index + 1)

            left, right = 0, index
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]

                indices[arr[left]] = left
                indices[arr[right]] = right

                left += 1
                right -= 1
            
            result.append(num)

            left, right = 0, num - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]

                indices[arr[left]] = left
                indices[arr[right]] = right

                left += 1
                right -= 1

        return result