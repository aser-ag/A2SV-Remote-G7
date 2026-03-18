class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        # fixed sliding window, count white blocks
        # track minimum

        n = len(blocks)
        whites = 0
        min_ops = float('inf')

        for i in range(k):
            if blocks[i] == 'W':
                whites += 1
        
        min_ops = min(min_ops, whites)

        left = 0
        for right in range(k, n):
            if blocks[right] == 'W':
                whites += 1

            if blocks[left] == 'W':
                whites -= 1

            left += 1
            
            min_ops = min(min_ops, whites)

        return min_ops