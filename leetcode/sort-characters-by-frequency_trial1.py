class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        arr = []
        for key in freq:
            arr.append([freq[key], key])
        arr.sort(reverse=True)
        result = []

        for item in arr:
            for i in range(item[0]):
                result.append(item[1])

        return "".join(result) 
