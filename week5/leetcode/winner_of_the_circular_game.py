class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        players = [0] * n

        for i in range(n):
            players[i] = i + 1
        
        index = 0
        while len(players) > 1:
            index = (index + k - 1) % len(players)
            players.pop(index)
        
        return players[0]
