class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        #sort
        n = len(piles)
        piles.sort(reverse=True)
        
        #from 1, every 2
        #give bob the smallest, so n/3 of the smallest are bob's

        pile = n/3
        i = 1
        total = 0

        while i < (n - pile):
            total += piles[i]
            i += 2
        
        return total
        