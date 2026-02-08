class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = [[], []]
        losses = {}
        wins = {}
        players = ()

        for item in matches:
            losses[item[1]] = losses.get(item[1], 0) + 1

        for item in matches:
            wins[item[0]] = wins.get(item[0], 0) + 1
        
        for player in wins:
            if player not in losses:
                answer[0].append(player)
        
        for player in losses:
            if losses[player] == 1:
                answer[1].append(player)

        answer[0].sort()
        answer[1].sort()

        return answer
