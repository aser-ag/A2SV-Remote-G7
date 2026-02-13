class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        size = len(s)
        shuffled_string = [''] * size

        for i in range(size):
            shuffled_string[indices[i]] = s[i]
        
        return "".join(shuffled_string)