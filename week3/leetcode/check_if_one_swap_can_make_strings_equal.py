class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_arr = sorted(list(s1))
        s2_arr = sorted(list(s2))
        count = 0
        
        for i in range(len(s1_arr)):
            if s1_arr[i] != s2_arr[i]:
                return False
        
        for i in range(len(s1)):
            if count > 2:
                return False
            if s1[i] != s2[i]:
                count += 1
            
        return count == 2 or count == 0