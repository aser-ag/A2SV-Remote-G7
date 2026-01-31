class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in range(len(strs[0])):
            char = strs[0][i]

            for j in range(1, len(strs)):

                if len(strs[j]) < i or strs[j][i] != char:
                    return strs[0][:i]
        
        return strs[0]