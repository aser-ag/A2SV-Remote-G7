class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left, n = 0, len(s)
        vowels = {"a", "e", "i", "o", "u"}

        max_count, current_count = 0, 0
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        
        max_count = current_count
        for right in range(k, n):
            left += 1
            if s[left - 1] in vowels:
                current_count -= 1

            if s[right] in vowels:
                current_count += 1

            # print(s[left : right + 1])
            max_count = max(max_count, current_count)
    
        return max_count