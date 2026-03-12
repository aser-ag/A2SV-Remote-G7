class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        len_p = len(players)
        len_t = len(trainers)

        p, t = 0, 0
        count = 0

        while p < len_p and t < len_t:
            if players[p] <= trainers[t]:
                count += 1
                p += 1
                t += 1
            else:
                while t < len_t and players[p] > trainers[t]:
                    t += 1
        
        return count