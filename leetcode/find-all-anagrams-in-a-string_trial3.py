class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        k = len(p)
        result = []

        if k > n:
            return []

        # fixed window
        # build target        
        target = {}
        for i in range(k):
            c = p[i]
            target[c] = target.get(c, 0) + 1
            
        # build first window
        window = {}
        count = 0
        for i in range(k):
            c = s[i]
            window[c] = window.get(c, 0) + 1

        for c in window:
            if c in target:
                if target[c] == window[c]:
                    count += target[c]

        if count == k:
            result.append(0)
        
        # slide window
        for i in range(k, n):
            left = s[i - k]
            right = s[i]
            
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            
            window[right] = window.get(right, 0) + 1

            count = 0
            for c in window:
                if c in target:
                    if target[c] == window[c]:
                        count += target[c]

            #print(window, count, i)
            if count == k:
                result.append(i - k + 1)  

        return result          