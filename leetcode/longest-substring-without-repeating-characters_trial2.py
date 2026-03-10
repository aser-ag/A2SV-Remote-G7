class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        occured = {}
        left = 0
        longest = 0

        for right in range(left, len(s)):
            char = s[right]

            occured[char] = occured.get(char, 0) + 1

            while occured[char] > 1:
                occured[s[left]] -= 1
                left += 1

            current = right - left + 1
            longest = max(longest, current)           
        
        return longest
            