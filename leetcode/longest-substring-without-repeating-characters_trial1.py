class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # variable size sliding window
        # expand indefinitely, shrink when right becomes 2nd occurence
        # shrink from left until right has 1 occurence
        window = {}
        n = len(s)
        left = 0
        max_len = 0

        for right in range(n):
            window[s[right]] = window.get(s[right], 0) + 1
            while left < n and window[s[right]] > 1:
                window[s[left]] -= 1
                
                if window[s[left]] == 0:
                    del window[s[left]]
                
                left += 1
            
            # print(window)
            # print(s[left: right + 1])
            max_len = max(max_len, len(window))

        return max_len