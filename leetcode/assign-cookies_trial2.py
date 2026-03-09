class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        greed = 0
        size = 0
        count = 0

        while greed < len(g) and size < len(s):
            if g[greed] > s[size]:
                size += 1
            else:
                count += 1
                greed += 1
                size += 1
        
        return count
