class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(s), len(t)
        i = 0
        j = 0

        while i < n and j < m:
            if s[i] == t[j]:
                j += 1
            
            i += 1
        
        return m - j